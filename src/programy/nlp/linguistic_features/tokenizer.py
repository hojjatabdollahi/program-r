from programy.nlp.nlp import NLP


class Tokenizer(NLP):

    def __init__(self):
        super().__init__()
        self.split_chars = '.'

    def tokenize(self, text):
        doc = self._spacy(text)
        tokens_text = [token.text for token in doc]
        return tokens_text


    def texts_to_words(self, texts):
        if not texts:
            return []
        return [word.strip() for word in texts.split(self.split_chars) if word]

    def words_to_texts(self, words):
        if not words:
            return ''
        to_join = [word.strip() for word in words if word]
        return self.split_chars.join(to_join)

    def words_from_current_pos(self, words, current_pos):
        if not words:
            return ''
        return self.split_chars.join(words[current_pos:])

    def compare(self, value1, value2):
        return value1 == value2


if __name__ == "__main__":
    tok = Tokenizer()
    print(tok.tokenize("I am sad. I am happy"))
