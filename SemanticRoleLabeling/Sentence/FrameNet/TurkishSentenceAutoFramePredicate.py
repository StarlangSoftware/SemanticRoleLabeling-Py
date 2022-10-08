from FrameNet.FrameNet import FrameNet

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from SemanticRoleLabeling.Sentence.FrameNet.SentenceAutoFramePredicate import SentenceAutoFramePredicate


class TurkishSentenceAutoFramePredicate(SentenceAutoFramePredicate):

    __frame_net: FrameNet

    def __init__(self, frameNet: FrameNet):
        """
        Constructor for TurkishSentenceAutoFramePredicate. Gets the Frames as input from the user, and sets
        the corresponding attribute.

        PARAMETERS
        ----------
        frameNet : FrameNet
            FrameNet containing the Turkish frameNet frames.
        """
        self.__frame_net = frameNet

    def autoPredicate(self, sentence: AnnotatedSentence) -> bool:
        """
        The method uses predicateFrameCandidates method to predict possible predicates. For each candidate, it sets for that
        word PREDICATE tag.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which predicates will be determined automatically.

        RETURNS
        -------
        bool
            If at least one word has been tagged, true; false otherwise.
        """
        candidate_list = sentence.predicateFrameCandidates(self.__frame_net)
        for word in candidate_list:
            if isinstance(word, AnnotatedWord):
                word.setFrameElement("PREDICATE$NONE$" + word.getSemantic())
        if len(candidate_list) > 0:
            return True
        return False
