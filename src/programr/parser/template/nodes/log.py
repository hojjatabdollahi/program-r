from programr.utils.logging.ylogger import YLogger


from programr.parser.exceptions import ParserException
from programr.parser.template.nodes.attrib import TemplateAttribNode



class TemplateLogNode(TemplateAttribNode):

    def __init__(self):
        TemplateAttribNode.__init__(self)
        self._level = "debug"
        self._output = "logging"

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def resolve_to_string(self, client_context):
        resolved = self.resolve_children_to_string(client_context)

        if self._output == "logging":
            YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
            if self._level == "debug":
                YLogger.debug(client_context, resolved)
            elif self._level == "warning":
                YLogger.warning(client_context, resolved)
            elif self._level == "error":
                YLogger.error(client_context, resolved)
            elif self._level == "info":
                YLogger.info(client_context, resolved)
            else:
                YLogger.info(client_context, resolved)
        else:
            print(resolved)
        return ""

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "LOG level=%s" % (self._level)

    def set_attrib(self, attrib_name, attrib_value):
        if attrib_name != 'level' and attrib_name != 'output':
            raise ParserException("Invalid attribute name %s for this node", attrib_name)
        if attrib_value not in ['debug', 'info', 'warning', 'error'] and \
            attrib_value not in ["logging", "print"]:
            raise ParserException("Invalid attribute value %s for this node %s", attrib_value, attrib_name)
        self._level = attrib_value

    def to_xml(self, client_context):
        xml = "<log"
        if self._level is not None:
            xml += ' level="%s"' % self._level
        xml += ">"
        xml += self.children_to_xml(client_context)
        xml += "</log>"
        return xml

    #######################################################################################################
    # LOG_EXPRESSION ::== <log>Message</log>
    #                           <log level="error|warning|debug|info">Message</log>
    #

    def parse_expression(self, graph, expression):
        self._parse_node_with_attribs(graph, expression, [["level", "debug"],["output", "logging"]])
