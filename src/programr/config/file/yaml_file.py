from programr.utils.logging.ylogger import YLogger
import yaml

from programr.config.file.file import BaseConfigurationFile
from programr.config.programr import ProgramrConfiguration

class YamlConfigurationFile(BaseConfigurationFile):

    def __init__(self):
        BaseConfigurationFile.__init__(self)
        self.yaml_data = None

    def load_from_text(self, text, client_configuration, bot_root):
        self.yaml_data = yaml.load(text)
        if self.yaml_data is None:
            raise Exception("Yaml data is missing")
        configuration = ProgramrConfiguration(client_configuration)
        configuration.load_config_data(self, bot_root)
        return configuration

    def load_from_file(self, filename, client_configuration, bot_root):
        configuration = ProgramrConfiguration(client_configuration)
        with open(filename, 'r+', encoding="utf-8") as yml_data_file:
            self.yaml_data = yaml.load(yml_data_file, Loader=yaml.FullLoader)
            configuration.load_config_data(self, bot_root)
        return configuration

    def get_section(self, section_name, parent_section=None):
        if parent_section is None:
            if section_name in self.yaml_data:
                return self.yaml_data[section_name]
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
            YLogger.warning(self, "Missing value for [%s] in config, return default value %s", option_name, missing_value)
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

    def get_float_option(self, section, option_name, missing_value=0.0):
        if option_name in section:
            return float(section[option_name])
        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value %d", option_name, missing_value)
            return missing_value

    def get_multi_option(self, section, option_name, missing_value=None):

        if missing_value is None:
            missing_value = []

        if option_name in section:
            values = section[option_name]
            splits = values.split('\n')
            multis = []
            for value in splits:
                if value is not None and value != '':
                    multis.append(value)
            return multis

        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value", option_name)
            return [missing_value]

    def get_multi_file_option(self, section, option_name, bot_root, missing_value=None):

        if missing_value is None:
            missing_value = []

        if option_name in section:
            values = section[option_name]
            splits = values.split('\n')
            multis = []
            for value in splits:
                if value is not None and value != '':
                    multis.append(value.replace('$BOT_ROOT', bot_root))
            return multis

        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value", option_name)
            return missing_value
