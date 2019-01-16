import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.image import TemplateImageNode
from programr.parser.template.nodes.word import TemplateWordNode

from programrtest.parser.base import ParserTestsBaseClass

class TemplateImageNodeTests(ParserTestsBaseClass):

    def test_image_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        image = TemplateImageNode()

        url = TemplateWordNode("http://Servusai.com/logo.png")

        root.append(image)
        image.append(url)

        resolved = root.resolve(self._client_context)
        self.assertIsNotNone(resolved)
        self.assertEquals("<image>http://Servusai.com/logo.png</image>", resolved)

        self.assertEquals("<image>http://Servusai.com/logo.png</image>", root.to_xml(self._client_context))

