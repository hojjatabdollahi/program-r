from programy.utils.logging.ylogger import YLogger
from programy.config.base import BaseConfigurationData


class MajorDomoConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, name="majordomo")
        self._service_name = None
        self._is_running = False
        self._ip = None
        self._port = None


    @property
    def service_name(self):
        return self._service_name

    @property
    def is_running(self):
        return self._is_running

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port


    def load_config_section(self, configuration_file, bot_root):
        MajorDomo = configuration_file.get_section(self._section_name)
        if MajorDomo is not None:
            self._service_name = configuration_file.get_option(MajorDomo, "service_name", missing_value="echo")
            self._is_running = configuration_file.get_bool_option(MajorDomo, "is_running", missing_value=False)
            self._ip = configuration_file.get_option(MajorDomo, "ip", missing_value=None)
            self._port = configuration_file.get_int_option(MajorDomo, "port", missing_value=None)
        else:
            YLogger.warning(self, "'Broker' section missing from bot config, using defaults")

