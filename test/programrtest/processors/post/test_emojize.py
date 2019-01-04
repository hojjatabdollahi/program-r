import unittest
from programr.processors.post.emojize import EmojizePreProcessor
from programr.bot import Bot
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class EmojizeTests(unittest.TestCase):

    def setUp(self):
        self.bot = Bot(config=BotConfiguration())

    def test_demojize(self):
        processor = EmojizePreProcessor()
        
        context = ClientContext(TestClient(), "TestUser")
        
        self.assertEqual("Python is 👍", processor.process(context, 'Python is :thumbs_up:'))
        self.assertEqual("Python is 👍", processor.process(context, 'Python is :thumbsup:'))
