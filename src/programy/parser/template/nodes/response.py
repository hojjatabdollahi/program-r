from programy.utils.logging.ylogger import YLogger
from programy.parser.template.nodes.indexed import TemplateIndexedNode



######################################################################################################################
#
# <response index=”n”/> is replaced with the value of the nth previous multi-sentence bot response..
# The response element returns the bot’s response specified by its historical index value.
#
class TemplateResponseNode(TemplateIndexedNode):

    def __init__(self, index=1):
        TemplateIndexedNode.__init__(self, index)

    def resolve_to_string(self, client_context):
        conversation = client_context.bot.get_conversation(client_context)
        question = conversation.previous_nth_question(self.index)
        resolved = question.combine_answers()
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        string = "RESPONSE"
        string += self.get_index_as_str()
        return string

    def to_xml(self, client_context):
        xml = "<response"
        xml += self.get_index_as_xml()
        xml += ">"
        xml += "</response>"
        return xml

    #######################################################################################################
    # RESPONSE_EXPRESSION ::== <response( INDEX_ATTRIBUTE)/> | <response><index>TEMPLATE_EXPRESSION</index></response>

    def parse_expression(self, graph, expression):
        self._parse_node_with_attrib(graph, expression, "index", "1")
        if self.children:
            YLogger.warning(self, "<response> node should not contain child text, use <response /> or <response></response> only")
