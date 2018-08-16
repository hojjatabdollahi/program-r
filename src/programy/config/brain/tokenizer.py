from programy.utils.logging.ylogger import YLogger

from programy.config.base import BaseConfigurationData


class BrainTokenizerConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, name="tokenizer")
        self._classname = None
        self._split_chars = " "

    @property
    def classname(self):
        return self._classname

    @property
    def split_chars(self):
        return self._split_chars

    def load_config_section(self, configuration_file, configuration, bot_root):
        tokenizer = configuration_file.get_section(self._section_name, configuration)
        if tokenizer is not None:
            self._classname = configuration_file.get_option(tokenizer, "classname", missing_value="programy.parser.tokenizer.Tokenizer")
            self._split_chars = configuration_file.get_option(tokenizer, "split_chars", missing_value=" ")
        else:
            YLogger.warning(self, "'tokenizer' section missing from bot config, using defaults")

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['classname'] = "programy.parser.tokenizer.Tokenizer"
            data['split_chars'] = ' '
        else:
            data['classname'] = self._classname
            data['split_chars'] = self._split_chars
