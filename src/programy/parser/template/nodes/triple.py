from programy.parser.template.nodes.base import TemplateNode
from programy.utils.text.text import TextUtils


class TemplateTripleNode(TemplateNode):

    def __init__(self, node_name, subj=None, pred=None, obj=None):
        TemplateNode.__init__(self)
        self._node_name = node_name
        self._subj = subj
        self._pred = pred
        self._obj = obj

    @property
    def node_name(self):
        return self._node_name

    def children_to_xml(self, client_context):
        xml = ""
        if self._subj is not None:
            subj = self._subj.resolve(client_context)
            xml += "<subj>" + subj + "</subj>"
        if self._pred is not None:
            pred = self._pred.resolve(client_context)
            xml += "<pred>" + pred + "</pred>"
        if self._obj is not None:
            obj = self._obj.resolve(client_context)
            xml += "<obj>" + obj + "</obj>"
        return xml

    def parse_expression(self, graph, expression):

        if 'subj' in expression.attrib:
            self._subj = graph.get_word_node(expression.attrib['subj'])

        if 'pred' in expression.attrib:
            self._pred = graph.get_word_node(expression.attrib['pred'])

        if 'obj' in expression.attrib:
            self._obj = graph.get_word_node(expression.attrib['obj'])

        head_text = self.get_text_from_element(expression)
        self.parse_text(graph, head_text)

        for child in expression:
            tag_name = TextUtils.tag_from_text(child.tag)

            if tag_name == 'subj':
                self._subj = self.parse_children_as_word_node(graph, child)
            elif tag_name == 'pred':
                self._pred = self.parse_children_as_word_node(graph, child)
            elif tag_name == 'obj':
                self._obj = self.parse_children_as_word_node(graph, child)
            else:
                graph.parse_tag_expression(child, self)

            tail_text = self.get_tail_from_element(child)
            self.parse_text(graph, tail_text)

