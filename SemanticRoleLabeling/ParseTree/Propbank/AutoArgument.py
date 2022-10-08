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
