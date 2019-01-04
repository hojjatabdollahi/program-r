import unittest
from programr.processors.pre.demojize import DemojizePreProcessor
from programr.bot import Bot
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class DemoizeTests(unittest.TestCase):

    def setUp(self):
        self.bot = Bot(config=BotConfiguration())

    def test_demojize(self):
        processor = DemojizePreProcessor()

        context = ClientContext(TestClient(), "testid")

        self.assertEqual("Python is :thumbs_up:", processor.process(context, 'Python is 👍'))
