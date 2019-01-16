from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.exceptions import ParserException


class TemplateSrNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        sentence = client_context.bot.get_conversation(client_context).current_question().current_sentence()
        star = sentence.matched_context.star(1)
        if star is not None:
            resolved = client_context.bot.ask_question(client_context, star, srai=True)
        else:
            YLogger.error(client_context, "Sr node has no stars available")
            resolved = ""
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "SR"

    def to_xml(self, client_context):
        xml = "<sr />"
        return xml

    #######################################################################################################
    # <sr/> |

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
        if self.children:
            raise ParserException("<sr> node should not contain child text, use <sr /> or <sr></sr> only")
