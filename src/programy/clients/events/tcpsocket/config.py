from programy.config.client.config import ClientConfigurationData


class SocketConfiguration(ClientConfigurationData):

    def __init__(self):
        ClientConfigurationData.__init__(self, "socket")
        self._host = "0.0.0.0"
        self._port = 80
        self._debug = False
        self._queue = 5
        self._max_buffer = 1024

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
    def queue(self):
        return self._queue

    @property
    def max_buffer(self):
        return self._max_buffer

    def load_configuration(self, configuration_file, bot_root):
        socket = configuration_file.get_section(self.section_name)
        if socket is not None:
            self._host = configuration_file.get_option(socket, "host", missing_value="0.0.0.0")
            self._port = configuration_file.get_option(socket, "port", missing_value=80)
            self._debug = configuration_file.get_bool_option(socket, "debug", missing_value=False)
            self._workers = configuration_file.get_option(socket, "queue", missing_value=5)
            self._max_buffer = configuration_file.get_option(socket, "max_buffer", missing_value=1024)
        super(SocketConfiguration, self).load_configuration(configuration_file, socket, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['host'] = "0.0.0.0"
            data['port'] = 80
            data['debug'] = False
            data['queue'] = 5
            data['max_buffer'] = 1024
        else:
            data['host'] = self._host
            data['port'] = self._port
            data['debug'] = self._debug
            data['queue'] = self._queue
            data['max_buffer'] = self._max_buffer

        super(SocketConfiguration, self).to_yaml(data, defaults)