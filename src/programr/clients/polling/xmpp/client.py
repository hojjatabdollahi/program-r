import sleekxmpp

from programr.utils.logging.ylogger import YLogger

from programr.clients.polling.client import PollingBotClient
from programr.clients.polling.xmpp.config import XmppConfiguration
from programr.clients.polling.xmpp.xmpp import XmppClient


class XmppBotClient(PollingBotClient):

    def __init__(self, argument_parser=None):
        self._xmpp_client = None
        self._server = None
        self._port = None
        self._username = None
        self._password = None
        PollingBotClient.__init__(self, "XMPP", argument_parser)

    def get_description(self):
        return 'ProgramR AIML2.0 XMPP Client'

    def get_client_configuration(self):
        return XmppConfiguration()

    def parse_configuration(self):
        self._server = self.configuration.client_configuration.server
        self._port = self.configuration.client_configuration.port

    def get_license_keys(self):
        self._username = self.license_keys.get_key("XMPP_USERNAME")
        self._password = self.license_keys.get_key("XMPP_PASSWORD")

    def create_client(self, username, password):
        return XmppClient(self, username, password)

    def ask_question(self, userid, question):
        client_context = self.create_client_context(userid)
        response = client_context.bot.ask_question(client_context, question, responselogger=self)
        return response

    def connect(self):
        YLogger.debug(self, "XMPPBotClient Connecting as %s to %s %s", self._username, self._server, self._port)
        self._xmpp_client = self.create_client(self._username, self._password)
        if self._xmpp_client is not None:
            self._xmpp_client.connect((self._server, self._port))
            self._xmpp_client.register_xep_plugins(self.configuration.client_configuration)
            return True
        return False

    def display_connected_message(self):
        print ("XMPP Bot connected and running...")

    def poll_and_answer(self):

        running = True
        try:
            self._xmpp_client.process(block=True)
            print("XMPP client exiting cleanly....")
            running = False

        except KeyboardInterrupt:
            print("XMPP client stopping via keyboard....")
            running = False

        except Exception as excep:
            YLogger.exception(self, "Failed to poll and answer", excep)

        return running


if __name__ == '__main__':

    print("Loading Xmpp client, please wait. See log output for progress...")
    xmpp_app = XmppBotClient()
    xmpp_app.run()
