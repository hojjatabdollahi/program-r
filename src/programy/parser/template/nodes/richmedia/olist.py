from programy.utils.logging.ylogger import YLogger

from programy.parser.template.nodes.richmedia.list import TemplateListNode


class TemplateOrderedListNode(TemplateListNode):

    def __init__(self):
        TemplateListNode.__init__(self)

    def resolve_to_string(self, client_context):
        str = "<olist>"
        str += self.resolve_list_items(client_context)
        str += "</olist>"
        return str

    def to_string(self):
        return "[OLIST] %d" % (len(self._items))

