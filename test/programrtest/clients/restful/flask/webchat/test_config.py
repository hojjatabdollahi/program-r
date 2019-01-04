import unittest

from programr.clients.restful.flask.webchat.config import WebChatConfiguration
from programr.config.file.yaml_file import YamlConfigurationFile
from programr.clients.events.console.config import ConsoleConfiguration

class WebChatConfigurationTests(unittest.TestCase):

    def test_init(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        webchat:
          host: 127.0.0.1
          port: 5000
          debug: false
          use_api_keys: false
          cookie_id: programrSession
          cookie_expires: 90
        """, ConsoleConfiguration(), ".")

        webchat_config = WebChatConfiguration()
        webchat_config.load_configuration(yaml, ".")

        self.assertEqual("127.0.0.1", webchat_config.host)
        self.assertEqual(5000, webchat_config.port)
        self.assertEqual(False, webchat_config.debug)
        self.assertEqual(False, webchat_config.use_api_keys)
        self.assertEqual("programrSession", webchat_config.cookie_id)
        self.assertEqual(90, webchat_config.cookie_expires)

    def test_to_yaml_with_defaults(self):
        config = WebChatConfiguration()

        data = {}
        config.to_yaml(data, True)

        self.assertEquals(data['cookie_id'], "programrSession")
        self.assertEquals(data['cookie_expires'], 90)

        self.assertEquals(data['bot'], 'bot')
        self.assertEquals(data['license_keys'], "./config/license.keys")
        self.assertEquals(data['bot_selector'], "programr.clients.client.DefaultBotSelector")
        self.assertEquals(data['renderer'], "programr.clients.render.text.TextRenderer")
