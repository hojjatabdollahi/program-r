from programy.nlp.nlp import NLP


class SentenceSegmentation(NLP):

    def __init__(self):
        super().__init__()
        self.split_chars = '.'


    def segment(self, text):
        doc = self._spacy(text)
        sentences = [sent.text for sent in doc.sents]
        return sentences



if __name__ == "__main__":
    tok = SentenceSegmentation()
    print(tok.segment("I am sad. I am happy."))
