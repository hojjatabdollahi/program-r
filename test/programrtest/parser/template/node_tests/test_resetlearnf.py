
from programr.parser.template.nodes.resetlearnf import TemplateResetLearnfNode

from programrtest.parser.base import ParserTestsBaseClass
from programr.parser.template.nodes.base import TemplateNode

class MockTemplateResetLearnfNode(TemplateResetLearnfNode):
    def __init__(self):
        TemplateResetLearnfNode.__init__(self)

    def resolve_to_string(self, context):
        raise Exception("This is an error")


class TemplateResetLearnfNodeTests(ParserTestsBaseClass):

    def test_node(self):
        root = TemplateResetLearnfNode()
        self.assertIsNotNone(root)
        self.assertEquals("", root.resolve(self._client_context))

    def test_node_exception_handling(self):
        root = TemplateNode()
        node = MockTemplateResetLearnfNode()
        root.append(node)

        result = root.resolve(self._client_context)
        self.assertIsNotNone(result)
        self.assertEquals("", result)

    def test_to_string(self):
        node = TemplateResetLearnfNode()
        self.assertEquals("RESETLEARNF", node.to_string())

    def test_to_xml(self):
        node = TemplateResetLearnfNode()
        self.assertEquals("<resetlearnf />", node.to_xml(self._client_context))