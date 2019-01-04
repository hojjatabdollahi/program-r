import unittest

from programr.config.file.yaml_file import YamlConfigurationFile
from programr.config.brain.securities import BrainSecuritiesConfiguration
from programr.clients.events.console.config import ConsoleConfiguration

class BrainSecuritiesConfigurationTests(unittest.TestCase):

    def test_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            security:
                authentication:
                    classname: programr.security.authenticate.passthrough.PassThroughAuthenticationService
                    denied_srai: AUTHENTICATION_FAILED
                authorisation:
                    classname: programr.security.authorise.passthrough.PassThroughAuthorisationService
                    denied_srai: AUTHORISATION_FAILED
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        securities_config = BrainSecuritiesConfiguration()
        securities_config.load_config_section(yaml, brain_config, ".")

        self.assertIsNotNone(securities_config.authorisation)
        self.assertIsNotNone(securities_config.authentication)