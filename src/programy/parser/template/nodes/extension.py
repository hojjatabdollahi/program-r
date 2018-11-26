from programy.utils.logging.ylogger import YLogger

from programy.utils.classes.loader import ClassLoader
from programy.parser.template.nodes.base import TemplateNode
from programy.utils.text.text import TextUtils
from programy.parser.exceptions import ParserException


######################################################################################################################
#
class TemplateExtensionNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)
        self._path = None

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def resolve_to_string(self, client_context):
        data = self.resolve_children_to_string(client_context)

        new_class = ClassLoader.instantiate_class(self._path)
        instance = new_class()
        resolved = instance.execute(client_context, data)

        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "EXTENSION (%s)" % self._path

    def to_xml(self, client_context):
        xml = '<extension'
        xml += ' path="%s"' % self._path
        xml += '>'
        xml += self.children_to_xml(client_context)
        xml += '</extension>'
        return xml

    #######################################################################################################
    # EXTENSION_EXPRESSION ::== <extension>
    #                               <path>programy.etension.SomeModule</path>
    #                               parameters
    # 						</extension>

    def parse_expression(self, graph, expression):

        if 'path' in expression.attrib:
            self.path = expression.attrib['path']

        head_text = self.get_text_from_element(expression)
        self.parse_text(graph, head_text)

        for child in expression:
            tag_name = TextUtils.tag_from_text(child.tag)

            if tag_name == 'path':
                self.path = self.get_text_from_element(child)
            else:
                graph.parse_tag_expression(child, self)

            tail_text = self.get_tail_from_element(child)
            self.parse_text(graph, tail_text)

        if self.path is None:
            raise ParserException("EXTENSION node, path attribute missing !")
