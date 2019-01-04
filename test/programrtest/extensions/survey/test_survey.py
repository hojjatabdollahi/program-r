import unittest

from programr.extensions.survey.survey import SurveyExtension
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient

class SurveyExtensionTests(unittest.TestCase):

    def setUp(self):
        client = TestClient()
        self.context = client.create_client_context("testid")

    def test_survey(self):

        minutes = SurveyExtension()
        self.assertIsNotNone(minutes)

        result = minutes.execute(self.context, "Answer1| Answer2")
        self.assertIsNotNone(result)
        self.assertEqual("OK", result)