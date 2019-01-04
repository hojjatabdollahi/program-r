import unittest

from programr.services.programr import ProgramrRESTService
from programr.config.brain.service import BrainServiceConfiguration

from programrtest.aiml_tests.client import TestClient


class ProgramrRESTServiceTests(unittest.TestCase):

    def test_format_payload(self):
        client = TestClient()
        client_context = client.create_client_context("testid")

        config = BrainServiceConfiguration("rest")
        config._classname = "programr.testclass"
        config._method = "GET"
        config._host = "localhost"
        config._port = 8080
        config._url = "/api/v1.0/ask"

        service = ProgramrRESTService(config, api=None)
        self.assertEquals({'question': 'Hello', 'userid': 'testid'}, service._format_payload(client_context, "Hello"))

    def test_format_get_url(self):
        client = TestClient()
        client_context = client.create_client_context("testid")

        config = BrainServiceConfiguration("rest")
        config._classname = "programr.testclass"
        config._method = "GET"
        config._host = "localhost"
        config._port = 8080
        config._url = "/api/v1.0/ask"

        service = ProgramrRESTService(config, api=None)
        self.assertEquals("/api/v1.0/ask?question=Hello&userid=testid", service._format_get_url("/api/v1.0/ask", client_context, "Hello"))

    def test_parse_response(self):
        client = TestClient()
        client_context = client.create_client_context("testid")

        config = BrainServiceConfiguration("rest")
        config._classname = "programr.testclass"
        config._method = "GET"
        config._host = "localhost"
        config._port = 8080
        config._url = "/api/v1.0/ask"

        service = ProgramrRESTService(config, api=None)
        self.assertEquals("Hello", service._parse_response('[{"response": {"answer": "Hello"}}]'))