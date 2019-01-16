import unittest

from programr.security.authorise.passthrough import PassThroughAuthorisationService
from programr.config.brain.service import BrainServiceConfiguration

class PassThroughAuthorisationServiceTests(unittest.TestCase):

    def test_authorisor(self):
        service = PassThroughAuthorisationService(BrainServiceConfiguration("authorisation"))
        self.assertIsNotNone(service)
        self.assertTrue(service.authorise("console", "sysadmin"))
        self.assertTrue(service.authorise("anyone", "sysadmin"))