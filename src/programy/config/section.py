from abc import ABCMeta, abstractmethod

from programy.config.base import BaseConfigurationData


class BaseSectionConfigurationData(BaseConfigurationData):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        BaseConfigurationData.__init__(self, name)

    @abstractmethod
    def load_config_section(self, configuration_file, configuration, bot_root):
        """
        Never Implemented
        """
        raise NotImplementedError()
