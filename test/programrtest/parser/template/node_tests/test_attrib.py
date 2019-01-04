from programr.parser.template.nodes.attrib import TemplateAttribNode

from programrtest.parser.base import ParserTestsBaseClass

######################################################################################################################
#
class TemplateAttribTests(ParserTestsBaseClass):

    def test_node(self):
        attrib = TemplateAttribNode()
        self.assertIsNotNone(attrib)
        with self.assertRaises(Exception):
            attrib.set_attrib("Something", "Other")
