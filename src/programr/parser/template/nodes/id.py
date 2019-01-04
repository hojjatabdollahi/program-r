from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.exceptions import ParserException


class TemplateIdNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve(self, client_context):
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), client_context.client.id)
        if client_context.client.id is not None:
            return client_context.client.id
        return ""

    def to_string(self):
        return "ID"

    def to_xml(self, client_context):
        return "<id />"

    #######################################################################################################
    # <id/> |

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
        if self.children:
            raise ParserException("<id> node should not contain child text, use <id /> or <id></id> only")
