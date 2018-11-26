from programy.utils.logging.ylogger import YLogger
# Ignore pylint warning, this import from Programy must be before ElementTree
# Which ensures that the class LineNumberingParser is injected into the code
from programy.utils.parsing.linenumxml import LineNumberingParser
import xml.etree.ElementTree as ET

from programy.config.file.file import BaseConfigurationFile
from programy.config.programy import ProgramyConfiguration

class XMLConfigurationFile(BaseConfigurationFile):

    def __init__(self):
        BaseConfigurationFile.__init__(self)
        self.xml_data = None

    def load_from_text(self, text, client_configuration, bot_root):
        tree = ET.fromstring(text)
        self.xml_data = tree
        configuration = ProgramyConfiguration(client_configuration)
        configuration.load_config_data(self, bot_root)
        return configuration

    def load_from_file(self, filename, client_configuration, bot_root):
        configuration = ProgramyConfiguration(client_configuration)
        with open(filename, 'r+', encoding="utf-8") as xml_data_file:
            tree = ET.parse(xml_data_file, parser=LineNumberingParser())
            self.xml_data = tree.getroot()
            configuration.load_config_data(self, bot_root)
        return configuration

    def is_string(self, section):
        if section._children:
            return False
        return True

    def get_section(self, section_name, parent_section=None):
        if parent_section is None:
            return self.xml_data.find(section_name)
        return parent_section.find(section_name)

    def get_keys(self, section):
        keys = []
        for child in section:
            keys.append(child.tag)
        return keys

    def get_child_section_keys(self, child_section_name, parent_section):
        found = parent_section.find(child_section_name)
        if found is not None:
            keys = []
            for child in found:
                keys.append(child.tag)
            return keys
        return None

    def get_option(self, section, option_name, missing_value=None):
        child = section.find(option_name)
        if child is not None:
            if not child._children:
                return self._infer_type_from_string(child.text)
            return child
        else:
            if missing_value is not None:
                YLogger.warning(self, "Missing value for [%s] in config, return default value %s", option_name, missing_value)
            return missing_value

    def _infer_type_from_string(self, text):
        if text == 'True' or text == 'true':
            return True
        elif text == 'False' or text == 'false':
            return False
        return text

    def get_bool_option(self, section, option_name, missing_value=False):
        child = section.find(option_name)
        if child is not None:
            return self.convert_to_bool(child.text)
        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value %s", option_name, missing_value)
            return missing_value

    def get_int_option(self, section, option_name, missing_value=0):
        child = section.find(option_name)
        if child is not None:
            return self.convert_to_int(child.text)
        else:
            YLogger.warning(self, "Missing value for [%s] in config, return default value %d", option_name, missing_value)
            return missing_value

    def get_multi_option(self, section, option_name, missing_value=None):
        if missing_value is None:
            missing_value = []
        value = self.get_option(section, option_name, missing_value)
        if isinstance(value, list):
            if not value:
                return value
        if isinstance(value, str):
            values = [value]
        else:
            values = []
            for child in value._children:
                if child.tag == "bot":
                    values.append(child.text)
        multis = []
        for value in values:
            multis.append(value)
        return multis

    def get_multi_file_option(self, section, option_name, bot_root, missing_value=None):
        if missing_value is None:
            missing_value = []
        value = self.get_option(section, option_name, missing_value)
        if isinstance(value, list):
            if not value:
                return value
        if isinstance(value, str):
            values = [value]
        else:
            values = []
            for child in value._children:
                if child.tag == "dir":
                    values.append(child.text)
        multis = []
        for value in values:
            multis.append(value.replace('$BOT_ROOT', bot_root))
        return multis
