import xml.etree.ElementTree as ET


class OutOfBandProcessor(object):

    def __init__(self):
        self._xml = None

    # Override this method to extract the data for your command
    # See actual implementations for details of how to do this
    def parse_oob_xml(self, oob: ET.Element):
        self._xml = oob
        return True

    # Override this method in your own class to do something
    # useful with the command data
    def execute_oob_command(self, client_context):
        return ""

    def process_out_of_bounds(self, client_context, oob: ET.Element):
        if self.parse_oob_xml(oob) is True:
            return self.execute_oob_command(client_context)
        return ""
