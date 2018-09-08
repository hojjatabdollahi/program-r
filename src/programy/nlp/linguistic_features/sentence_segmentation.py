from programy.nlp.spacylib import spacy_lib
from programy.utils.logging.ylogger import YLogger

class SentenceSegmentation():

    def __init__(self):
        self.split_chars = '.'


    def segment(self, text):
        raise NotImplementedError("Should be override to be used.")

    @staticmethod
    def factory(type_):
        if type_ == "spacy":
            return SpacySentenceSegmentation()

        elif type_ == "default":
            return DefaultSentenceSegmentation()

        else:
            YLogger.warning(SentenceSegmentation, "the module is unknown, defaulting to DefualtSentenceSegmentation")
            return None



class SpacySentenceSegmentation(SentenceSegmentation):
    def __init__(self):
        super().__init__()


    def segment(self, text):
        doc = spacy_lib(text)
        sentences = [sent.text for sent in doc.sents]
        return sentences


class DefaultSentenceSegmentation(SentenceSegmentation):

    def __init__(self):
        super().__init__()


    def segment(self, text):
        return