from programr.config.client.config import ClientConfigurationData


class RestConfiguration(ClientConfigurationData):

    def __init__(self, name):
        ClientConfigurationData.__init__(self, name)
        self._host = "0.0.0.0"
        self._port = 80
        self._debug = False
        self._use_api_keys = False
        self._api_key_file = None
        self._ssl_cert_file = None
        self._ssl_key_file = None

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def debug(self):
        return self._debug

    @property
    def use_api_keys(self):
        return self._use_api_keys

    @property
    def api_key_file(self):
        return self._api_key_file

    @property
    def ssl_cert_file(self):
        return self._ssl_cert_file

    @property
    def ssl_key_file(self):
        return self._ssl_key_file

    def load_configuration(self, configuration_file, bot_root):
        rest = configuration_file.get_section(self.section_name)
        if rest is not None:
            self._host = configuration_file.get_option(rest, "host", missing_value="0.0.0.0")
            self._port = configuration_file.get_option(rest, "port", missing_value=80)
            self._debug = configuration_file.get_bool_option(rest, "debug", missing_value=False)
            self._use_api_keys = configuration_file.get_bool_option(rest, "use_api_keys", missing_value=False)
            self._api_key_file = configuration_file.get_option(rest, "api_key_file")
            if self._api_key_file is not None:
                self._api_key_file = self.sub_bot_root(self._api_key_file, bot_root)
            self._ssl_cert_file = configuration_file.get_option(rest, "ssl_cert_file")
            if self._ssl_cert_file is not None:
                self._ssl_cert_file = self.sub_bot_root(self._ssl_cert_file, bot_root)
            self._ssl_key_file = configuration_file.get_option(rest, "ssl_key_file")
            if self._ssl_key_file is not None:
                self._ssl_key_file = self.sub_bot_root(self._ssl_key_file, bot_root)
        super(RestConfiguration, self).load_configuration(configuration_file, rest, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['host'] = "0.0.0.0"
            data['port'] = 80
            data['debug'] = False
            data['use_api_keys'] = False
            data['api_key_file'] = './api.keys'
            data['ssl_cert_file'] = './rsa.cert'
            data['ssl_key_file'] = './rsa.keys'
        else:
            data['host'] = self._host
            data['port'] = self._port
            data['debug'] = self._debug
            data['use_api_keys'] = self._use_api_keys
            data['api_key_file'] = self._api_key_file
            data['ssl_cert_file'] = self._ssl_cert_file
            data['ssl_key_file'] = self._ssl_key_file

        super(RestConfiguration, self).to_yaml(data, defaults)