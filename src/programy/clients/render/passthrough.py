from programy.utils.logging.ylogger import YLogger

import time

from programy.clients.render.renderer import RichMediaRenderer


class PassThroughRenderer(RichMediaRenderer):

    def __init__(self, client):
        RichMediaRenderer.__init__(self, client)

    def render(self, client_context, message):
        if self._client:
            self._client.process_response(client_context, message)
        return message