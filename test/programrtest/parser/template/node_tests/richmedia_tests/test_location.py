import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.location import TemplateLocationNode
from programr.parser.template.nodes.word import TemplateWordNode

from programrtest.parser.base import ParserTestsBaseClass

class TemplateLocationNodeTests(ParserTestsBaseClass):

    def test_location_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        location = TemplateLocationNode()

        root.append(location)

        resolved = root.resolve(self._client_context)
        self.assertIsNotNone(resolved)
        self.assertEquals("<location />", resolved)

        self.assertEquals("<location />", root.to_xml(self._client_context))

