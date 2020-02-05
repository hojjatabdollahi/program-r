from newsapi import NewsApiClient

from programr.utils.logging.ylogger import YLogger
from programr.services.service import Service


class NewsAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key


    # NOTE: sources is a str to identify what news source to pull from
    #       ex: 'bbc-news'
    def headlines(self, sources=None):
        return NewsApiClient(self.api_key).get_top_headlines(sources=sources)


class NewsService(Service):

    def __init__(self, config=None, api=None):
        Service.__init__(self, config)

        api_key = '6516eee2cc744675849e70aa63cf1f39'

        if api is None:
            self._api = NewsAPI(api_key)
        else:
            self._api = api

    def get_headlines_info(self, top_headlines):
        content = top_headlines['articles'][0]['content']
        return content

    def ask_question(self, client_context, question: str):
        try:
            words  = question.split()
            question = " ".join(words[1:])
            if words[0] == 'DESCRIPTION':
                YLogger.debug(client_context, f"source: {question}")
                top_headlines = self._api.headlines(question)
                search = self.get_headlines_info(top_headlines)
            else:
                YLogger.error(client_context, "Unknown News API command [%s]", words[0])
                search = ""
            return search
        except Exception as ex:
            YLogger.error(client_context, "General error querying News API for question [%s]", question)
            YLogger.error(client_context, f"Exception message: {ex}")
        return ""