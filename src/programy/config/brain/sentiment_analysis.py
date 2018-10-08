from programy.utils.logging.ylogger import YLogger

from programy.config.base import BaseConfigurationData


class BrainSentimentAnalysisConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, name="sentiment_analysis")
        self._method = None
        self._alpha = None
        self._negative_threshold = None
        self._positive_thresehold = None


    @property
    def method(self):
        return self._method

    @property
    def positive_threshold(self):
        return self._positive_thresehold

    @property
    def negative_threshold(self):
        return self._negative_threshold

    @property
    def alpha(self):
        return self._alpha


    def load_config_section(self, configuration_file, configuration, bot_root):
        sentiment_analysis = configuration_file.get_section(self._section_name, configuration)
        if sentiment_analysis is not None:
            self._method = configuration_file.get_option(sentiment_analysis, "method", missing_value="default")
            self._negative_threshold = configuration_file.get_float_option(sentiment_analysis, "negative_threshold", missing_value=0.1)
            self._positive_thresehold = configuration_file.get_float_option(sentiment_analysis, "positive_threshold", missing_value=-0.1)
            self._alpha = configuration_file.get_float_option(sentiment_analysis, "alpha", missing_value=0.0)
        else:
            YLogger.warning(self, "'sentiment_analysis' section missing from bot config, using defaults")
