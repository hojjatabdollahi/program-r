import unittest
from programr.processors.pre.toupper import ToUpperPreProcessor
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class ToUpperTests(unittest.TestCase):

    def test_to_upper(self):
        processor = ToUpperPreProcessor()

        context = ClientContext(TestClient(), "testid")

        result = processor.process(context, "Hello")
        self.assertIsNotNone(result)
        self.assertEqual("HELLO", result)
