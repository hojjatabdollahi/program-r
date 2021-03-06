from programr.utils.logging.ylogger import YLogger

from programr.config.bot.filestorage import BotConversationsFileStorageConfiguration
from programr.config.bot.redisstorage import BotConversationsRedisStorageConfiguration
from programr.config.bot.mongodbstorage import BotConversationsMongodbStorageConfiguration
from programr.dialog.storage.file import ConversationFileStorage
from programr.dialog.storage.redis import ConversationRedisStorage
from programr.dialog.storage.mongodb import ConversationMongodbStorage

class ConversationStorageFactory(object):

    @staticmethod
    def get_storage_config(type, config_name, configuration_file, configuration, bot_root):
        if type == 'file':
            storage = BotConversationsFileStorageConfiguration(config_name=config_name)
            storage.load_config_section(configuration_file, configuration, bot_root)
            return storage
        elif type == 'redis':
            storage = BotConversationsRedisStorageConfiguration(config_name=config_name)
            storage.load_config_section(configuration_file, configuration, bot_root)
            return storage

        elif type == "mongodb":
            storage = BotConversationsMongodbStorageConfiguration(config_name=config_name)
            storage.load_config_section(configuration_file, configuration, bot_root)
            return storage

        YLogger.warning(None, "Invalid Conversations file storage type [%s]", type)
        return None

    @staticmethod
    def get_storage(config):
        if config.conversations.type == 'file':
            return ConversationFileStorage(config.conversations.storage)
        elif config.conversations.type == 'redis':
            return ConversationRedisStorage(config.conversations.storage)
        elif config.conversations.type == "mongodb":
            return ConversationMongodbStorage(config.conversations.storage)

        YLogger.warning(None, "Invalid Conversations file storage type [%s]", config.conversations.type)
        return None
