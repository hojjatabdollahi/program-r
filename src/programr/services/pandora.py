from programr.utils.logging.ylogger import YLogger
from xml.etree import ElementTree

from programr.services.service import Service
from programr.config.brain.service import BrainServiceConfiguration
from programr.services.requestsapi import RequestsAPI


class PandoraAPI(object):

    def __init__(self, request_api=None):
        if request_api is None:
            self._requests_api = RequestsAPI()
        else:
            self._requests_api = request_api

    def ask_question(self, url, question, botid):
        payload = {'botid': botid, 'input': question}
        response = self._requests_api.get(url, params=payload)

        if response is None:
            raise Exception("No response from pandora service")

        tree = ElementTree.fromstring(response.content)

        that = tree.find("that")
        if that is None:
            raise Exception("Invalid response from pandora service, no <that> element in xml")

        return that.text


class PandoraService(Service):

    def __init__(self, config: BrainServiceConfiguration, api=None):
        Service.__init__(self, config)

        if api is None:
            self.api = PandoraAPI()
        else:
            self.api = api

        if config.url is None:
            raise Exception("Undefined url parameter")

    def ask_question(self, client_context, question: str):
        try:
            if client_context.client.license_keys.has_key('PANDORA_BOTID'):
                botid = client_context.client.license_keys.get_key('PANDORA_BOTID')
            else:
                YLogger.error(client_context, "No variable PANDORA_BOTID found in license key file")
                return ""

            return self.api.ask_question(self._config.url, question, botid)

        except Exception as excep:
            YLogger.error(client_context, str(excep))
            return ""
