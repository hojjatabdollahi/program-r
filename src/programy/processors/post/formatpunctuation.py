from programy.utils.logging.ylogger import YLogger
import re

from programy.processors.processing import PostProcessor

class FormatPunctuationProcessor(PostProcessor):
    def __init__(self):
        PostProcessor.__init__(self)

    def space_split(self, string):
        last = 0
        splits = []
        in_quote = None
        for i, letter in enumerate(string):
            if in_quote:
                if letter == in_quote:
                    in_quote = None
            else:
                if letter == '"' or letter == "'":
                    in_quote = letter

            if not in_quote and letter == ' ':
                splits.append(string[last:i])
                last = i + 1

        if last < len(string):
            splits.append(string[last:])

        return splits

    def process(self, context, word_string):
        YLogger.debug(context, "Formatting punctuation...")

        word_list = self.space_split(word_string)
        new_word_list = []
        for word in word_list:
            word = re.sub(r'(["|\'])\s+', r'\1', word)
            word = re.sub(r'\s+(["|\'])', r'\1', word)
            new_word_list.append(word)
        word_string = " ".join(new_word_list)
        word_string = re.sub(r'\s+([.,:;!?])', r'\1', word_string)
        word_string = re.sub(r'([@])\s+', r'\1', word_string)

        return word_string
