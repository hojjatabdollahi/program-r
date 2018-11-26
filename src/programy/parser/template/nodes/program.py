from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.exceptions import ParserException

class TemplateProgramNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        fullname = "AIMLBot"
        if client_context.brain.properties.has_property("fullname") is True:
            fullname = client_context.brain.properties.property("fullname")
        else:
            YLogger.error(client_context, "Fullname property missing")

        version = ""
        if client_context.brain.properties.has_property("version") is True:
            version = client_context.brain.properties.property("version")
        else:
            YLogger.error(client_context, "Version property missing")

        resolved = "%s %s" % (fullname, version)
        YLogger.debug(self, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "PROGRAM"

    def to_xml(self, client_context):
        xml = "<program />"
        return xml

    #######################################################################################################
    # <program/>	'''

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
        if self.children:
            raise ParserException(
                "<program> node should not contain child text, use <program /> or <program></program> only")
