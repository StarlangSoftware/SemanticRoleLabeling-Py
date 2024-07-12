from abc import abstractmethod

from AnnotatedSentence.ViewLayerType import ViewLayerType
from Dictionary.Word import Word
from PropBank.ArgumentType import ArgumentType
from PropBank.Frameset import Frameset

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.Condition.IsTransferable import IsTransferable
from AnnotatedTree.Processor.NodeDrawableCollector import NodeDrawableCollector


class AutoArgument:

    second_language: ViewLayerType

    @abstractmethod
    def autoDetectArgument(self, parseNode: ParseNodeDrawable, argumentType: ArgumentType) -> bool:
        pass

    def __init__(self, secondLanguage: ViewLayerType):
        self.second_language = secondLanguage

    def autoArgument(self,
                     parseTree: ParseTreeDrawable,
                     frameset: Frameset):
        """
        Given the parse tree and the frame net, the method collects all leaf nodes and tries to set a propbank argument
        label to them. Specifically it tries all possible argument types one by one ARG0 first, then ARG1, then ARG2 etc.
        Each argument type has a special function to accept. The special function checks basically if there is a specific
        type of ancestor (specific to the argument, for example SUBJ for ARG0), or not.
        :param parseTree: Parse tree for semantic role labeling
        :param frameset: Frame net used in labeling.
        """
        node_drawable_collector = NodeDrawableCollector(parseTree.getRoot(), IsTransferable(self.second_language))
        leaf_list = node_drawable_collector.collect()
        for parse_node in leaf_list:
            if isinstance(parse_node, ParseNodeDrawable) and parse_node.getLayerData(ViewLayerType.PROPBANK) is None:
                for argument_type in ArgumentType:
                    if frameset.containsArgument(argument_type) and self.autoDetectArgument(parse_node, argument_type):
                        parse_node.getLayerInfo().setLayerData(ViewLayerType.PROPBANK,
                                                              ArgumentType.getPropbankType(argument_type))
                if Word.isPunctuationSymbol(parse_node.getLayerData(self.second_language)):
                    parse_node.getLayerInfo().setLayerData(ViewLayerType.PROPBANK, "NONE")
        parseTree.save()
