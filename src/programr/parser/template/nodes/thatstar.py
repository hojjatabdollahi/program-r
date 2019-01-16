from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.indexed import TemplateDoubleIndexedNode


#####################################################################################################################
#
class TemplateThatStarNode(TemplateDoubleIndexedNode):

    def __init__(self, question=1, sentence=1):
        TemplateDoubleIndexedNode.__init__(self, question, sentence)

    def resolve_to_string(self, client_context):
        conversation = client_context.bot.get_conversation(client_context)

        question = conversation.previous_nth_question(self.question - 1)

        sentence = question.current_sentence()

        resolved = sentence.matched_context.thatstar(self.sentence)

        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        string = "THATSTAR"
        string += self.get_question_and_sentence_as_str()
        return string

    def to_xml(self, client_context):
        xml = "<thatstar"
        xml += self.get_question_and_sentence_as_index_xml()
        xml += "></thatstar>"
        return xml

    #######################################################################################################
    # THATSTAR_EXPRESSION ::== <thatstar( INDEX_ATTRIBUTE)/> | <thatstar><index>TEMPLATE_EXPRESSION</index></thatstar>

    def parse_expression(self, graph, expression):
        self._parse_node_with_attrib(graph, expression, "index", "1,1")
