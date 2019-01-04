from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
import json


class TemplateRestNode(TemplateNode):

    def __init__(self):
        TemplateNode.__init__(self)

    def resolve_to_string(self, client_context):
        result = self.resolve_children_to_string(client_context)
        resolved = "NIL"
        if result != "":
            try:
                data = json.loads(result)
                if isinstance(data, list):
                    if len(data) > 1:
                        resolved = json.dumps(data[1:])
                else:
                    raise Exception("Not what I wanted")
            except Exception as e:
                words = result.split(" ")
                if words:
                    if len(words) > 1:
                        resolved = " ".join(words[1:])

        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), resolved)
        return resolved

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "REST"

    def to_xml(self, client_context):
        xml = "<rest>"
        xml += self.children_to_xml(client_context)
        xml += "</rest>"
        return xml

    #######################################################################################################
    # <implode>ABC</implode>

    def parse_expression(self, graph, expression):
        self._parse_node(graph, expression)
