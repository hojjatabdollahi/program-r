from programy.utils.logging.ylogger import YLogger

from programy.config.section import BaseSectionConfigurationData


class BrainNodesConfiguration(BaseSectionConfigurationData):

    def __init__(self):
        BaseSectionConfigurationData.__init__(self, "nodes")
        self._pattern_nodes = None
        self._template_nodes = None

    @property
    def pattern_nodes(self):
        return self._pattern_nodes

    @property
    def template_nodes(self):
        return self._template_nodes

    def load_config_section(self, configuration_file, configuration, bot_root):
        nodes = configuration_file.get_section("nodes", configuration)
        if nodes is not None:
            pattern_nodes = configuration_file.get_option(nodes, "pattern_nodes", missing_value=None)
            if pattern_nodes is not None:
                self._pattern_nodes = self.sub_bot_root(pattern_nodes, bot_root)
            template_nodes = configuration_file.get_option(nodes, "template_nodes", missing_value=None)
            if template_nodes is not None:
                self._template_nodes = self.sub_bot_root(template_nodes, bot_root)
        else:
            YLogger.warning(self, "'nodes' section missing from bot config, using to defaults")

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['pattern_nodes'] = "./config/pattern_nodes.conf"
            data['template_nodes'] = "./config/template_nodes.conf"
        else:
            data['pattern_nodes'] = self._pattern_nodes
            data['template_nodes'] = self._template_nodes
