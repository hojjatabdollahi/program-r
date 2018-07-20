from programy.config.client.config import ClientConfigurationData


class MajorDomoConfiguration(ClientConfigurationData):

    def __init__(self):
        ClientConfigurationData.__init__(self, "majordomo")
        self._service_name = "echo"
        self._ip = "0.0.0.0"
        self._port = 0
        self._verbose = False


    @property
    def service_name(self):
        return self._service_name

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port

    @property
    def verbose(self):
        return self._verbose


    def load_configuration(self, configuration_file, bot_root):
        majordomo = configuration_file.get_section(self.section_name)
        if majordomo is not None:
            self._service_name = configuration_file.get_option(majordomo, "service_name", missing_value="echo")
            self._ip = configuration_file.get_option(majordomo, "ip", missing_value="0.0.0.0")
            self._port = configuration_file.get_int_option(majordomo, "port", missing_value=0)
            self._verbose = configuration_file.get_bool_option(majordomo, "verbose", missing_value=False)
        super(MajorDomoConfiguration, self).load_configuration(configuration_file, majordomo, bot_root)

    # def to_yaml(self, data, defaults=True):
    #     if defaults is True:
    #         data['default_userid'] = "console"
    #         data['prompt'] = ">>>"
    #     else:
    #         data['default_userid'] = self._default_userid
    #         data['prompt'] = self._prompt
    #     super(MajorDomoConfiguration, self).to_yaml(data, defaults)