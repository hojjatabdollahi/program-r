import json

from programr.utils.logging.ylogger import YLogger
from programr.config.file.file import BaseConfigurationFile
from programr.config.programr import ProgramrConfiguration


class JSONConfigurationFile(BaseConfigurationFile):

    def __init__(self):
        BaseConfigurationFile.__init__(self)
        self.json_data = None

    def load_from_text(self, text, client_configuration, bot_root):
        self.json_data = json.loads(text)
        configuration = ProgramrConfiguration(client_configuration)
        configuration.load_config_data(self, bot_root)
        return configuration

    def load_from_file(self, filename, client_configuration, bot_root):
        configuration = ProgramrConfiguration(client_configuration)
        with open(filename, 'r+', encoding="utf-8") as json_data_file:
            self.json_data = json.load(json_data_file)
            configuration.load_config_data(self, bot_root)
        return configuration

    def get_section(self, section_name, parent_section=None):
        if parent_section is None:
            if section_name in self.json_data:
                return self.json_data[section_name]
        else:
            if section_name in parent_section:
                return parent_section[section_name]
        return None

    def get_keys(self, section):
        return section.keys()

    def get_child_section_keys(self, child_section_name, parent_section):
        if child_section_name in parent_section:
            return parent_section[child_section_name].keys()
        return None

    def get_option(self, section, option_name, missing_value=None):
        if option_name in section:
            return section[option_name]
        else:
            YLogger.warning(self, "Missing value for [%s] in config , return default value %s", option_name, missing_value)
            return missing_value

    def get_bool_option(self, section, option_name, missing_value=False):
        if option_name in section:
            return section[option_name]
        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value %s", option_name, missing_value)
            return missing_value

    def get_int_option(self, section, option_name, missing_value=0):
        if option_name in section:
            return section[option_name]
        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value %d", option_name, missing_value)
            return missing_value

    def get_multi_option(self, section, option_name, missing_value=None):
        if missing_value is None:
            missing_value = []
        value = self. get_option(section, option_name, missing_value)
        if isinstance(value, list):
            values = value
        else:
            values = [value]
        multis = []
        for value in values:
            multis.append(value)
        return multis

    def get_multi_file_option(self, section, option_name, bot_root, missing_value=None):
        if missing_value is None:
            missing_value = []
        value = self. get_option(section, option_name, missing_value)
        if isinstance(value, list):
            values = value
        else:
            values = [value]
        multis = []
        for value in values:
            multis.append(value.replace('$BOT_ROOT', bot_root))
        return multis
