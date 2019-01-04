import unittest

from programr.security.authorise.authorisor import Authoriser
from programr.config.brain.security import BrainSecurityConfiguration


class AuthorisorTests(unittest.TestCase):

    def test_authoriser(self):
        authoriser = Authoriser (BrainSecurityConfiguration("authorisation"))
        self.assertIsNotNone(authoriser)
        self.assertFalse(authoriser.authorise("console", "sysadmin"))