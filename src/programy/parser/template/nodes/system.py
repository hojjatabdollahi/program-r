from programy.utils.logging.ylogger import YLogger
import subprocess

from programy.parser.exceptions import ParserException
from programy.parser.template.nodes.attrib import TemplateAttribNode


class TemplateSystemNode(TemplateAttribNode):

    def __init__(self):
        TemplateAttribNode.__init__(self)
        self._timeout = 0

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    def resolve_to_string(self, client_context):
        if client_context.brain.configuration.overrides.allow_system_aiml is True:
            command = self.resolve_children_to_string(client_context)
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = []
            for line in process.stdout.readlines():
                byte_string = line.decode("utf-8")
                result.append(byte_string.strip())
            process.wait()
            resolved = " ".join(result)
        else:
            YLogger.warning(client_context, "System command node disabled in config")
            resolved = ""
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "SYSTEM timeout=%s" % (self._timeout)

    def set_attrib(self, attrib_name, attrib_value):
        if attrib_name != 'timeout':
            raise ParserException("Invalid attribute name %s for this node", attrib_name)
        YLogger.warning(self, "System node timeout attrib currently ignored")
        self._timeout = attrib_value

    def to_xml(self, client_context):
        xml = "<system"
        if self._timeout != 0:
            xml += ' timeout="%d"' % self._timeout
        xml += ">"
        xml += self.children_to_xml(client_context)
        xml += "</system>"
        return xml

    #######################################################################################################
    # SYSTEM_EXPRESSION ::==
    # 		<system( TIMEOUT_ATTRIBUTE)>TEMPLATE_EXPRESSION</system> |
    #  		<system><timeout>TEMPLATE_EXPRESSION</timeout></system>
    # TIMEOUT_ATTRIBUTE :== timeout=”NUMBER”

    def parse_expression(self, graph, expression):
        self._parse_node_with_attrib(graph, expression, "timeout", "0")
