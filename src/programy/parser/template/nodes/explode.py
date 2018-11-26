from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.base import TemplateNode


class TemplateExplodeNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        result = self.resolve_children_to_string(client_context)
        letters = [ch for ch in result if ch != ' ']

        resolved = " ".join(letters)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "EXPLODE"

    def to_xml(self, client_context):
        xml = "<explode>"
        xml += self.children_to_xml(client_context)
        xml += "</explode>"
        return xml

    #######################################################################################################
    # <explode>ABC</explode>

    def add_default_star(self):
        return True

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
