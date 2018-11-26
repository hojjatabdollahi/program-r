from programy.utils.logging.ylogger import YLogger

from random import randint

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.exceptions import ParserException
from programy.utils.text.text import TextUtils


class TemplateRandomNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        selection = randint(0, (len(self._children) - 1))
        resolved = self._children[selection - 1].resolve(client_context)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    #TODO Same method in every class, move to base class
    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "[RANDOM] %d" % (len(self._children))

    def to_xml(self, client_context):
        xml = "<random>"
        for child in self.children:
            xml += "<li>"
            xml += child.to_xml(client_context)
            xml += "</li>"
        xml += "</random>"
        return xml

    #######################################################################################################
    # 	RANDOM_EXPRESSION ::== <random>(<li>TEMPLATE_EXPRESSION</li>)+</random>

    def parse_expression(self, graph, expression):
        li_found = False
        for child in expression:
            tag_name = TextUtils.tag_from_text(child.tag)

            if tag_name == 'li':
                li_found = True
                li_node = graph.get_base_node()
                self.children.append(li_node)
                li_node.parse_template_node(graph, child)
            else:
                raise ParserException("Unsupported random child tag: %s" % (tag_name), xml_element=expression)

        if li_found is False:
            raise ParserException("No li children of random element!", xml_element=expression)
