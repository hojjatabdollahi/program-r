from programr.utils.logging.ylogger import YLogger
from programr.services.service import Service
from programr.config.brain.service import BrainServiceConfiguration
from bs4 import BeautifulSoup
import requests


class ChomskyAPI():

    def __init__(self, url):
        self._url = url

    def ask_question(self, message):
        return self._send(message)

    def _send(self, question):
        user_input = question.replace(' ', '+')
        payload = {'input': user_input, 'questionstring': '', 'submit': 'Ask+Chomsky',
                   'botcust2': '89732c4fee7e3b9f'}

        headers = {'Connection': 'keep-alive',
                   'Cache-Control': 'max-age=0',
                   'Origin': 'http://demo.vhost.pandorabots.com',
                   'Upgrade-Insecure-Requests': '1',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
                   'Cookie': 'botcust2=89732c4fee7e3b9f; _ga=GA1.2.2084854527.1534456980',
                   }

        r = requests.post(self._url, data=payload, headers=headers)
        soup = BeautifulSoup(r.text, features="html.parser")
        answer = soup.findAll('font')[-1].text.split('\n')[-1].rstrip()
        return answer




class ChomskyService(Service):

    def __init__(self, config: BrainServiceConfiguration, api=None):
        Service.__init__(self, config)

        if api is None:
            self.api = ChomskyAPI(config.url)
        else:
            self.api = api


    def ask_question(self, client_context, question: str):
        try:
            #client_context.bot.brain.configuration
            return self.api.ask_question(question)

        except Exception as excep:
            YLogger.error(client_context, str(excep))
            return ""


