import re

from programr.utils.logging.ylogger import YLogger
from abc import ABCMeta, abstractmethod

from programr.clients.client import BotClient
from programr.clients.restful.config import RestConfiguration

class RestBotClient(BotClient):
    __metaclass__ = ABCMeta

    def __init__(self, id, argument_parser=None):
        BotClient.__init__(self, id, argument_parser)
        self.api_keys = []

    def get_client_configuration(self):
        return RestConfiguration("rest")

    def load_api_keys(self):
        if self.configuration.client_configuration.use_api_keys is True:
            if self.configuration.client_configuration.api_key_file is not None:
                with open(self.configuration.client_configuration.api_key_file, "r", encoding="utf-8") as api_key_file:
                    for api_key in api_key_file:
                        self.api_keys.append(api_key.strip())

    def initialise(self):
        self.load_api_keys()

    @abstractmethod
    def get_api_key(self, rest_request):
        raise NotImplementedError()

    @abstractmethod
    def get_question(self, rest_request):
        raise NotImplementedError()

    @abstractmethod
    def get_userid(self, rest_request):
        raise NotImplementedError()

    @abstractmethod
    def create_response(self, response, status):
        raise NotImplementedError()

    def is_apikey_valid(self, apikey):
        return bool(apikey in self.api_keys)

    def verify_api_key_usage(self, request):
        if self.configuration.client_configuration.use_api_keys is True:

            apikey = self.get_api_key(request)

            if apikey is None:
                YLogger.error(self, "Unauthorised access - api required but missing")
                return {'error': 'Unauthorized access'}, 401

            if self.is_apikey_valid(apikey) is False:
                YLogger.error(self, "'Unauthorised access - invalid api key")
                return {'error': 'Unauthorized access'}, 401

        return None, None

    def format_success_response(self, userid, question, answer, options):
        return {"question": question, "answer": answer, "option": options[0], "userid": userid}

    def format_error_response(self, userid, question, error):
        client_context = self.create_client_context(userid)
        return {"question": question, "answer": client_context.bot.default_response, "userid": userid, "error": error}

    def ask_question(self, userid, question):
        response = ""
        try:
            client_context = self.create_client_context(userid)
            #TODO: add logic of the new changes here.
            #      Not sure what Rohola meant by above comment.
            print(question)
            response, options = client_context.bot.ask_question_with_options(client_context, question)
            # YLogger.debug(client_context, "response from ask_question_with_options (%s)", response)
            # YLogger.debug(client_context, "options from ask_question_with_options (%s)", options)
        except Exception as e:
            print(e)
        return response, options

    def process_request(self, request):
        question = "Unknown"
        userid = "Unknown"
        try:
            YLogger.debug(self, "In process_request")
            response, status = self.verify_api_key_usage(request)
            YLogger.debug(self, "verify_api_key_usage returned successfully")

            YLogger.debug(self, f"response: {response}")
            YLogger.debug(self, f"status: {status}")
            if response is not None:
                return response, status

            YLogger.debug(self, f"request: {request}")

            question = self.get_question(request)
            YLogger.debug(self, f"Got question: {question}")
            
            userid = self.get_userid(request)
            YLogger.debug(self, f"Got userid: {userid}")

            answer, options = self.ask_question(userid, question)
            YLogger.debug(self, f"Got answer: {answer}")

            return self.format_success_response(userid, question, answer, options), 200

        except Exception as excep:
            YLogger.error(self, excep)
            return self.format_error_response(userid, question, str(excep)), 500
