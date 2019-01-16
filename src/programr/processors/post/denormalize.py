from programr.utils.logging.ylogger import YLogger
from programr.processors.processing import PostProcessor

class DenormalizePostProcessor(PostProcessor):

    def __init__(self):
        PostProcessor.__init__(self)

    def process(self, context, word_string):
        denormalized = context.brain.denormals.denormalise_string(word_string)
        YLogger.debug(context, "Denormalising input from [%s] to [%s]", word_string, denormalized)
        return denormalized
