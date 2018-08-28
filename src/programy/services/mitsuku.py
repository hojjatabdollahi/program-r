from programy.utils.logging.ylogger import YLogger
from programy.services.service import Service
from programy.config.brain.service import BrainServiceConfiguration
import fbchat
from fbchat.models import *


class MitsukuAPI():

    def __init__(self, username, password, url="chatbots.io"):
        self._fb_client = fbchat.Client(username, password)
        mitsuku_pages = self._fb_client.searchForPages(url, 5)
        self._mitsuku_page = mitsuku_pages[0]


    def ask_question(self, message):
        return self._send(message)

    def _finditem(self, obj, key):
        if key in obj:
            return obj[key]
        for k, v in obj.items():
            if isinstance(v, dict):
                item = self._finditem(v, key)
                if item is not None:
                    return item

    def _find(self, list_of_dicts, key):
        for v in list_of_dicts:
            c = self._finditem(v, key)
            if c:
                return c

        return None

    def _receive(self, client, markAlive=True):
        client.startListening()
        client.onListening()
        while True:

            try:
                if markAlive:
                    client._ping(client.sticky, client.pool)

                content = client._pullMessage(client.sticky, client.pool)
                if content:
                    if self._find(content["ms"], "tags") == ['source:messenger:commerce']:
                        return self._find(content["ms"], "body")
                    else:
                        continue

            except KeyboardInterrupt:
                return False

    def _send(self, message):
        try:
            self._fb_client.send(Message(text=message), self._mitsuku_page.uid)
            content = self._receive(self._fb_client, True)
            #print(content)
        except:
            self._fb_client.logout()

        return content




class MitsukuService(Service):

    def __init__(self, config: BrainServiceConfiguration, api=None):
        Service.__init__(self, config)

        if api is None:
            self.api = MitsukuAPI(config.username, config.password)
        else:
            self.api = api


    def ask_question(self, client_context, question: str):
        try:
            #client_context.bot.brain.configuration
            return self.api.ask_question(question)

        except Exception as excep:
            YLogger.error(client_context, str(excep))
            return ""


