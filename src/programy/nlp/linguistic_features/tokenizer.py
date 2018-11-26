from programy.nlp.spacylib import spacy_lib

class Tokenizer():

    def __init__(self,):
        self.split_chars = '.'


    def tokenize(self, text):
        raise NotImplementedError("Should be override to be used")


    @staticmethod
    def factory(type_):
        if type_ == "spacy":
            return SpacyTokenizer()

        elif type_ == "default":
            return DefaultTokenizer()

        else:
            return None



class SpacyTokenizer(Tokenizer):

    def __init__(self):
        super().__init__()
        self.split_chars = ' '

    def tokenize(self, text):
        doc = spacy_lib(text)
        tokens_text = [token.text for token in doc]
        print("tokens:  ",tokens_text)
        return tokens_text


    def texts_to_words(self, texts):
        if not texts:
            return []
        a = [word.strip() for word in texts.split(self.split_chars) if word]
        #print(a)
        return a

    def words_to_texts(self, words):
        if not words:
            return ''
        to_join = [word.strip() for word in words if word]
        #print(to_join)
        return self.split_chars.join(to_join)

    def words_from_current_pos(self, words, current_pos):
        if not words:
            return ''
        return self.split_chars.join(words[current_pos:])

    def compare(self, value1, value2):
        return value1 == value2



class DefaultTokenizer(Tokenizer):

    def __init__(self):
        pass