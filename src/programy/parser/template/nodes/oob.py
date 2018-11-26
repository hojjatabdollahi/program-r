from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.base import TemplateNode

class TemplateOOBNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        resolved = self.resolve_children_to_string(client_context)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return "<oob>" + resolved + "</oob>"

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "OOB"

    def to_xml(self, client_context):
        xml = "<oob>"
        xml += self.children_to_xml(client_context)
        xml += "</oob>"
        return xml

    def parse_expression(self, graph, expression):

        head_text = self.get_text_from_element(expression)
        self.parse_text(graph, head_text)

        for child in expression:
            graph.parse_tag_expression(child, self)

            tail_text = self.get_tail_from_element(child)
            self.parse_text(graph, tail_text)
