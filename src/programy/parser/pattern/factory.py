import os

from programy.parser.factory import NodeFactory


class PatternNodeFactory(NodeFactory):

    def __init__(self):
        NodeFactory.__init__(self, "Pattern")

    def default_config_file(self):
        return os.path.dirname(__file__) + os.sep + "pattern_nodes.conf"

    def get_root_node(self):
        root_class = self.new_node_class('root')
        return root_class()
