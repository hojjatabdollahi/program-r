import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.word import TemplateWordNode
from programr.parser.template.nodes.get import TemplateGetNode
from programr.parser.template.nodes.oob import TemplateOOBNode

from programrtest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphOOBTests(TemplateGraphTestClient):

    def test_oob_node_from_xml_single_word(self):
        template = ET.fromstring("""
			<template>
				<oob>Text</oob>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
        self.assertIsInstance(root, TemplateNode)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 1)

        node = root.children[0]
        self.assertIsNotNone(node)
        self.assertIsInstance(node, TemplateOOBNode)

    def test_oob_node_from_xml_multi_words(self):
        template = ET.fromstring("""
			<template>
				<oob>Some Text</oob>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
        self.assertIsInstance(root, TemplateNode)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 1)

        node = root.children[0]
        self.assertIsNotNone(node)
        self.assertIsInstance(node, TemplateOOBNode)

        self.assertEquals(len(node.children), 2)
        self.assertIsInstance(node.children[0], TemplateWordNode)
        self.assertEquals(node.children[0].word, "Some")
        self.assertIsInstance(node.children[1], TemplateWordNode)
        self.assertEquals(node.children[1].word, "Text")

    def test_oob_node_from_xml_multi_words(self):
        template = ET.fromstring("""
			<template>
				<oob>Some <get name="SomeGet" /> Text</oob>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
        self.assertIsInstance(root, TemplateNode)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 1)

        node = root.children[0]
        self.assertIsNotNone(node)
        self.assertIsInstance(node, TemplateOOBNode)

        self.assertEquals(len(node.children), 3)
        self.assertIsInstance(node.children[0], TemplateWordNode)
        self.assertEquals(node.children[0].word, "Some")
        self.assertIsInstance(node.children[1], TemplateGetNode)
        self.assertIsInstance(node.children[2], TemplateWordNode)
        self.assertEquals(node.children[2].word, "Text")

    def test_oob_node_from_xml_unknown_elements(self):
        template = ET.fromstring("""
			<template>
				<oob><dial><star /></dial></oob>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
