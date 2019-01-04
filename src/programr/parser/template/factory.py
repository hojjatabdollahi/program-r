import os
from programr.parser.factory import NodeFactory

class TemplateNodeFactory(NodeFactory):

    def __init__(self):
        NodeFactory.__init__(self, "Template")

    def default_config_file(self):
        return os.path.dirname(__file__) + os.sep + "template_nodes.conf"
