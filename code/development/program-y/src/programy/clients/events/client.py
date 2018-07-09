"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from programy.utils.logging.ylogger import YLogger

from programy.clients.client import BotClient

class EventBotClient(BotClient):

    def __init__(self, id, argument_parser=None):
        self._running = False
        self._first_time = True
        self._session_saving_mode = False
        BotClient.__init__(self, id, argument_parser=argument_parser)

    def prior_to_run_loop(self):
        pass

    def run_loop(self):
        #client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
        self._running = True
        conversation_file = "/home/rohola/conv_questions.p"
        while self._running:
            if self._first_time:
                try:
                    if self._session_saving_mode:
                        client_context = self.load_client_context(self._configuration.client_configuration.default_userid, conversation_file)
                    else:
                        client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
                except Exception as exp:
                    client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
                finally:
                    self._first_time = False

            self._running = self.wait_and_answer(client_context)

    def wait_and_answer(self, client_context):
        raise NotImplementedError("You must override this and implement the logic wait for a question and send an answer back")

    def post_run_loop(self):
        pass

    def run(self):

        if self.arguments.noloop is False:
            YLogger.info(self, "Entering conversation loop...")

            self.prior_to_run_loop()

            self.run_loop()

            self.post_run_loop()

        else:
            YLogger.debug(self, "noloop set to True, exiting...")
