from programy.utils.logging.ylogger import YLogger
from programy.config.base import BaseConfigurationData

class BotConversationsRedisStorageConfiguration(BaseConfigurationData):

    def __init__(self, config_name):
        BaseConfigurationData.__init__(self, name=config_name)
        self._host = "localhost"
        self._port = 6379
        self._password = None
        self._prefix = None

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def password(self):
        return self._password

    @property
    def prefix(self):
        return self._prefix

    def load_config_section(self, configuration_file, configuration, bot_root):
        conversations_redis_storage = configuration_file.get_section(self._section_name, configuration)
        if conversations_redis_storage is not None:
            self._host = configuration_file.get_option(conversations_redis_storage, "host", missing_value="localhost")
            self._port = configuration_file.get_int_option(conversations_redis_storage, "port", missing_value=6379)
            self._password = configuration_file.get_option(conversations_redis_storage, "password", missing_value=None)
            self._prefix = configuration_file.get_option(conversations_redis_storage, "prefix",
                                                         missing_value="program_y:bot_cache")
        else:
            YLogger.warning(self, "'BotConversationsRedisStorageConfiguration' section missing from bot config, using defaults")

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['host'] = 'localhost'
            data['port'] = 6379
            data['password'] = 'password'
            data['prefix'] = 'programy'
        else:
            data['host'] = self._host
            data['port'] = self._port
            data['password'] = self._password
            data['prefix'] = self._prefix
