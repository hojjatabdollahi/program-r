from programy.utils.logging.ylogger import YLogger
import requests

from programy.services.service import Service
from programy.config.brain.service import BrainServiceConfiguration


class RestAPI(object):

    def get(self, url):
        return requests.get(url)

    def post(self, url, data):
        return requests.post(url, data=data)


class GenericRESTService(Service):

    def __init__(self, config: BrainServiceConfiguration, api=None):
        Service.__init__(self, config)

        if api is None:
            self.api = RestAPI()
        else:
            self.api = api

        if config.method is None:
            self.method = "GET"
        else:
            self.method = config.method

        if config.host is None:
            raise Exception("Undefined host parameter")
        self.host = config.host

        self.port = None
        if config.port is not None:
           self.port = config.port

        self.url = None
        if config.url is not None:
           self.url = config.url

    def _format_url(self):
        if self.port is not None:
            host_port = "http://%s:%s"%(self.host, self.port)
        else:
            host_port = "http://%s"%self.host

        if self.url is not None:
            return "%s%s"%(host_port, self.url)
        else:
            return host_port

    def _format_payload(self, client_context, question):
        return {}

    def _format_get_url(self, url, client_context, question):
        return url

    def _parse_response(self, text):
        return text

    def ask_question(self, client_context, question: str):

        try:
            url = self._format_url()

            if self.method == 'GET':
                full_url = self._format_get_url(url, client_context, question)
                response = self.api.get(full_url)
            elif self.method == 'POST':
                payload = self._format_payload(client_context, question)
                response = self.api.post(url, data=payload)
            else:
                raise Exception("Unsupported REST method [%s]"%self.method)

            if response.status_code != 200:
                YLogger.error(client_context, "[%s] return status code [%d]", self.host, response.status_code)
            else:
                return self._parse_response(response.text)

        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)

        return ""
