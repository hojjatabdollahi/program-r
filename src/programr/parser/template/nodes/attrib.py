from programr.utils.logging.ylogger import YLogger
from programr.utils.text.text import TextUtils
from programr.parser.template.nodes.base import TemplateNode

class TemplateAttribNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def set_attrib(self, attrib_name, attrib_value):
        raise NotImplementedError("Should not call this base method, implementation missing")

    #######################################################################################################

    def _parse_node_with_attribs(self, graph, expression, attribs):

        attribs_found = []
        for attrib in attribs:
            attrib_name = attrib[0]
            if attrib_name in expression.attrib:
                self.set_attrib(attrib_name, expression.attrib[attrib_name])
                attribs_found.append(attrib_name)

        self.parse_text(graph, self.get_text_from_element(expression))

        for child in expression:
            tag_name = TextUtils.tag_from_text(child.tag)

            for attrib in attribs:
                attrib_name = attrib[0]
                if tag_name == attrib_name:
                    self.set_attrib(attrib[0], self.get_text_from_element(child))
                else:
                    graph.parse_tag_expression(child, self)

            self.parse_text(graph, self.get_tail_from_element(child))

        for attrib in attribs:
            attrib_name = attrib[0]
            if attrib_name not in attribs_found:
                if attrib[1] is not None:
                    YLogger.debug(self, "Setting default value for attrib [%s]", attrib_name)
                    self.set_attrib(attrib_name, attrib[1])

    def _parse_node_with_attrib(self, graph, expression, attrib_name, default_value=None):

        attrib_found = True
        if attrib_name in expression.attrib:
            self.set_attrib(attrib_name, expression.attrib[attrib_name])

        self.parse_text(graph, self.get_text_from_element(expression))

        for child in expression:
            tag_name = TextUtils.tag_from_text(child.tag)

            if tag_name == attrib_name:
                self.set_attrib(attrib_name, self.get_text_from_element(child))
            else:
                graph.parse_tag_expression(child, self)

            self.parse_text(graph, self.get_tail_from_element(child))

        if attrib_found is False:
            YLogger.debug(self, "Setting default value for attrib [%s]", attrib_name)
            self.set_attrib(attrib_name, default_value)
