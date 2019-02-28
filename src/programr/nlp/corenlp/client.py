from pycorenlp import StanfordCoreNLP

from programr.config.brain.corenlp import BrainCoreNLPConfiguration
from programr.nlp.corenlp.server import StanfordCoreNLPServer


class Client():

    def __init__(self, configuration: BrainCoreNLPConfiguration):
        '''
        As you make an instance of the client the server starts to run
        '''
        corenlp_server = StanfordCoreNLPServer(corenlp_dir=configuration.jar_dir, port=configuration.port)
        corenlp_server.run()

        self._url = str(configuration.ip) + ":" + str(configuration.port)

    def get_sentence_sentiment(self, sentence):
        '''
        return values are these
        "Very negative" = 0 "Negative" = 1 "Neutral" = 2 "Positive" = 3 "Very positive" = 4
        :param sentence:
        :return:
        '''
        try:

            stanford_corenlp = StanfordCoreNLP(self._url)
            result = stanford_corenlp.annotate(sentence,
                                               properties={
                                   'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 5000,
                               })
        except Exception as ex:
            print(ex)
            return None

        sentiment = result["sentences"][0]["sentiment"].lower()
        sentiment_distribution = result["sentences"][0]["sentimentDistribution"]
        return sentiment, sentiment_distribution


    def get_sentences_sentiments(self, sentences):
        try:

            stanford_corenlp = StanfordCoreNLP(self._url)
            result = stanford_corenlp.annotate(sentences,
                                               properties={
                                   'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 5000,
                               })
        except:
            return None

        sentiments = [sentiment_info["sentiment"] for sentiment_info in result["sentences"]]
        sentiment_values = [sentiment_info["sentimentValue"] for sentiment_info in result["sentences"]]
        return sentiments, sentiment_values





if __name__ == "__main__":
    b = BrainCoreNLPConfiguration()
    b._ip= "http://localhost"
    b._port = "9000"
    #b._jar_dir = "C:/Users/DreamFace/Codes/libs/stanford-corenlp-full-2018-02-27/*"
    b._jar_dir = "/home/rohola/Codes/Python/program-r/libs/stanford-corenlp-full-2018-02-27/*"
    for i in range(100):
        c = Client(b)
        print(c.get_sentence_sentiment("I am happy."))
