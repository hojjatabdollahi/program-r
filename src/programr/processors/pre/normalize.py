from programr.utils.logging.ylogger import YLogger
from programr.processors.processing import PreProcessor

class NormalizePreProcessor(PreProcessor):

    def __init__(self):
        PreProcessor.__init__(self)

    def process(self, context, word_string):
        normalized = context.brain.normals.normalise_string(word_string)
        YLogger.debug(context, "Normalising input from [%s] to [%s]", word_string, normalized)
        return normalized
