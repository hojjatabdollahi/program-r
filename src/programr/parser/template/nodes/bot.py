from programr.utils.logging.ylogger import YLogger
from programr.parser.template.nodes.base import TemplateNode
from programr.parser.exceptions import ParserException
from programr.utils.text.text import TextUtils

class TemplateBotNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)
        self._name = None
        self.local = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def get_bot_variable(client_context, name):
        value = client_context.brain.properties.property(name)
        if value is None:
            YLogger.error(client_context, "No bot property for [%s]", name)

            value = client_context.brain.properties.property("default-property")
            if value is None:
                YLogger.error(client_context, "No value for default-property")

                value = client_context.brain.configuration.defaults.default_get
                if value is None:
                    YLogger.error(client_context, "No value for default default-property, return 'unknown'")
                    value = "unknown"

        return value

    def resolve_to_string(self, client_context):
        name = self.name.resolve(client_context)
        value = TemplateBotNode.get_bot_variable(client_context, name)
        YLogger.debug(client_context, "[%s] resolved to [%s] = [%s]", self.to_string(), name, value)
        return value

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "[BOT (%s)]" % (self.name.to_string())

    def to_xml(self, client_context):
        xml = "<bot "
        xml += ' name="%s"' % self.name.resolve(client_context)
        xml += " />"
        return xml

    # ######################################################################################################
    # BOT_PROPERTY_EXPRESSION ::==
    # <bot name="PROPERTY"/> |
    # <bot><name>TEMPLATE_EXPRESSION</name></bot>

    def parse_expression(self, graph, expression):
        name_found = False

        if 'name' in expression.attrib:
            self.name = self.parse_attrib_value_as_word_node(graph, expression, 'name')
            name_found = True

        self.parse_text(graph, self.get_text_from_element(expression))

        for child in expression:
            tag_name = TextUtils.tag_from_text(child.tag)

            if tag_name == 'name':
                self.name = self.parse_children_as_word_node(graph, child)
                self.local = False
                name_found = True

            else:
                graph.parse_tag_expression(child, self)

            self.parse_text(graph, self.get_tail_from_element(child))

        if name_found is False:
            raise ParserException("Name not found in bot", xml_element=expression)
