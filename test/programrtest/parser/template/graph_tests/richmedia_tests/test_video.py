import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.video import TemplateVideoNode

from programrtest.parser.template.graph_tests.graph_test_client import TemplateGraphTestClient


class TemplateGraphVideoTests(TemplateGraphTestClient):

    def test_video_node_from_xml(self):
        template = ET.fromstring("""
			<template>
				<video>http://http://www.servusai.com/aiml.mov</video>
			</template>
			""")
        root = self._graph.parse_template_expression(template)
        self.assertIsNotNone(root)
        self.assertIsInstance(root, TemplateNode)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 1)

        node = root.children[0]
        self.assertIsNotNone(node)
        self.assertIsInstance(node, TemplateVideoNode)

        self.assertEquals("http://http://www.servusai.com/aiml.mov", node.resolve_children_to_string(self._client_context))