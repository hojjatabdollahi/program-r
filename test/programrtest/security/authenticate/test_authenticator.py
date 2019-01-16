import unittest

from programr.security.authenticate.authenticator import Authenticator
from programr.config.brain.security import BrainSecurityConfiguration
from programr.bot import Bot
from programr.brain import Brain
from programr.config.bot.bot import BotConfiguration
from programr.config.brain.brain import BrainConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient

class AuthenticatorTests(unittest.TestCase):

    def test_authenticator_with_empty_config(self):
        client_context = ClientContext(TestClient(), "console")
        client_context.bot = Bot(BotConfiguration())
        client_context.bot.configuration.conversations._max_histories = 3
        client_context.brain = client_context.bot.brain

        service = Authenticator(BrainSecurityConfiguration("authentication"))
        self.assertIsNotNone(service)
        self.assertIsNotNone(service.configuration)
        self.assertIsNone(service.get_default_denied_srai())
        self.assertFalse(service.authenticate(client_context))
