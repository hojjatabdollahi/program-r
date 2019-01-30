import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.split import TemplateSplitNode
from programr.parser.template.nodes.word import TemplateWordNode

from programrtest.parser.base import ParserTestsBaseClass

class TemplateSplitNodeTests(ParserTestsBaseClass):

    def test_split_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        split = TemplateSplitNode()

        root.append(split)

        resolved = root.resolve(self._client_context)
        self.assertIsNotNone(resolved)
        self.assertEquals("<split />", resolved)

        self.assertEquals("<split />", root.to_xml(self._client_context))
