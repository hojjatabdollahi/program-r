import unittest

from programr.config.file.yaml_file import YamlConfigurationFile
from programr.config.brain.service import BrainServiceConfiguration
from programr.clients.events.console.config import ConsoleConfiguration

class BrainServiceConfigurationTests(unittest.TestCase):

    def test_rest_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            services:
                REST:
                    classname: programr.services.rest.GenericRESTService
                    method: GET
                    host: 0.0.0.0
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")
        self.assertIsNotNone(brain_config)
        services_config = yaml.get_section("services", brain_config)
        self.assertIsNotNone(services_config)

        service_config = BrainServiceConfiguration("REST")
        service_config.load_config_section(yaml, services_config, ".")

        self.assertEqual("programr.services.rest.GenericRESTService", service_config.classname)
        self.assertEqual("GET", service_config.method)
        self.assertEqual("0.0.0.0", service_config.host)
        self.assertIsNone(service_config.port)
        self.assertIsNone(service_config.url)

    def test_pannous_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            services:
                Pannous:
                    classname: programr.services.pannous.PannousService
                    url: http://weannie.pannous.com/api
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")
        self.assertIsNotNone(brain_config)
        services_config = yaml.get_section("services", brain_config)
        self.assertIsNotNone(services_config)

        service_config = BrainServiceConfiguration("Pannous")
        service_config.load_config_section(yaml, services_config, ".")

        self.assertEqual("programr.services.pannous.PannousService", service_config.classname)
        self.assertEqual("http://weannie.pannous.com/api", service_config.url)
        self.assertIsNone(service_config.method)
        self.assertIsNone(service_config.host)
        self.assertIsNone(service_config.port)

    def test_pandora_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            services:
                Pandora:
                    classname: programr.services.pandora.PandoraService
                    url: http://www.pandorabots.com/pandora/talk-xml
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")
        self.assertIsNotNone(brain_config)
        services_config = yaml.get_section("services", brain_config)
        self.assertIsNotNone(services_config)

        service_config = BrainServiceConfiguration("Pandora")
        service_config.load_config_section(yaml, services_config, ".")

        self.assertEqual("programr.services.pandora.PandoraService", service_config.classname)
        self.assertEqual("http://www.pandorabots.com/pandora/talk-xml", service_config.url)
        self.assertIsNone(service_config.method)
        self.assertIsNone(service_config.host)
        self.assertIsNone(service_config.port)

    def test_wikipedia_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            services:
                Wikipedia:
                    classname: programr.services.wikipediaservice.WikipediaService
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")
        self.assertIsNotNone(brain_config)
        services_config = yaml.get_section("services", brain_config)
        self.assertIsNotNone(services_config)

        service_config = BrainServiceConfiguration("Wikipedia")
        service_config.load_config_section(yaml, services_config, ".")

        self.assertEqual("programr.services.wikipediaservice.WikipediaService", service_config.classname)
        self.assertIsNone(service_config.method)
        self.assertIsNone(service_config.host)
        self.assertIsNone(service_config.port)
        self.assertIsNone(service_config.url)

    def test_rest_without_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            services:
                REST:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")
        self.assertIsNotNone(brain_config)
        services_config = yaml.get_section("services", brain_config)
        self.assertIsNotNone(services_config)

        service_config = BrainServiceConfiguration("REST")
        service_config.load_config_section(yaml, services_config, ".")

        self.assertIsNone(service_config.classname)
        self.assertIsNone(service_config.method)
        self.assertIsNone(service_config.host)
        self.assertIsNone(service_config.port)
        self.assertIsNone(service_config.url)


