from nltk.tokenize import sent_tokenize
from programr.utils.logging.ylogger import YLogger


class SentenceSegmentation():

    def __init__(self):
        self.split_chars = '.'

    def segment(self, text):
        raise NotImplementedError("Should be override to be used.")

    @staticmethod
    def factory(type_):
        if type_ == "spacy":
            return SpacySentenceSegmentation()

        elif type_ == "nltk":
            return NLTKSentenceSegmentation()

        elif type_ == "default":
            return DefaultSentenceSegmentation()

        else:
            YLogger.warning(SentenceSegmentation, "the module is unknown, defaulting to DefualtSentenceSegmentation")
            return None


class SpacySentenceSegmentation(SentenceSegmentation):
    def __init__(self):
        super().__init__()

    def segment(self, text):
        from programr.nlp.spacylib import spacy_lib
        doc = spacy_lib(text)
        sentences = [sent.text for sent in doc.sents]
        return sentences


class NLTKSentenceSegmentation(SentenceSegmentation):
    def __init__(self):
        super().__init__()

    def segment(self, text):
        return sent_tokenize(text)


class DefaultSentenceSegmentation(SentenceSegmentation):

    def __init__(self):
        super().__init__()

    def segment(self, text):
        return
