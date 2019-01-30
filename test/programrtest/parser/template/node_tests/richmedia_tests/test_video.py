import xml.etree.ElementTree as ET

from programr.parser.template.nodes.base import TemplateNode
from programr.parser.template.nodes.richmedia.video import TemplateVideoNode
from programr.parser.template.nodes.word import TemplateWordNode

from programrtest.parser.base import ParserTestsBaseClass

class TemplateVideoNodeTests(ParserTestsBaseClass):

    def test_video_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.children)
        self.assertEqual(len(root.children), 0)

        video = TemplateVideoNode()

        url = TemplateWordNode("http://Servusai.com/logo.mov")

        root.append(video)
        video.append(url)

        resolved = root.resolve(self._client_context)
        self.assertIsNotNone(resolved)
        self.assertEquals("<video>http://Servusai.com/logo.mov</video>", resolved)

        self.assertEquals("<video>http://Servusai.com/logo.mov</video>", root.to_xml(self._client_context))
