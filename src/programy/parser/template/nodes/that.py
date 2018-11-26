from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.indexed import TemplateDoubleIndexedNode

######################################################################################################################
#
# <that />
# <that index=”n” />
# <that index="m,n" />
#
class TemplateThatNode(TemplateDoubleIndexedNode):

    def __init__(self, question=1, sentence=1):
        TemplateDoubleIndexedNode.__init__(self, question, sentence)

    def resolve_to_string(self, client_context):
        conversation = client_context.bot.get_conversation(client_context)
        question = conversation.previous_nth_question(self.question)
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
        string = "THAT"
        string += self.get_question_and_sentence_as_str()
        return string

    def to_xml(self, client_context):
        xml = "<that"
        xml += self.get_question_and_sentence_as_index_xml()
        xml += ">"
        xml += "</that>"
        return xml

    #######################################################################################################
    # THAT_EXPRESSION ::== <that( INDEX_ATTRIBUTE)/> | <that><index></index></that>

    def parse_expression(self, graph, expression):
        self._parse_node_with_attrib(graph, expression, "index", "1")
