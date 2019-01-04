from abc import ABCMeta, abstractmethod
from programr.utils.logging.ylogger import YLogger


class BaseConfigurationData(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self._section_name = name
        self._additionals = {}

    def exists(self, name):
        return bool(name in self._additionals)

    def value(self, key):
        if key in self._additionals:
            return self._additionals[key]
        else:
            YLogger.warning(self, "Configuration key [%s] does not exist", key)
            return None

    @property
    def section_name(self):
        return self._section_name

    @property
    def id(self):
        return self._section_name

    def _get_file_option(self, config_file, option_name, section, bot_root):
        option = config_file.get_option(section, option_name)
        if option is not None:
            option = self.sub_bot_root(option, bot_root)
        return option

    def sub_bot_root(self, text, root):
        return text.replace('$BOT_ROOT', root)

    def additionals_to_add(self):
        return []

    def load_additional_key_values(self, file_config, service):
        for key in file_config.get_keys(service):
            if key in self.additionals_to_add():
                value = file_config.get_option(service, key)
                self._additionals[key] = value

    def config_to_yaml(self, data, config, defaults=True):
        data[config.id] = {}
        config.to_yaml(data[config.id], defaults)

    def to_yaml(self, data, defaults=True):
        pass
