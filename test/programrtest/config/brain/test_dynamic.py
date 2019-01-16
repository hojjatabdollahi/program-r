import unittest

from programr.config.file.yaml_file import YamlConfigurationFile
from programr.config.brain.dynamic import BrainDynamicsConfiguration
from programr.clients.events.console.config import ConsoleConfiguration

class BrainDynamicsConfigurationTests(unittest.TestCase):

    def test_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            dynamic:
                variables:
                    gettime: programr.dynamic.variables.datetime.GetTime
                sets:
                    number: programr.dynamic.sets.numeric.IsNumeric
                    roman:   programr.dynamic.sets.roman.IsRomanNumeral
                maps:
                    romantodec: programr.dynamic.maps.roman.MapRomanToDecimal
                    dectoroman: programr.dynamic.maps.roman.MapDecimalToRoman
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        dynamic_config = BrainDynamicsConfiguration()
        dynamic_config.load_config_section(yaml, brain_config, ".")


    def test_without_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            dynamic:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        dynamic_config = BrainDynamicsConfiguration()
        dynamic_config.load_config_section(yaml, brain_config, ".")


    def test_with_no_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        dynamic_config = BrainDynamicsConfiguration()
        dynamic_config.load_config_section(yaml, brain_config, ".")


