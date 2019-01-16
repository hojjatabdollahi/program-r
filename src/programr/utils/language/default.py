import re


class DefaultLangauge(object):
    SENTENCE_SPLIT_CHARS = r'[\.?!;:]'
    WORD_SPLIT_CHARS = r'\s+'

    @staticmethod
    def split_into_sentences(text):
        raw = re.split(DefaultLangauge.SENTENCE_SPLIT_CHARS, text)
        return [sentence.strip() for sentence in raw if sentence]

    @staticmethod
    def split_into_words(sentence):
        raw = re.split(DefaultLangauge.WORD_SPLIT_CHARS, sentence)
        return [word.strip() for word in raw if word]


