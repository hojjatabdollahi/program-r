from newsapi import NewsApiClient

from programr.utils.logging.ylogger import YLogger
from programr.services.service import Service


class NewsAPI(object):

    # NOTE: website of the news api
    # https://newsapi.org

    def __init__(self, api_key):
        self.api_key = api_key


    # NOTE: sources is a str to identify what news source to pull from
    #       ex: 'bbc-news'
    #       You can find a list of acceptable country codes here: 
    #       https://github.com/mattlisiv/newsapi-python/blob/master/newsapi/const.py
    def headlines(self, sources=None, country=None):
        return NewsApiClient(self.api_key).get_top_headlines(sources=sources, country=country)


class NewsService(Service):

    def __init__(self, config=None, api=None):
        Service.__init__(self, config)

        api_key = '6516eee2cc744675849e70aa63cf1f39'

        if api is None:
            self._api = NewsAPI(api_key)
        else:
            self._api = api

        self._current_article = 0

    def get_content_info(self, top_headlines):
        content = top_headlines['articles'][self._current_article]['content']
        return content

    def get_title_info(self, top_headlines):
        title = top_headlines['articles'][self._current_article]['title']
        return title

    def get_description_info(self, top_headlines):
        description = top_headlines['articles'][self._current_article]['description']
        return description

    def clean_text(self, text):
        text = text.replace("Image copyrightReutersImage caption", "")
        text = text.replace("\n", " ")
        text.encode("ascii", errors="ignore")
        # summary = re.sub('\[.*\]', '', summary)
        return text

    def format_response(self, top_headlines):
        description = self.get_description_info(top_headlines)
        title = self.get_title_info(top_headlines)
        
        # YLogger.debug(client_context, f"article description: {description}")

        search = f"The title of the article is {title}, here is a quick summary...{description} ."
        search += " Should I read the full article?"
        return search

    def ask_question(self, client_context, question: str):
        try:
            words  = question.split()
            question = " ".join(words[1:])
            if words[0] == 'SOURCE':
                top_headlines = self._api.headlines(sources=question)
                YLogger.debug(client_context, f"top_headlines: {top_headlines}")

                description = self.get_description_info(top_headlines)
                title = self.get_title_info(top_headlines)
                
                YLogger.debug(client_context, f"article description: {description}")

                search = f"The title of the article is {title}, here is a quick summary...{description}"

                # YLogger.debug(client_context, f"search: {search}")
                # YLogger.debug(client_context, f"search type: {type(search)}")
            elif words[0] == 'COUNTRY':
                top_headlines = self._api.headlines(country=question)
                search = self.format_response(top_headlines)
            elif words[0] == 'ARTICLE':
                top_headlines = self._api.headlines(country=question)
                search = self.get_content_info(top_headlines)
                search = self.clean_text(search)
            elif words[0] == 'NEXT':
                # FIXME: On second iteration of next goes to UDC category, not here
                top_headlines = self._api.headlines(country=question)
                YLogger.debug(client_context, f"top_headlines: {top_headlines}")

                self._current_article += 1
                YLogger.debug(client_context, f"current_article index: {self._current_article}")
                search = self.format_response(top_headlines)
            else:
                YLogger.error(client_context, "Unknown News API command [%s]", words[0])
                search = ""
            return search
        except Exception as ex:
            YLogger.error(client_context, "General error querying News API for question [%s]", question)
            YLogger.error(client_context, f"Exception message: {ex}")
        return ""