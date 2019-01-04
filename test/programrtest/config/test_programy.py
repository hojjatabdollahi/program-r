import unittest

from programr.config.programr import ProgramrConfiguration
from programr.config.base import BaseConfigurationData


class TestConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, "test")

    def load_configuration(self, config_file, bot_root):
        return


class ProgramrConfigurationTests(unittest.TestCase):

    def test_programr(self):
        program_config = ProgramrConfiguration(TestConfiguration())
        self.assertIsNotNone(program_config)
        self.assertIsNotNone(program_config.client_configuration)




