from abc import ABCMeta, abstractmethod


class BaseConfigurationFile(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def load_from_text(self, text, client_configuration, bot_root):
        """
        Never Implemented
        """
        raise NotImplementedError()

    @abstractmethod
    def load_from_file(self, filename, client_configuration, bot_root):
        """
        Never Implemented
        """
        raise NotImplementedError()

    @abstractmethod
    def get_section(self, section_name, parent_section=None):
        """
        Never Implemented
        """
        raise NotImplementedError()

    @abstractmethod
    def get_keys(self, section):
        """
        Never Implemented
        """
        raise NotImplementedError()

    @abstractmethod
    def get_child_section_keys(self, child_section_name, parent_section):
        """
        Never Implemented
        """
        raise NotImplementedError()

    @abstractmethod
    def get_option(self, section, option_name, missing_value=None):
        """
        Never Implemented
        """
        raise NotImplementedError()

    @abstractmethod
    def get_multi_file_option(self, section, option_name, bot_root, missing_value=None):
        """
        Never Implemented
        """
        raise NotImplementedError()

    def is_string(self, section):
        return bool(isinstance(section, str))

    def convert_to_bool(self, value):
        if value.upper() == 'TRUE':
            return True
        elif value.upper() == 'FALSE':
            return False
        else:
            raise Exception("Invalid boolean config value [%s]"%value)

    def convert_to_int(self, value):
        if value.isdigit():
            return int(value)
        else:
            raise Exception("Invalid integer config value [%s]"%value)
