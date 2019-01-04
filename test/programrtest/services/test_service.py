import unittest

from programr.services.service import Service, ServiceFactory
from programr.config.brain.brain import BrainConfiguration
from programr.config.brain.service import BrainServiceConfiguration

class MockService(Service):

    def __init__(self, config):
        Service.__init__(self, config)

    def ask_question(self, context: str, question: str):
        return "asked"

class ServiceFactoryTests(unittest.TestCase):

    def test_load_services(self):

        service_config = BrainServiceConfiguration("mock")
        service_config._classname = 'programrtest.services.test_service.MockService'

        brain_config = BrainConfiguration()
        brain_config.services._services['mock'] = service_config

        ServiceFactory.preload_services(brain_config.services)

        self.assertIsNotNone(ServiceFactory.get_service("mock"))
        self.assertIsInstance(ServiceFactory.get_service("mock"), MockService)