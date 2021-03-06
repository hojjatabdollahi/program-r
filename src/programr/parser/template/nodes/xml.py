from programr.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programr.parser.template.nodes.attrib import TemplateAttribNode
from programr.parser.template.nodes.word import TemplateWordNode
from programr.parser.template.nodes.word import TemplateNode
from programr.utils.text.text import TextUtils


class TemplateXMLNode(TemplateAttribNode):

    def __init__(self):
        TemplateAttribNode.__init__(self)
        self._name = None
        self._attribs = {}

    def set_attrib(self, attrib_name, attrib_value):
        self._attribs[attrib_name] = attrib_value

    def resolve_to_string(self, client_context):
        xml = "<%s" % self._name
        for attrib_name in self._attribs:
            if isinstance(self._attribs[attrib_name], str):
                attrib_value = self._attribs[attrib_name]
            else:
                attrib_value = self._attribs[attrib_name].resolve(client_context)
            escaped = TextUtils.html_escape(attrib_value)
            escaped = escaped.replace(" ", "")
            xml += ' %s="%s"' % (attrib_name, escaped)
        xml += ">"
        xml += self.resolve_children_to_string(client_context)
        xml += "</%s>" % self._name
        return xml

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "XML"

    def to_xml(self, client_context):
        xml = "<%s"%self._name
        for attrib_name in self._attribs:
            if isinstance(self._attribs[attrib_name], str):
                attrib_value = self._attribs[attrib_name]
            else:
                attrib_value = self._attribs[attrib_name].resolve(client_context)
            escaped = TextUtils.html_escape(attrib_value)
            xml += ' %s="%s"' % (attrib_name, escaped)
        xml += ">"
        child_xml = self.children_to_xml(client_context)
        xml += child_xml
        xml += "</%s>"%self._name
        return xml

    def parse_expression(self, graph, expression):
        self._parse_node_with_attribs(graph, expression)

    def _parse_node_with_attribs(self, graph, expression):

        self._name = TextUtils.tag_from_text(expression.tag)

        for attrib_name in expression.attrib:
            attrib_value = expression.attrib[attrib_name]
            if "<" in attrib_value and ">" in attrib_value:
                start = attrib_value.find("<")
                end = attrib_value.rfind(">")

                front = attrib_value[:start]
                middle = attrib_value[start:end+1]
                back = attrib_value[end+1:]

                root = TemplateNode()
                root.append(TemplateWordNode(front))

                xml = ET.fromstring(middle)
                xml_node = TemplateNode()
                graph.parse_tag_expression(xml, xml_node)
                root.append(xml_node)

                root.append(TemplateWordNode(back))

                self.set_attrib(attrib_name, root)

            else:
                self.set_attrib(attrib_name, TemplateWordNode(attrib_value))

        self.parse_text(graph, self.get_text_from_element(expression))

        for child in expression:
            graph.parse_tag_expression(child, self)
            self.parse_text(graph, self.get_tail_from_element(child))
