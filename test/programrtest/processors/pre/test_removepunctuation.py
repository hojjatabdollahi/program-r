import unittest
from programr.processors.pre.removepunctuation import RemovePunctuationPreProcessor
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class RemovePunctuationTests(unittest.TestCase):

    def test_remove_punctuation(self):
        processor = RemovePunctuationPreProcessor()

        context = ClientContext(TestClient(), "testid")

        result = processor.process(context, "Hello!")
        self.assertIsNotNone(result)
        self.assertEqual("Hello", result)

        result = processor.process(context, "$100")
        self.assertIsNotNone(result)
        self.assertEqual("$100", result)
