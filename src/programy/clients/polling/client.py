import time

from programy.utils.logging.ylogger import YLogger

from programy.clients.client import BotClient


class PollingBotClient(BotClient):

    def __init__(self, id, argument_parser=None):
        BotClient.__init__(self, id, argument_parser=argument_parser)

    def connect(self):
        return True

    def disconnect(self):
        return True

    def poll_and_answer(self):
        raise NotImplementedError("You must override this and implement the logic poll for messages and send answers back")

    def sleep(self, period):
        time.sleep(period)

    def run(self):
        try:
            if self.connect():
                self.display_connected_message()

                self._running = True
                while self._running:
                    self._running = self.poll_and_answer()

                YLogger.debug(self, "Exiting gracefully...")

            else:
                raise Exception("Connection failed....")

        except Exception as e:
            YLogger.exception(self, "Polling run error", e)

        finally:
            self.disconnect()
