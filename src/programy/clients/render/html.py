from programy.utils.logging.ylogger import YLogger

import time
import urllib.parse

from programy.clients.render.text import TextRenderer


class HtmlRenderer(TextRenderer):

    def __init__(self, callback=None):
        TextRenderer.__init__(self, callback)

    def create_postback_url(self):
        return "#"

    def handle_text(self, client_context, text):
        str = "%s"%text['text']
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_url_button(self, client_context, button):
        str = '<a href="%s">%s</a>'%(button['url'], button['text'])
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_postback_button(self, client_context, button):
        str = '<a class="postback" postback="%s" href="#">%s</a>' % (button['postback'], button['text'])
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_link(self, client_context, link):
        str = '<a href="%s">%s</a>'%(link['url'], link['text'])
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_image(self, client_context, image):
        str = '<img src="%s" />'%image['url']
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_video(self, client_context, video):
        str = """<video src="%s">
Sorry, your browser doesn't support embedded videos, 
but don't worry, you can <a href="%s">download it</a>
and watch it with your favorite video player!
</video>"""%(video['url'], video['url'])
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def _format_card(self, card):
        str = '<div class="card" >'
        str += '<img src="%s" />' % card['image']
        str += '<h1>%s</h1>' % card['title']
        str += '<h2>%s</h2>' % card['subtitle']
        for button in card['buttons']:
            if button['url'] is not None:
                str += '<a href="%s">%s</a>' % (button['url'], button['text'])
            else:
                str += '<a class="postback" postback="%s" href="#">%s</a>' % (button['postback'], button['text'])
        str += '</div>'
        return str

    def handle_card(self, client_context, card):
        str = self._format_card(card)
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_carousel(self, client_context, carousel):
        str = '<div class="carousel">'
        for card in carousel['cards']:
            str += self._format_card(card)
        str += "</div>"
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_reply(self, client_context, reply):
        str = ''
        if reply['postback'] is not None:
            str += '<a class="postback" postback="%s" href="#">%s</a>' % (reply['postback'], reply['text'])
        else:
            str += '<a class="postback" postback="%s" href="#">%s</a>' % (reply['text'], reply['text'])
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_delay(self, client_context, delay):
        str = '<div class="delay">...</div>'
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_split(self, client_context, split):
        str = "<br />"
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_list(self, client_context, list):
        str = "<ul>"
        for item in list['items']:
            str += "<li>%s</li>"%item['text']
        str += "</ul>"
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_ordered_list(self, client_context, list):
        str = "<ol>"
        for item in list['items']:
            str += "<li>%s</li>" % item['text']
        str += "</ol>"
        if self._client:
            self._client.process_response(client_context, str)
        return str

    def handle_location(self, client_context, location):
        str = ""
        if self._client:
            self._client.process_response(client_context, str)
        return str