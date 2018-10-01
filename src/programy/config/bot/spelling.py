from programy.utils.logging.ylogger import YLogger

from programy.config.base import BaseConfigurationData

class BotSpellingConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, name="spelling")
        self._classname = None
        self._corpus = None
        self._alphabet = None
        self._check_before = False
        self._check_and_retry = False

    @property
    def classname(self):
        return self._classname

    @property
    def corpus(self):
        return self._corpus

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def check_before(self):
        return self._check_before

    @property
    def check_and_retry(self):
        return self._check_and_retry

    def load_config_section(self, configuration_file, configuration, bot_root):
        spelling = configuration_file.get_section(self._section_name, configuration)
        if spelling is not None:
            self._classname = configuration_file.get_option(spelling, "classname", missing_value=None)
            self._alphabet = configuration_file.get_option(spelling, "alphabet", missing_value=None)
            corpus = configuration_file.get_option(spelling, "corpus", missing_value=None)
            self._corpus = self.sub_bot_root(corpus, bot_root)
            self._check_before = configuration_file.get_bool_option(spelling, "check_before", missing_value=False)
            self._check_and_retry = configuration_file.get_option(spelling, "check_and_retry", missing_value=False)
        else:
            YLogger.warning(self, "'spelling' section missing from bot config, using defaults")

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['classname'] = "programy.spelling.norvig.NorvigSpellingChecker"
            data['corpus'] = "./spelling/corpus.txt"
            data['alphabet'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            data['check_before'] = False
            data['check_and_retry'] = True
        else:
            data['classname'] = self._classname
            data['corpus'] = self._corpus
            data['alphabet'] = self._alphabet
            data['check_before'] = self._check_before
            data['check_and_retry'] = self._check_and_retry
