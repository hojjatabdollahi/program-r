from programr.parser.exceptions import ParserException
from programr.parser.pattern.nodes.base import PatternNode


class PatternTemplateNode(PatternNode):

    def __init__(self, template, userid='*'):
        PatternNode.__init__(self, userid)
        self._template = template

    @property
    def template(self):
        return self._template

    def is_template(self):
        return True

    def can_add(self, new_node):
        if new_node.is_root():
            raise ParserException("Cannot add root node to template node")
        elif new_node.is_topic():
            raise ParserException("Cannot add topic node to template node")
        elif new_node.is_that():
            raise ParserException("Cannot add that node to template node")
        elif new_node.is_template():
            raise ParserException("Cannot add template node to template node")

    def to_xml(self, client_context, include_user=False):
        string = ""
        if include_user is True:
            string += '<template userid="%s">'%self.userid
        else:
            string += '<template>'
        string2 = super(PatternTemplateNode, self).to_xml(client_context, include_user)
        string += string2
        string += '</template>\n'
        return string

    def to_string(self, verbose=True):
        if verbose is True:
            return "PTEMPLATE [%s] [%s]" %(self.userid, self._child_count(verbose))
        return "PTEMPLATE"

    def equivalent(self, other):
        if other.is_template():
            if self.userid == other.userid:
                return True
        return False

