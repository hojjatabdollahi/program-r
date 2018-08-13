from pycorenlp import StanfordCoreNLP

from programy.config.brain.corenlp import BrainCoreNLPConfiguration
from programy.nlp.corenlp.server import StanfordCoreNLPServer


class Client():

    def __init__(self, configuration: BrainCoreNLPConfiguration):
        '''
        As you make an instace of the client the server starts to run
        '''
        corenlp_server = StanfordCoreNLPServer(corenlp_dir=configuration.jar_dir)
        corenlp_server.run()
        #self._ip = 'http://localhost:9000'

        self._url = str(configuration.ip) + ":" + str(configuration.port)


    def get_sentence_sentiment(self, sentence):
        try:
            nlp = StanfordCoreNLP(self._url)
            result = nlp.annotate(sentence,
                                  properties={
                                   'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 5000,
                               })
        except:
            return None


        return result["sentences"][0]["sentiment"], result["sentences"][0]["sentimentValue"]



