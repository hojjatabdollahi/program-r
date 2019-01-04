from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.exceptions import ParserException


class TemplateResetLearnNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        YLogger.debug(client_context, "Removing all learn nodes created by [%s]", client_context.userid)
        root = client_context.brain.aiml_parser.pattern_parser.root
        root.remove_children_with_userid(client_context.userid)
        return ""

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "RESETLEARN"

    def to_xml(self, client_context):
        return "<resetlearn />"

    #######################################################################################################
    # RESETLEARN_EXPRESSION ::== <resetlearn />

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
        if self.children:
            raise ParserException("<resetlearn> node should not contain child text, use <resetlearn /> or <resetlearn></resetlearn> only")
