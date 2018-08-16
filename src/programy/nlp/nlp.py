import spacy


class NLP(object):


    def __init__(self):
        self._spacy = spacy.load("en")
        print("loaded module")

