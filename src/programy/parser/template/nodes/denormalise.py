from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.base import TemplateNode


######################################################################################################################
#
class TemplateDenormalizeNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        string = self.resolve_children_to_string(client_context)
        resolved = client_context.brain.denormals.denormalise_string(string)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "DENORMALIZE"

    def to_xml(self, client_context):
        xml = "<denormalize>"
        xml += self.children_to_xml(client_context)
        xml += "</denormalize>"
        return xml

    #######################################################################################################
    # DENORMALIZE_EXPRESSION ::== <denormalize>TEMPLATE_EXPRESSION</denormalize>

    def add_default_star(self):
        return True

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
