from programy.clients.events.client import EventBotClient
from programy.clients.events.majordomo.config import MajorDomoConfiguration
from programy.utils.logging.ylogger import YLogger


class MajorDomoBotClient(EventBotClient):

    def __init__(self, argument_parser=None):
        self.running = False
        EventBotClient.__init__(self, "majordomo", argument_parser)

    def get_description(self):
        return 'ProgramY AIML2.0 MajorDomo Client'

    def get_client_configuration(self):
        return MajorDomoConfiguration()

    def add_client_arguments(self, parser=None):
        return

    def parse_args(self, arguments, parsed_args):
        return

    def get_question(self, client_context, input_func=input):
        ask = "%s " % self.get_client_configuration().prompt
        return input_func(ask)

    def display_startup_messages(self, client_context):
        self.process_response(client_context, client_context.bot.get_version_string(client_context))
        initial_question = client_context.bot.get_initial_question(client_context)
        self._renderer.render(client_context, initial_question)

    def process_question(self, client_context, question):
        # Returns a response
        return client_context.bot.ask_question(client_context, question, responselogger=self)

    def render_response(self, client_context, response):
        # Calls the renderer which handles RCS context, and then calls back to the client to show response
        self._renderer.render(client_context, response)

    def process_response(self, client_context, response):
        print(response)

    def process_question_answer(self, client_context):
        question = self.get_question(client_context)
        response = self.process_question(client_context, question)
        self.render_response(client_context, response)

    def wait_and_answer(self, client_context):
        running = True
        try:
            # client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
            self.process_question_answer(client_context)
        except KeyboardInterrupt as keye:
            running = False
            client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
            self._renderer.render(client_context, client_context.bot.get_exit_response(client_context))
        except Exception as excep:
            YLogger.exception(self, "Oops something bad happened !", excep)
        return running

    def prior_to_run_loop(self):
        userid = "MajorDomo"
        client_context = self.create_client_context(userid)
        self.display_startup_messages(client_context)


    def run(self):
        if self.arguments.noloop is False:
            YLogger.info(self, "Entering conversation loop...")

            self.prior_to_run_loop()

            self.worker_run_loop_new()

            self.post_run_loop()

        else:
            YLogger.debug(self, "noloop set to True, exiting...")




if __name__ == '__main__':
    def run():
        print("Loading, please wait...")
        majordomo_app = MajorDomoBotClient()
        majordomo_app.run()


    run()


