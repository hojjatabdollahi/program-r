from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.exceptions import ParserException

class TemplateSizeNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        resolved = str(client_context.brain.aiml_parser.num_categories)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "SIZE"

    def to_xml(self, client_context):
        xml = "<size />"
        return xml

    #######################################################################################################
    # <size/> |

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
        if self.children:
            raise ParserException("<size> node should not contain child text, use <size /> or <size></size> only")
