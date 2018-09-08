from programy.config.brain.nlp import BrainNLPConfiguration
from programy.nlp.linguistic_features.sentence_segmentation import SentenceSegmentation
from programy.nlp.linguistic_features.tokenizer import Tokenizer
from programy.nlp.semantic.semantic_similarity import SemanticSimilarity
from programy.utils.logging.ylogger import YLogger


class NLP(object):

    def __init__(self, configuraion: BrainNLPConfiguration):
        self._tokenizer = Tokenizer.factory(configuraion.tokenizer.libname)
        self._sentence_segmentation = SentenceSegmentation.factory(configuraion.sentence_segmentation.libname)
        self._semantic_similarity = SemanticSimilarity.factory(configuraion.semantic_similarity.method)

    @property
    def tokenizer(self):
        return self._tokenizer

    @property
    def sentence_segmentation(self):
        return self._sentence_segmentation

    @property
    def semantic_similarity(self):
        return self._semantic_similarity
