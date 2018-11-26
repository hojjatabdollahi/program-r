class ParserException(Exception):
    def __init__(self, message, filename=None, xml_exception=None, xml_element=None):
        Exception.__init__(self, message)
        self._message = message
        self._filename = filename
        self._xml_exception = xml_exception
        self._xml_element = xml_element

    @property
    def message(self):
        return self._message

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @property
    def xml_exception(self):
        return self._xml_exception

    @xml_exception.setter
    def xml_exception(self, xml_exception):
        self._xml_exception = xml_exception

    @property
    def xml_element(self):
        return self._xml_element

    @xml_element.setter
    def xml_element(self, xml_element):
        self._xml_element = xml_element

    def format_message(self):
        msg = self._message

        if self._filename is not None:
            msg += " in [%s]" % self._filename

        if self._xml_exception is not None:
            if isinstance(self._xml_exception, str):
                msg += " : "
                msg += self._xml_exception
            else:
                msg += " at [line(%d), column(%d)]" % (self._xml_exception.position[0],
                                                       self._xml_exception.position[1])

        if self._xml_element is not None:
            if hasattr(self._xml_element, '_end_line_number') and hasattr(self._xml_element, '_end_column_number'):
                msg += " at [line(%d), column(%d)]" % (self._xml_element._end_line_number,
                                                       self._xml_element._end_column_number)
        return msg


class DuplicateGrammarException(ParserException):
    def __init__(self, message, filename=None, xml_exception=None, xml_element=None):
        ParserException.__init__(self, message, filename=filename, xml_exception=xml_exception, xml_element=xml_element)


class MatcherException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message
