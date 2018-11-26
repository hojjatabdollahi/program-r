from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.indexed import TemplateIndexedNode

######################################################################################################################
#
# <topicstar />
# <topicstar index=”n” />
# The topicstar element will either return the current topic if used outside of a topic element or the wildcard
# element when inside a topic element. The topicstar element can also use index like the star element can, though
# this will return as the default case for empty predicates if no wildcards are present.

class TemplateTopicStarNode(TemplateIndexedNode):

    def __init__(self, index=1):
        TemplateIndexedNode.__init__(self, index)

    def resolve_to_string(self, client_context):
        conversation = client_context.bot.get_conversation(client_context)
        question = conversation.current_question()
        sentence = question.current_sentence()
        resolved = sentence.matched_context.topicstar(self.index)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        string = "TOPICSTAR"
        string += self.get_index_as_str()
        return string

    def to_xml(self, client_context):
        xml = "<topicstar"
        xml += self.get_index_as_xml()
        xml += ">"
        xml += "</topicstar>"
        return xml

    #######################################################################################################
    # TOPICSTAR_EXPRESSION ::== <topicstar( INDEX_ATTRIBUTE)/> | <topicstar><index>TEMPLATE_EXPRESSION</index></topicstar>

    def parse_expression(self, graph, expression):
        self._parse_node_with_attrib(graph, expression, "index", "1")
