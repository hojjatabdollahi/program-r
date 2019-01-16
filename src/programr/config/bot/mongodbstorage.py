from programr.utils.logging.ylogger import YLogger
from programr.config.base import BaseConfigurationData

class BotConversationsMongodbStorageConfiguration(BaseConfigurationData):


    def __init__(self, config_name):
        BaseConfigurationData.__init__(self, name=config_name)
        self._host = "localhost"
        self._port = 27017
        self._password = None
        self._root = None
        self._name = None
        self._collection_name = None

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def root(self):
        return self._root

    @property
    def name(self):
        return self._name

    @property
    def collection_name(self):
        return self._collection_name


    def load_config_section(self, configuration_file, configuration, bot_root):
        conversations_mongodb_storage = configuration_file.get_section(self._section_name, configuration)
        if conversations_mongodb_storage is not None:
            self._host = configuration_file.get_option(conversations_mongodb_storage, "host", missing_value="localhost")
            self._port = configuration_file.get_int_option(conversations_mongodb_storage, "port", missing_value=27017)
            self._password = configuration_file.get_option(conversations_mongodb_storage, "password", missing_value=None)
            self._root = configuration_file.get_option(conversations_mongodb_storage, "root", missing_value=None)
            self._name = configuration_file.get_option(conversations_mongodb_storage, "name", missing_value=None)
            self._collection_name = configuration_file.get_option(conversations_mongodb_storage, "collection_name", missing_value=None)

        else:
            YLogger.warning(self, "'BotConversationsMongodbStorageConfiguration' section missing from bot config, using defaults")


    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['host'] = 'localhost'
            data['port'] = 27017
            data['password'] = 'password'
            data["root"] = "./"
        else:
            data['host'] = self._host
            data['port'] = self._port
            data['password'] = self._password
            data["root"] = self._root
            data["name"] = self._name
            data["collection_name"] = self._collection_name