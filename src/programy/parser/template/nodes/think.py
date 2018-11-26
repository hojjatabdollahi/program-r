from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.base import TemplateNode



class TemplateThinkNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        resolved = self.resolve_children_to_string(client_context)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return ""

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "THINK"

    def to_xml(self, client_context):
        xml = "<think>"
        xml += self.children_to_xml(client_context)
        xml += "</think>"
        return xml

    #######################################################################################################
    # THINK_EXPRESSION ::== <think>TEMPLATE_EXPRESSION</think>

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
