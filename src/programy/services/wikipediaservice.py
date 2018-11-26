from programy.utils.logging.ylogger import YLogger
import wikipedia

from programy.services.service import Service


class WikipediaAPI(object):

    # Provide a summary of a single article
    def summary(self, title, sentences=0, chars=0, auto_suggest=True, redirect=True):
        return wikipedia.summary(title, sentences, chars, auto_suggest, redirect)

    # Provide a list of articles matching the query
    # Use summary to return the neccassary action
    def search(self, query, results=10, suggestion=False):
        return wikipedia.search(query, results, suggestion)


class WikipediaService(Service):

    def __init__(self, config=None, api=None):
        Service.__init__(self, config)

        if api is None:
            self._api = WikipediaAPI()
        else:
            self._api = api

    def ask_question(self, client_context, question: str):
        try:
            words  = question.split()
            question = " ".join(words[1:])
            if words[0] == 'SUMMARY':
                search = self._api.summary(question, sentences=1)
            elif words[0] == 'SEARCH':
                results = self._api.search(question)
                search = ", ".join(results)
            else:
                YLogger.error(client_context, "Unknown Wikipedia command [%s]", words[0])
                search = ""
            return search
        except wikipedia.exceptions.DisambiguationError:
            YLogger.error(client_context, "Wikipedia search is ambiguous for question [%s]", question)
        except wikipedia.exceptions.PageError:
            YLogger.error(client_context, "No page on Wikipedia for question [%s]", question)
        except Exception:
            YLogger.error(client_context, "General error querying Wikipedia for question [%s]", question)
        return ""
