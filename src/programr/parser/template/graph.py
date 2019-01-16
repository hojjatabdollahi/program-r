from programr.parser.exceptions import ParserException
from programr.parser.template.factory import TemplateNodeFactory
from programr.utils.text.text import TextUtils

class TemplateGraph(object):

    def __init__(self, aiml_parser):
        self._aiml_parser = aiml_parser

        self.load_template_node_factory()

    @property
    def aiml_parser(self):
        return self._aiml_parser

    @property
    def template_factory(self):
        return self._template_factory

    def load_template_node_factory(self):
        template_nodes = self._aiml_parser.brain.configuration.nodes.template_nodes
        self._template_factory = TemplateNodeFactory()
        self._template_factory.load_nodes_config_from_file(template_nodes)

    #
    # TEMPLATE_EXPRESSION ::== TEXT | TAG_EXPRESSION | (TEMPLATE_EXPRESSION)*
    #
    def parse_template_expression(self, pattern):
        node = self.get_base_node()
        node.parse_template_node(self, pattern)
        return node

    def get_node_class_by_name(self, name):
        if self._template_factory.exists(name):
            return self._template_factory.new_node_class(name)
        else:
            raise ParserException("No node [%s] registered in Template Node Factory"%(name))

    # Helper function to return TemplateNode
    def get_base_node(self):
        base_class = self.get_node_class_by_name('base')
        return base_class()

    # Helper function to return TemplateWordNode
    def get_word_node(self, text):
        word_class = self.get_node_class_by_name('word')
        return word_class(text)

    def parse_tag_expression(self, expression, branch):
        tag_name = TextUtils.tag_from_text(expression.tag)
        if self._template_factory.exists(tag_name):
            if tag_name == "condition":
                node_instance = self._template_factory.new_node_class(tag_name)()
            else:
                node_instance = self._template_factory.new_node_class(tag_name)()
            node_instance.parse_expression(self, expression)
            branch.children.append(node_instance)
        else:
            self.parse_unknown_as_xml_node(expression, branch)

    #######################################################################################################
    # 	UNKNONWN NODE
    #   When its a node we don't know, add it as a text node. This deals with html nodes creeping into the text
    def parse_unknown_as_xml_node(self, expression, branch):
        xml_node_class = self.get_node_class_by_name('xml')
        xml_node = xml_node_class()
        branch.children.append(xml_node)
        xml_node.parse_expression(self, expression)
