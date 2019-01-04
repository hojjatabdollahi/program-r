import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.search import TemplateSearchNode

from programrtest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphSearchTests(TemplateGraphTestClient):

    def test_search_basic(self):
        template = ET.fromstring("""
			<template>
			    <search>
			        keith sterling
			    </search>
			</template>
			""")

        ast = self._graph.parse_template_expression(template)
        self.assertIsNotNone(ast)

        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertIsNotNone(ast.children[0])
        self.assertIsInstance(ast.children[0], TemplateSearchNode)

        result = ast.resolve(self._client_context)
        self.assertIsNotNone(result)
        self.assertEquals("https://www.google.co.uk/search?q=keith+sterling", result)