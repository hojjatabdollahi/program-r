from programy.config.brain.sentence_segmentation import BrainSentenceSegmentationConfiguration
from programy.config.brain.tokenizer import BrainTokenizerConfiguration
from programy.utils.logging.ylogger import YLogger

from programy.config.section import BaseSectionConfigurationData
from programy.config.brain.corenlp import BrainCoreNLPConfiguration


class BrainNLPConfiguration(BaseSectionConfigurationData):
    def __init__(self):
        BaseSectionConfigurationData.__init__(self, "nlp")
        self._module_name = None
        self._corenlp = BrainCoreNLPConfiguration()
        self._toknizer = BrainTokenizerConfiguration()
        self._sentence_segmentation = BrainSentenceSegmentationConfiguration()


    @property
    def module_name(self):
        return self._module_name

    @property
    def corenlp(self):
        return self._corenlp

    @property
    def tokenizer(self):
        return self._toknizer

    @property
    def sentence_segmentation(self):
        return self._sentence_segmentation


    def load_config_section(self, configuration_file, configuration, bot_root):
        nlp = configuration_file.get_section("nlp", configuration)
        if nlp is not None:
            self._module_name = configuration_file.get_option(nlp, "modulename")
            corenlp = self._corenlp.load_config_section(configuration_file, nlp, bot_root)
            tokenizer = self._toknizer.load_config_section(configuration_file, nlp, bot_root)
            sentence_segmentation = self._sentence_segmentation.load_config_section(configuration_file, nlp, bot_root)

        else:
            YLogger.warning(self, "Config section [services] missing from Brain, no nlp loaded")

    # def to_yaml(self, data, defaults=True):
    #     if defaults is True:
    #         data['REST'] = {}
    #         data['REST']['classname'] = 'programy.services.rest.GenericRESTService'
    #         data['REST']['method'] = 'GET'
    #         data['REST']['host'] = '0.0.0.0'
    #
    #         data['Pannous'] = {}
    #         data['Pannous']['classname'] = 'programy.services.pannous.PannousService'
    #         data['Pannous']['url'] = 'http://weannie.pannous.com/api'
    #
    #         data['Pandora'] = {}
    #         data['Pandora']['classname'] = 'programy.services.pandora.PandoraService'
    #         data['Pandora']['url'] = 'http://www.pandorabots.com/pandora/talk-xml'
    #
    #         data['Wikipedia'] = {}
    #         data['Wikipedia']['classname'] = 'programy.services.wikipediaservice.WikipediaService'
    #
    #         data['DuckDuckGo'] = {}
    #         data['DuckDuckGo']['classname'] = 'programy.services.duckduckgo.DuckDuckGoService'
    #         data['DuckDuckGo']['url'] = 'http://api.duckduckgo.com'
