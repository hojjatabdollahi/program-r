from programr.parser.template.nodes.resetlearn import TemplateResetLearnNode
from programr.parser.template.nodes.base import TemplateNode

from programrtest.parser.base import ParserTestsBaseClass

class MockTemplateResetLearnNode(TemplateResetLearnNode):
    def __init__(self):
        TemplateResetLearnNode.__init__(self)

    def resolve_to_string(self, context):
        raise Exception("This is an error")

class TemplateResetLearnNodeTests(ParserTestsBaseClass):

    def test_node(self):
        root = TemplateResetLearnNode()
        self.assertIsNotNone(root)
        self.assertEquals("", root.resolve(self._client_context))

    def test_node_exception_handling(self):
        root = TemplateNode()
        node = MockTemplateResetLearnNode()
        root.append(node)

        result = root.resolve(self._client_context)
        self.assertIsNotNone(result)
        self.assertEquals("", result)

    def test_to_string(self):
        node = MockTemplateResetLearnNode()
        self.assertEquals("RESETLEARN", node.to_string())

    def test_to_xml(self):
        node = TemplateResetLearnNode()
        self.assertEquals("<resetlearn />", node.to_xml(self._client_context))