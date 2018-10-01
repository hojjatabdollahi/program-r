from programy.utils.logging.ylogger import YLogger

from programy.config.container import BaseContainerConfigurationData
from programy.config.bot.bot import BotConfiguration
from programy.config.client.scheduler import SchedulerConfiguration

class ClientConfigurationData(BaseContainerConfigurationData):

    def __init__(self, name):
        BaseContainerConfigurationData.__init__(self, name)
        self._bot_configs = []
        self._bot_configs.append(BotConfiguration("bot"))
        self._license_keys = None
        self._bot_selector = None
        self._scheduler = SchedulerConfiguration()
        self._renderer = None

    @property
    def configurations(self):
        return self._bot_configs

    @property
    def license_keys(self):
        return self._license_keys

    @property
    def bot_selector(self):
        return self._bot_selector

    @property
    def scheduler(self):
        return self._scheduler

    @property
    def renderer(self):
        return self._renderer

    def load_configuration(self, configuration_file, section, bot_root):
        if section is not None:
            bot_names = configuration_file.get_multi_option(section, "bot", missing_value="bot")
            first = True
            for name in bot_names:
                if first is True:
                    config = self._bot_configs[0]
                    first = False
                else:
                    config = BotConfiguration(name)
                    self._bot_configs.append(config)
                config.load_configuration(configuration_file, bot_root)

            self._license_keys = configuration_file.get_option(section, "license_keys")
            if self._license_keys is not None:
                self._license_keys = self.sub_bot_root(self._license_keys, bot_root)

            self._bot_selector = configuration_file.get_option(section, "bot_selector")

            self._scheduler.load_config_section(configuration_file, section, bot_root)

            self._renderer = configuration_file.get_option(section, "renderer")

        else:
            YLogger.warning(self, "No bot name defined for client [%s], defaulting to 'bot'.", self.section_name)
            self._bot_configs[0]._section_name = "bot"
            self._bot_configs[0].load_configuration(configuration_file, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['bot'] = 'bot'
            data['license_keys'] = "./config/license.keys"
            data['bot_selector'] = "programy.clients.client.DefaultBotSelector"
            data[self._scheduler.id] = {}
            self._scheduler.to_yaml(data[self._scheduler.id], defaults)
            data['renderer'] = "programy.clients.render.text.TextRenderer"
        else:
            data['bot'] = self._bot_configs[0].id
            data['license_keys'] = self.license_keys
            data['bot_selector'] = self.bot_selector
            data[self._scheduler.id] = {}
            self._scheduler.to_yaml(data[self._scheduler.id], defaults)
            data['renderer'] = self.renderer
