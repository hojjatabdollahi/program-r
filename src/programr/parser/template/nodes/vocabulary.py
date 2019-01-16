from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode


class TemplateVocabularyNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        set_words = client_context.brain.sets.count_words_in_sets()
        pattern_words = client_context.brain.aiml_parser.pattern_parser.count_words_in_patterns()
        resolved = "%d" % (set_words + pattern_words)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "VOCABULARY"

    def to_xml(self, client_context):
        xml = "<vocabulary>"
        xml += self.children_to_xml(client_context)
        xml += "</vocabulary>"
        return xml

    #######################################################################################################
    # <vocabulary/> |

    def add_default_star(self):
        return True

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
