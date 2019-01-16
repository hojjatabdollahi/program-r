from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode

class TemplateEvalNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        resolved = self.resolve_children_to_string(client_context)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "EVAL"

    def to_xml(self, client_context):
        xml = "<eval>"
        xml += self.children_to_xml(client_context)
        xml += "</eval>"
        return xml

    #######################################################################################################
    # EVAL_EXPRESSION ::== <eval>TEMPLATE_EXPRESSION</eval>
    #

    def parse_expression(self, graph, expression):

        head_text = self.get_text_from_element(expression)
        self.parse_text(graph, head_text)

        for child in expression:
            graph.parse_tag_expression(child, self)

            tail_text = self.get_tail_from_element(child)
            self.parse_text(graph, tail_text)
