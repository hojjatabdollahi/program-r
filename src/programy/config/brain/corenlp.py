from programy.utils.logging.ylogger import YLogger
from programy.config.section import BaseSectionConfigurationData
from programy.config.brain.service import BrainServiceConfiguration
import os

class BrainCoreNLPConfiguration(BaseSectionConfigurationData):
    def __init__(self):
        BaseSectionConfigurationData.__init__(self, "nlp")
        self._classname = None
        self._ip = None
        self._port = None
        self._jar_dir = None

    @property
    def classname(self):
        return self._classname

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port

    @property
    def jar_dir(self):
        return self._jar_dir


    def load_config_section(self, configuration_file, configuration, bot_root):
        corenlp = configuration_file.get_section("corenlp", configuration)
        if corenlp is not None:
            self._classname = configuration_file.get_option(corenlp, "classname")
            self._ip = configuration_file.get_option(corenlp, "ip")
            self._port = configuration_file.get_option(corenlp, "port")
            self._jar_dir = configuration_file.get_option(corenlp, "jar_dir")
            if not os.path.isabs(self._jar_dir):
                programr_root = os.path.dirname(os.path.dirname(bot_root))
                self._jar_dir = os.path.join(programr_root, self._jar_dir)


        else:
            YLogger.warning(self, "Config section [services] missing from Brain, no services loaded")

    def to_yaml(self, data, defaults=True):
        data['classname'] = self._classname
        data['ip'] = self._ip
        data['port'] = self._port
        data['jar_dir'] = self._jar_dir
