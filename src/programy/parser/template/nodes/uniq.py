from programy.utils.logging.ylogger import YLogger

from programy.utils.text.text import TextUtils
from programy.parser.template.nodes.triple import TemplateTripleNode

class TemplateUniqNode(TemplateTripleNode):

    def __init__(self, subj=None, pred=None, obj=None):
        TemplateTripleNode.__init__(self, node_name="uniq", subj=subj, pred=pred, obj=obj)

    def resolve_to_string(self, client_context):
        rdf_subject = self._subj.resolve(client_context).upper()
        rdf_predicate = self._pred.resolve(client_context).upper()
        rdf_object = self._obj.resolve(client_context)

        results = client_context.brain.rdf.match_only_vars(rdf_subject, rdf_predicate, rdf_object)

        values = []
        for result in results:
            for pair in result:
                if pair[1] not in values:
                    values.append(pair[1])

        resolved = ""
        if values:
            resolved = " ".join(values)

        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "UNIQ"

    def to_xml(self, client_context):
        xml = "<uniq>"
        xml += self.children_to_xml(client_context)
        xml += "</uniq>"
        return xml
