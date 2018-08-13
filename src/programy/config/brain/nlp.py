from programy.utils.logging.ylogger import YLogger

from programy.config.section import BaseSectionConfigurationData
from programy.config.brain.service import BrainServiceConfiguration
from programy.config.brain.corenlp import BrainCoreNLPConfiguration


class BrainNLPConfiguration(BaseSectionConfigurationData):
    def __init__(self):
        BaseSectionConfigurationData.__init__(self, "nlp")
        self._corenlp = BrainCoreNLPConfiguration()


    @property
    def corenlp(self):
        return self._corenlp

    def load_config_section(self, configuration_file, configuration, bot_root):
        nlp = configuration_file.get_section("nlp", configuration)
        if nlp is not None:
            corenlp = self._corenlp.load_config_section(configuration_file, nlp, bot_root)


        else:
            YLogger.warning(self, "Config section [services] missing from Brain, no services loaded")

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
