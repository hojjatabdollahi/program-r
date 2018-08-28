import json
from urllib.parse import quote

from programy.services.rest import GenericRESTService
from programy.config.brain.service import BrainServiceConfiguration


class ProgramyRESTService(GenericRESTService):

    def __init__(self, config: BrainServiceConfiguration, api=None):
        GenericRESTService.__init__(self, config, api)

    def _format_payload(self, client_context, question):
        return {'question': question, "userid": client_context.userid}

    def _format_get_url(self, url, client_context, question):
        return "%s?question=%s&userid=%s"%(url, quote(question), client_context.userid)

    def _parse_response(self, text):
        data = json.loads(text)
        if data:
            if 'response' in data[0]:
                if 'answer' in data[0]['response']:
                    return data[0]['response']['answer']
        return ""
