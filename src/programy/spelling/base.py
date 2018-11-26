from abc import ABCMeta, abstractmethod

class SpellingChecker(object):
    __metaclass__ = ABCMeta

    def __init__(self, spelling_config=None):
        self.spelling_config = spelling_config

    @abstractmethod
    def correct(self, phrase):
        raise NotImplementedError()
