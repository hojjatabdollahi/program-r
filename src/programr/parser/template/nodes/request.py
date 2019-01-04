from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.indexed import TemplateIndexedNode
from programr.parser.exceptions import ParserException

######################################################################################################################
#
# <request index=”n”/> is replaced with the value of the nth previous multi-sentence input to the bot.
# The request element returns the user’s input specified by its historical index value.

class TemplateRequestNode(TemplateIndexedNode):

    def __init__(self, index=1):
        TemplateIndexedNode.__init__(self, index)

    def resolve_to_string(self, client_context):
        conversation = client_context.bot.get_conversation(client_context)
        question = conversation.previous_nth_question(self.index)
        resolved = question.combine_sentences()
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context,"Failed to resolve",  excep)
            return ""

    def to_string(self):
        string = "REQUEST"
        string += self.get_index_as_str()
        return string

    def to_xml(self, client_context):
        xml = "<request"
        xml += self.get_index_as_xml()
        xml += ">"
        xml += "</request>"
        return xml

    #######################################################################################################
    # REQUEST_EXPRESSION ::== <request( INDEX_ATTRIBUTE)/> | <request><index>TEMPLATE_EXPRESSION</index></request>

    def parse_expression(self, graph, expression):
        self._parse_node_with_attrib(graph, expression, "index", "1")
        if self.children:
            raise ParserException("<request> node should not contain child text, use <request /> or <request></request> only")
