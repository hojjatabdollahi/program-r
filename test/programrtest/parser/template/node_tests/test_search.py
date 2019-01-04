import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.word import TemplateWordNode
from programr.parser.template.nodes.search import TemplateSearchNode

from programrtest.parser.base import ParserTestsBaseClass

class MockTemplateSearchNode(TemplateSearchNode):
    def __init__(self):
        TemplateSearchNode.__init__(self)

    def resolve_to_string(self, context):
        raise Exception("This is an error")

class TemplateSearchNodeTests(ParserTestsBaseClass):

    def test_to_string(self):
        root = TemplateSearchNode()
        self.assertIsNotNone(root)
        self.assertEquals("SEARCH", root.to_string())

    def test_to_xml(self):
        root = TemplateNode()
        node = TemplateSearchNode()
        root.append(node)
        node.append(TemplateWordNode("programr"))

        xml = root.xml_tree(self._client_context)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual("<template><search>programr</search></template>", xml_str)

    def test_node(self):
        root = TemplateNode()
        node = TemplateSearchNode()
        root.append(node)
        node.append(TemplateWordNode("programr"))

        result = node.resolve(self._client_context)
        self.assertIsNotNone(result)
        self.assertEqual("https://www.google.co.uk/search?q=programr", result)

    def test_node_exception_handling(self):
        root = TemplateNode()
        node = MockTemplateSearchNode()
        root.append(node)

        result = root.resolve(self._client_context)
        self.assertIsNotNone(result)
        self.assertEquals("", result)