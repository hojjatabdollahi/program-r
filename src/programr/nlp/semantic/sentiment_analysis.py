from programr.config.brain.corenlp import BrainCoreNLPConfiguration
from programr.config.brain.nlp import BrainNLPConfiguration
from programr.config.brain.semantic_similarity import BrainSemanticSimilarityConfiguration
from programr.config.brain.sentiment_analysis import BrainSentimentAnalysisConfiguration
from programr.utils.logging.ylogger import YLogger
from programr.nlp.corenlp.client import Client

class SentimentAnalysis():


    def __init__(self,):
        pass

    @staticmethod
    def factory(config: BrainNLPConfiguration):
        if config.sentiment_analysis.method == "corenlp":
            return CoreNLPSentimentAnalysis(config.sentiment_analysis, config.corenlp)
        elif config.sentiment_analysis.method == "default":
            return DefaultSentimentAnalysis()

    def get_sentence_sentiment(self, sentence):
        raise NotImplementedError("Should be override to be used.")

    def get_sentences_sentiments(self, sentences):
        raise NotImplementedError("Should be override to be used.")

    def alpha(self):
        raise NotImplementedError("Should be override to be used.")

    def positive_threshold(self):
        raise NotImplementedError("Should be override to be used.")

    def negative_threshold(self):
        raise NotImplementedError("Should be override to be used.")



class CoreNLPSentimentAnalysis(SentimentAnalysis):

    def __init__(self, semantic_analysis_config: BrainSentimentAnalysisConfiguration, corenlp_config: BrainCoreNLPConfiguration):
        super().__init__()
        self.client = Client(corenlp_config)
        self._semantic_analysis_config = semantic_analysis_config


    def get_sentence_sentiment(self, sentence):
        return self.client.get_sentence_sentiment(sentence)

    def get_sentences_sentiments(self, sentences):
        return self.client.get_sentences_sentiments(sentences)

    def expected_sentiment_value(self, sentiment_distribution):
        shorten_sentiment_distribution = [sentiment_distribution[0]+sentiment_distribution[1],
                                          sentiment_distribution[2],
                                          sentiment_distribution[3]+ sentiment_distribution[4]]
        value = -shorten_sentiment_distribution[0] + shorten_sentiment_distribution[2]

        return value

    @property
    def alpha(self):
        return self._semantic_analysis_config.alpha

    @property
    def positive_threshold(self):
        return self._semantic_analysis_config.positive_threshold

    @property
    def negative_threshold(self):
        return self._semantic_analysis_config.negative_threshold



class DefaultSentimentAnalysis(SentimentAnalysis):

    def __init__(self):
        super().__init__()

    def get_sentence_sentiment(self, sentence):
        return

    def get_sentences_sentiments(self, sentences):
        return

    def alpha(self):
        return

    def positive_threshold(self):
        return

    def negative_threshold(self):
        return
