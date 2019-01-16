import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.resetlearnf import TemplateResetLearnfNode
from programr.parser.exceptions import ParserException

from programrtest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient

class TemplateGraphResetLearnfTests(TemplateGraphTestClient):

     def test_learnf_type1(self):
        template = ET.fromstring("""
			<template>
				<resetlearnf />
			</template>
			""")

        ast = self._graph.parse_template_expression(template)
        self.assertIsNotNone(ast)

        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertIsNotNone(ast.children[0])
        self.assertIsInstance(ast.children[0], TemplateResetLearnfNode)
        self.assertEqual(0, len(ast.children[0].children))

     def test_learnf_type2(self):
        template = ET.fromstring("""
			<template>
				<resetlearnf></resetlearnf>
			</template>
			""")

        ast = self._graph.parse_template_expression(template)
        self.assertIsNotNone(ast)

        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertIsNotNone(ast.children[0])
        self.assertIsInstance(ast.children[0], TemplateResetLearnfNode)
        self.assertEqual(0, len(ast.children[0].children))

     def test_request_with_children(self):
        template = ET.fromstring("""
			<template>
				<resetlearnf>Error</resetlearnf>
			</template>
			""")
        with self.assertRaises(ParserException):
            ast = self._graph.parse_template_expression(template)
