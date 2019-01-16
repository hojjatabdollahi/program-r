import unittest

from programr.processors.post.multispaces import RemoveMultiSpacePostProcessor
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient

class RemoveMultiSpaceTests(unittest.TestCase):

    def test_remove_multi_spaces(self):
        processor = RemoveMultiSpacePostProcessor()

        context = ClientContext(TestClient(), "testid")
        
        result = processor.process(context, "Hello World")
        self.assertIsNotNone(result)
        self.assertEqual("Hello World", result)

        result = processor.process(context, "Hello World ")
        self.assertIsNotNone(result)
        self.assertEqual("Hello World", result)

        result = processor.process(context, " Hello World")
        self.assertIsNotNone(result)
        self.assertEqual("Hello World", result)

        result = processor.process(context, " Hello  World ")
        self.assertIsNotNone(result)
        self.assertEqual("Hello World", result)
