from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.triple import TemplateTripleNode
from programy.parser.exceptions import ParserException


class TemplateDeleteTripleNode(TemplateTripleNode):

    def __init__(self, subj=None, pred=None, obj=None):
        TemplateTripleNode.__init__(self, node_name="deletetriple", subj=subj, pred=pred, obj=obj)

    def resolve_to_string(self, client_context):
        rdf_subject = self._subj.resolve(client_context)
        rdf_predicate = self._pred.resolve(client_context)
        rdf_object = self._obj.resolve(client_context)

        resolved = ""
        client_context.brain.rdf.delete_entity(rdf_subject, rdf_predicate, rdf_object)
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "DELETETRIPLE"

    def to_xml(self, client_context):
        xml = "<deletetriple>"
        xml += self.children_to_xml(client_context)
        xml += "</deletetriple>"
        return xml

    #######################################################################################################
    # DELETETRIPLE_EXPRESSION ::== <deletetriple>TEMPLATE_EXPRESSION</deletetriple>

    def parse_expression(self, graph, expression):
        super(TemplateDeleteTripleNode, self).parse_expression(graph, expression)

        if self._subj is None:
            raise ParserException("<%s> node missing subject attribue/element"%self.node_name)

        if  self._pred is None:
            YLogger.debug(self, "<%s> node missing predicate attribue/element", self.node_name)

        if self._obj is None:
            YLogger.debug(self, "<%s> node missing object attribue/element", self.node_name)
