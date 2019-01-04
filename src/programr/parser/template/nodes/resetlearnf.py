from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.exceptions import ParserException


class TemplateResetLearnfNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        return ""

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "RESETLEARNF"

    def to_xml(self, client_context):
        return "<resetlearnf />"

    #######################################################################################################
    # RESETLEARNF_EXPRESSION ::== <resetlearnf />>

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
        if self.children:
            raise ParserException("<resetlearn> node should not contains child text, use <id /> or <id></id> only")
