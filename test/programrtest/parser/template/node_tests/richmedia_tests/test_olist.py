import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.olist import TemplateOrderedListNode
from programr.parser.template.nodes.word import TemplateWordNode

from programrtest.parser.base import ParserTestsBaseClass

class TemplateListNodeTests(ParserTestsBaseClass):

    def test_olist_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        list = TemplateOrderedListNode()

        list._items.append(TemplateWordNode("Item1"))
        list._items.append(TemplateWordNode("Item2"))

        root.append(list)

        resolved = root.resolve(self._client_context)

        self.assertIsNotNone(resolved)
        self.assertEquals("<olist><item>Item1</item><item>Item2</item></olist>", resolved)

        self.assertEquals("<olist><item>Item1</item><item>Item2</item></olist>", root.to_xml(self._client_context))

