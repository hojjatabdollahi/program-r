from programr.config.bot.session import BotSessionConfiguration
from programr.utils.logging.ylogger import YLogger

from programr.config.brain.brain import BrainConfiguration
from programr.config.bot.spelling import BotSpellingConfiguration
from programr.config.bot.conversations import BotConversationsConfiguration
from programr.config.container import BaseContainerConfigurationData


class BotConfiguration(BaseContainerConfigurationData):

    DEFAULT_ROOT = "."
    DEFAULT_RESPONSE = ""
    DEFAULT_RESPONSE_SRAI = ""
    DEFAULT_EMPTY_STRING = ""
    DEFAULT_EXIT_RESPONSE = "Bye!"
    DEFAULT_EXIT_RESPONSE_SRAI = ""
    DEFAULT_INITIAL_QUESTION = "Hello"
    DEFAULT_INITIAL_QUESTION_SRAI = ""
    DEFAULT_OVERRIDE_PREDICATES = True
    DEFAULT_MAX_QUESTION_RECURSION = 100
    DEFAULT_MAX_QUESTION_TIMEOUT = -1
    DEFAULT_MAX_SEARCH_DEPTH = 100
    DEFAULT_MAX_SEARCH_TIMEOUT = -1
    DEFAULT_TAB_PARSE_OUTPUT = True
    DEFAULT_REPHRASE_FILE = None
    DEFAULT_EMOTIVE = True

    def __init__(self, section_name="bot"):

        self._brain_configs = []
        self._brain_configs.append(BrainConfiguration("brain"))
        self._brain_selector = None

        self._bot_root = BotConfiguration.DEFAULT_ROOT
        self._default_response = BotConfiguration.DEFAULT_RESPONSE
        self._default_response_srai = BotConfiguration.DEFAULT_RESPONSE_SRAI
        self._exit_response = BotConfiguration.DEFAULT_EXIT_RESPONSE
        self._exit_response_srai = BotConfiguration.DEFAULT_EXIT_RESPONSE_SRAI
        self._initial_question = BotConfiguration.DEFAULT_INITIAL_QUESTION
        self._initial_question_srai = BotConfiguration.DEFAULT_INITIAL_QUESTION_SRAI
        self._empty_string = BotConfiguration.DEFAULT_EMPTY_STRING
        self._override_properties = BotConfiguration.DEFAULT_OVERRIDE_PREDICATES
        self._max_question_recursion = BotConfiguration.DEFAULT_MAX_QUESTION_RECURSION
        self._max_question_timeout = BotConfiguration.DEFAULT_MAX_QUESTION_TIMEOUT
        self._max_search_depth = BotConfiguration.DEFAULT_MAX_SEARCH_DEPTH
        self._max_search_timeout = BotConfiguration.DEFAULT_MAX_SEARCH_TIMEOUT
        self._tab_parse_output = BotConfiguration.DEFAULT_TAB_PARSE_OUTPUT
        self._rephrase_sentences_file = BotConfiguration.DEFAULT_REPHRASE_FILE
        self._emotive = BotConfiguration.DEFAULT_EMOTIVE
        self._spelling = BotSpellingConfiguration()
        self._conversations = BotConversationsConfiguration()
        self._session = BotSessionConfiguration()

        BaseContainerConfigurationData.__init__(self, section_name)

    def load_configuration(self, configuration_file, bot_root):
        bot = configuration_file.get_section(self.section_name)
        if bot is not None:

            self._default_response = configuration_file.get_option(bot, "default_response",
                                                                   BotConfiguration.DEFAULT_RESPONSE)
            self._default_response_srai = configuration_file.get_option(bot, "default_response_srai",
                                                                        BotConfiguration.DEFAULT_RESPONSE_SRAI)
            self._empty_string = configuration_file.get_option(bot, "empty_string",
                                                               BotConfiguration.DEFAULT_EMPTY_STRING)
            self._exit_response = configuration_file.get_option(bot, "exit_response",
                                                                BotConfiguration.DEFAULT_EXIT_RESPONSE)
            self._exit_response_srai = configuration_file.get_option(bot, "exit_response_srai",
                                                                     BotConfiguration.DEFAULT_EXIT_RESPONSE_SRAI)
            self._initial_question = configuration_file.get_option(bot, "initial_question",
                                                                   BotConfiguration.DEFAULT_INITIAL_QUESTION)
            self._initial_question_srai = configuration_file.get_option(bot, "initial_question_srai",
                                                                        BotConfiguration.DEFAULT_INITIAL_QUESTION_SRAI)
            self._override_properties = configuration_file.get_option(bot, "override_properties",
                                                                      BotConfiguration.DEFAULT_OVERRIDE_PREDICATES)
            self._max_question_recursion = configuration_file.get_int_option(bot, "max_question_recursion",
                                                                             BotConfiguration.DEFAULT_MAX_QUESTION_RECURSION)
            self._max_question_timeout = configuration_file.get_int_option(bot, "max_question_timeout",
                                                                           BotConfiguration.DEFAULT_MAX_QUESTION_TIMEOUT)
            self._max_search_depth = configuration_file.get_int_option(bot, "max_search_depth",
                                                                       BotConfiguration.DEFAULT_MAX_SEARCH_DEPTH)
            self._max_search_timeout = configuration_file.get_int_option(bot, "max_search_timeout",
                                                                         BotConfiguration.DEFAULT_MAX_SEARCH_TIMEOUT)
            self._tab_parse_output = configuration_file.get_bool_option(bot, "tab_parse_output",
                                                                        BotConfiguration.DEFAULT_TAB_PARSE_OUTPUT)
            self._rephrase_sentences_file = configuration_file.get_option(bot, "rephrase_sentences_file",
                                                                          BotConfiguration.DEFAULT_REPHRASE_FILE)
            self._emotive = configuration_file.get_bool_option(bot, "emotive", BotConfiguration.DEFAULT_EMOTIVE)

            self._spelling.load_config_section(configuration_file, bot, bot_root)
            self._conversations.load_config_section(configuration_file, bot, bot_root)
            self._session.load_config_section(configuration_file, bot, bot_root)
        else:
            YLogger.warning(self, "Config section [%s] missing, using default values", self.section_name)

        self.load_configurations(configuration_file, bot, bot_root)

    def load_configurations(self, configuration_file, bot, bot_root):
        if bot is not None:
            brain_names = configuration_file.get_multi_option(bot, "brain", missing_value="brain")
            first = True
            for name in brain_names:
                if first is True:
                    config = self._brain_configs[0]
                    first = False
                else:
                    config = BrainConfiguration(name)
                    self._brain_configs.append(config)
                config.load_configuration(configuration_file, bot_root)

                self._brain_selector = configuration_file.get_option(bot, "brain_selector")

        else:
            YLogger.warning(self, "No brain name defined for bot [%s], defaulting to 'brain'.", self.section_name)
            brain_name = "brain"
            self._brain_configs[0]._section_name = brain_name
            self._brain_configs[0].load_configuration(configuration_file, bot_root)

    @property
    def configurations(self):
        return self._brain_configs

    @property
    def brain_selector(self):
        return self._brain_selector

    @property
    def bot_root(self):
        return self._bot_root

    @property
    def default_response(self):
        return self._default_response

    @default_response.setter
    def default_response(self, text):
        self._default_response = text

    @property
    def default_response_srai(self):
        return self._default_response_srai

    @default_response_srai.setter
    def default_response_srai(self, text):
        self._default_response_srai = text

    @property
    def empty_string(self):
        return self._empty_string

    @empty_string.setter
    def empty_string(self, text):
        self._empty_string = text

    @property
    def exit_response(self):
        return self._exit_response

    @exit_response.setter
    def exit_response(self, text):
        self._exit_response = text

    @property
    def exit_response_srai(self):
        return self._exit_response_srai

    @exit_response_srai.setter
    def exit_response_srai(self, text):
        self._exit_response_srai = text

    @property
    def initial_question(self):
        return self._initial_question

    @initial_question.setter
    def initial_question(self, text):
        self._initial_question = text

    @property
    def initial_question_srai(self):
        return self._initial_question_srai

    @initial_question_srai.setter
    def initial_question_srai(self, text):
        self._initial_question_srai = text

    @property
    def override_properties(self):
        return self._override_properties

    @override_properties.setter
    def override_properties(self, override):
        self._override_properties = override

    @property
    def max_question_recursion(self):
        return self._max_question_recursion

    @property
    def max_question_timeout(self):
        return self._max_question_timeout

    @property
    def max_search_depth(self):
        return self._max_search_depth

    @property
    def max_search_timeout(self):
        return self._max_search_timeout

    @property
    def tab_parse_output(self):
        return self._tab_parse_output

    @property
    def rephrase_clauses_file(self):
        return self._rephrase_sentences_file

    @property
    def emotive(self):
        return self._emotive

    @property
    def spelling(self):
        return self._spelling

    @property
    def conversations(self):
        return self._conversations

    @property
    def session(self):
        return self._session

    def to_yaml(self, data, defaults=True):

        data['bot_root'] = self.bot_root
        data['default_response'] = self.default_response
        data['default_response_srai'] = self.default_response_srai
        data['exit_response'] = self.exit_response
        data['exit_response_srai'] = self.exit_response_srai
        data['initial_question'] = self.initial_question
        data['initial_question_srai'] = self.initial_question_srai
        data['empty_string'] = self.empty_string
        data['override_properties'] = self.override_properties
        data['max_question_recursion'] = self.max_question_recursion
        data['max_question_timeout'] = self.max_question_timeout
        data['max_search_depth'] = self.max_search_depth
        data['max_search_timeout'] = self.max_search_timeout
        data['tab_parse_output'] = self.tab_parse_output
        data['rephrase_clauses_file'] = self.rephrase_clauses_file
        data['emotive'] = self.emotive
        self.config_to_yaml(data, BotSpellingConfiguration(), defaults)
        self.config_to_yaml(data, BotConversationsConfiguration(), defaults)
