import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.button import TemplateButtonNode
from programr.parser.template.nodes.word import TemplateWordNode

from programrtest.parser.base import ParserTestsBaseClass

class TemplateButtonNodeTests(ParserTestsBaseClass):

    def test_url_button_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        button = TemplateButtonNode()
        button._text = TemplateWordNode("Servusai.com")
        button._url = TemplateWordNode("http://Servusai.com")

        root.append(button)

        resolved = root.resolve(self._client_context)
        self.assertIsNotNone(resolved)
        self.assertEquals("<button><text>Servusai.com</text><url>http://Servusai.com</url></button>", resolved)

        self.assertEquals("<button><text>Servusai.com</text><url>http://Servusai.com</url></button>", root.to_xml(self._client_context))

    def test_url_postback_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        button = TemplateButtonNode()
        button._text = TemplateWordNode("SAY HELLO")
        button._postback = TemplateWordNode("HELLO")

        root.append(button)

        resolved = root.resolve(self._client_context)
        self.assertIsNotNone(resolved)
        self.assertEquals("<button><text>SAY HELLO</text><postback>HELLO</postback></button>", resolved)

        self.assertEquals("<button><text>SAY HELLO</text><postback>HELLO</postback></button>", root.to_xml(self._client_context))
