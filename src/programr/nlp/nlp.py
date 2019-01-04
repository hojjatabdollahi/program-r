from programr.config.brain.nlp import BrainNLPConfiguration
from programr.nlp.linguistic_features.sentence_segmentation import SentenceSegmentation
from programr.nlp.linguistic_features.tokenizer import Tokenizer
from programr.nlp.semantic.semantic_similarity import SemanticSimilarity
from programr.nlp.semantic.sentiment_analysis import SentimentAnalysis
from programr.utils.logging.ylogger import YLogger
import nltk


class NLP(object):

    def __init__(self, configuraion: BrainNLPConfiguration):
        self._tokenizer = Tokenizer.factory(configuraion.tokenizer.libname)
        self._sentence_segmentation = SentenceSegmentation.factory(configuraion.sentence_segmentation.libname)
        self._semantic_similarity = SemanticSimilarity.factory(configuraion.semantic_similarity.method)
        self._sentiment_analysis = SentimentAnalysis.factory(configuraion)
        self._load_libraries(configuraion.nltk_data_dir)

    @property
    def tokenizer(self):
        return self._tokenizer

    @property
    def sentence_segmentation(self):
        return self._sentence_segmentation

    @property
    def semantic_similarity(self):
        return self._semantic_similarity

    @property
    def sentiment_analysis(self):
        return self._sentiment_analysis

    def _load_libraries(self, nltk_data_dir):
        nltk.download("popular", download_dir=nltk_data_dir, quiet=True)
