from abc import ABCMeta, abstractmethod

from programr.config.base import BaseConfigurationData


class BaseContainerConfigurationData(BaseConfigurationData):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        BaseConfigurationData.__init__(self, name)

    @abstractmethod
    def load_configuration(self, configuration_file, bot_root):
        """
        Never Implemented
        """
        raise NotImplementedError()


