from programy.utils.logging.ylogger import YLogger

from programy.config.section import BaseSectionConfigurationData


class BrainOOBConfiguration(BaseSectionConfigurationData):

    def __init__(self, oob_name):
        BaseSectionConfigurationData.__init__(self, oob_name)
        self._classname = None

    @property
    def classname(self):
        return self._classname

    def load_config_section(self, configuration_file, configuration, bot_root):
        service = configuration_file.get_section(self.section_name, configuration)
        if service is not None:
            self._classname = configuration_file.get_option(service, "classname", missing_value=None)
        else:
            YLogger.warning(self, "'oob' section missing from brain config, using to defaults")

    def to_yaml(self, data, defaults=True):
        data['classname'] = self._classname
