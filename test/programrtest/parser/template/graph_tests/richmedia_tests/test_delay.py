import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.delay import TemplateDelayNode

from programrtest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphDelayTests(TemplateGraphTestClient):

    def test_delay_node_from_xml(self):
        template = ET.fromstring("""
			<template>
				<delay><seconds>10</seconds></delay>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
        self.assertIsInstance(root, TemplateNode)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 1)

        node = root.children[0]
        self.assertIsNotNone(node)
        self.assertIsInstance(node, TemplateDelayNode)

        self.assertEquals("10", node._seconds.resolve(self._client_context))