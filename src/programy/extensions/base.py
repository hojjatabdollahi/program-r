from abc import ABCMeta, abstractmethod

class Extension(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self,context, data):
        raise NotImplementedError()

    @staticmethod
    def split_into_commands(data):
        return [x.upper() for x in data.split()]