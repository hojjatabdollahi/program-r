
from programy.utils.logging.ylogger import YLogger

from programy.config.base import BaseConfigurationData

class BotConversationsFileStorageConfiguration(BaseConfigurationData):

    def __init__(self, config_name):
        BaseConfigurationData.__init__(self, name=config_name)
        self._dir = None

    @property
    def dir(self):
        return self._dir

    def load_config_section(self, configuration_file, configuration, bot_root):
        ConversationsFileStorage = configuration_file.get_section(self._section_name, configuration)
        if ConversationsFileStorage is not None:
            dir = configuration_file.get_option(ConversationsFileStorage, "dir", missing_value=None)
            if dir is not None:
                self._dir = self.sub_bot_root(dir, bot_root)
        else:
            YLogger.warning(self, "'BotConversationsFileStorageConfiguration' section missing from bot config, using defaults")

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['dir'] = './conversations'
        else:
            data['dir'] = self._dir