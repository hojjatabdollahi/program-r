from abc import ABCMeta, abstractmethod

class ConversationStorage(object):

    def __init__(self, config):
        self._config = config

    @abstractmethod
    def empty(self):
        """
        Never Implemented
        """

    @abstractmethod
    def save_conversation(self, client_context):
        """
        Never Implemented
        """

    @abstractmethod
    def load_conversation(self, conversation, clientid, restore_last_topic=False):
        """
        Never Implemented
        """
