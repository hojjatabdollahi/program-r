import unittest
from programr.processors.post.denormalize import DenormalizePostProcessor
from programr.processors.post.formatpunctuation import FormatPunctuationProcessor
from programr.processors.post.formatnumbers import FormatNumbersPostProcessor
from programr.processors.post.multispaces import RemoveMultiSpacePostProcessor
from programr.processors.post.emojize import EmojizePreProcessor
from programr.bot import Bot
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class PostProcessingTests(unittest.TestCase):

    def post_process(self, output_str):
        context = ClientContext(TestClient(), "testid")
   
        context.bot = Bot(config=BotConfiguration())
        context.brain = context.bot.brain
        context.bot.brain.denormals.process_splits([" dot com ",".com"])
        context.bot.brain.denormals.process_splits([" atsign ","@"])
        denormalize = DenormalizePostProcessor()
        punctuation = FormatPunctuationProcessor()
        numbers = FormatNumbersPostProcessor()
        multispaces = RemoveMultiSpacePostProcessor()
        emojize = EmojizePreProcessor()

        output_str = denormalize.process(context, output_str)
        output_str = punctuation.process(context, output_str)
        output_str = numbers.process(context, output_str)
        output_str = multispaces.process(context, output_str)
        output_str = emojize.process(context, output_str)

        return output_str

    def test_post_cleanup(self):

        result = self.post_process("Hello World")
        self.assertIsNotNone(result)
        self.assertEqual("Hello World", result)

        result = self.post_process("Hello World . This is It! ")
        self.assertIsNotNone(result)
        self.assertEqual("Hello World. This is It!", result)

        result = self.post_process("Is the result 23 . 45 ?")
        self.assertIsNotNone(result)
        self.assertEqual("Is the result 23.45?", result)

        result = self.post_process("My email address is ybot atsign programr dot com")
        self.assertIsNotNone(result)
        self.assertEqual("My email address is ybot@programr.com", result)

        result = self.post_process("He said ' Hello World '.")
        self.assertIsNotNone(result)
        self.assertEqual("He said 'Hello World'.", result)

