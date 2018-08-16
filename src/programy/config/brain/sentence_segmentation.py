from programy.utils.logging.ylogger import YLogger

from programy.config.base import BaseConfigurationData


class BrainSentenceSegmentationConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, name="sentence_segmentation")
        self._classname = None

    @property
    def classname(self):
        return self._classname


    def load_config_section(self, configuration_file, configuration, bot_root):
        sentence_segmentation = configuration_file.get_section(self._section_name, configuration)
        if sentence_segmentation is not None:
            self._classname = configuration_file.get_option(sentence_segmentation, "classname", missing_value="programy.nlp.linguistic_features.sentence_segmentation.SentenceSegmentation")
        else:
            YLogger.warning(self, "'sentence_segmentation' section missing from bot config, using defaults")

    # def to_yaml(self, data, defaults=True):
    #     if defaults is True:
    #         data['classname'] = "programy.parser.tokenizer.Tokenizer"
    #         data['split_chars'] = ' '
    #     else:
    #         data['classname'] = self._classname
    #         data['split_chars'] = self._split_chars
