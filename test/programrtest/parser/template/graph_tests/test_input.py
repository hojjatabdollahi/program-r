import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.input import TemplateInputNode
from programr.parser.exceptions import ParserException

from programrtest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphInputTests(TemplateGraphTestClient):

    def test_input_node_from_xml(self):
        template = ET.fromstring("""
			<template>
				<input/>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
        self.assertIsInstance(root, TemplateNode)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 1)

        node = root.children[0]
        self.assertIsNotNone(node)
        self.assertIsInstance(node, TemplateInputNode)

    def test_input_node_with_children(self):
        template = ET.fromstring("""
			<template>
				<input>Text</input>
			</template>
			""")
        with self.assertRaises(ParserException):
            root = self._graph.parse_template_expression(template)