class ProgramyConfiguration(object):

    def __init__(self, client_configuration):
        self._client_config = client_configuration

    @property
    def client_configuration(self):
        return self._client_config

    def load_config_data(self, config_file, bot_root):
        self._client_config.load_configuration(config_file, bot_root)
