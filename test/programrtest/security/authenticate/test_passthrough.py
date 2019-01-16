import unittest

from programr.security.authenticate.passthrough import BasicPassThroughAuthenticationService
from programr.config.brain.service import BrainServiceConfiguration
from programr.bot import Bot
from programr.brain import Brain
from programr.config.bot.bot import BotConfiguration
from programr.config.brain.brain import BrainConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class BasicPassThroughAuthenticationServiceTests(unittest.TestCase):

    def test_service(self):
        client_context = ClientContext(TestClient(), "unknown")
        client_context.bot = Bot(BotConfiguration())
        client_context.bot.configuration.conversations._max_histories = 3
        client_context.brain = client_context.bot.brain

        service = BasicPassThroughAuthenticationService(BrainServiceConfiguration("authentication"))
        self.assertIsNotNone(service)
        self.assertIsNotNone(service.configuration)
        client_context._userid = "console"
        self.assertTrue(service.authenticate(client_context))
        client_context._userid = "anyone"
        self.assertTrue(service.authenticate(client_context))
