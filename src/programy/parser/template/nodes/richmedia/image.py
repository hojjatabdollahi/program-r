from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.exceptions import ParserException
from programy.utils.text.text import TextUtils


class TemplateImageNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        str = "<image>%s</image>"%self.resolve_children_to_string(client_context)
        return str

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "[IMAGE] %d" % (len(self._children))

    def to_xml(self, client_context):
        return self.resolve_to_string(client_context)

    #######################################################################################################
    #
    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)

