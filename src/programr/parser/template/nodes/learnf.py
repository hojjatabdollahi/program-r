from programr.utils.logging.ylogger import YLogger
import os
import xml.etree.ElementTree as ET

from programr.parser.template.nodes.learn import TemplateLearnNode


class TemplateLearnfNode(TemplateLearnNode):

    def __init__(self):
        TemplateLearnNode.__init__(self)

    def resolve_to_string(self, client_context):
        for category in self.children:
            new_node = self._create_new_category(client_context, category)
            self.write_learnf_to_file(client_context, new_node)
        return ""

    def resolve(self, client_context):
        try:
            return self.resolve_to_string(client_context)
        except Exception as excep:
            YLogger.exception(client_context, "Failed to resolve", excep)
            return ""

    def to_string(self):
        return "LEARNF"

    def to_xml(self, client_context):
        xml = "<learnf>"
        xml += self.children_to_xml(client_context)
        xml += "</learnf>"
        return xml

    @staticmethod
    def create_learnf_path(client_context):
        return "%s%s%s.aiml"%(client_context.brain.configuration.defaults.learnf_path, os.sep, client_context.userid)

    @staticmethod
    def create_learn_file_if_missing(client_context, learnf_path):

        if os.path.exists(client_context.brain.configuration.defaults.learnf_path) is False:
            os.mkdir(client_context.brain.configuration.defaults.learnf_path)

        if os.path.isfile(learnf_path) is False:
            file = open(learnf_path, "w+", encoding="utf-8")
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<aiml>\n')
            file.write('</aiml>\n')
            file.close()

    @staticmethod
    def create_category_xml_node(client_context, category)   :
        # Add our new element
        child = ET.Element("category")
        child.append(category.pattern)
        child.append(category.topic)
        child.append(category.that)
        child.append(category.template.xml_tree(client_context))
        return child

    @staticmethod
    def write_node_to_learnf_file(client_context, node):

        learnf_path = TemplateLearnfNode.create_learnf_path(client_context)

        TemplateLearnfNode.create_learn_file_if_missing(client_context, learnf_path)

        YLogger.debug(client_context, "Writing learnf to %s", learnf_path)

        tree = ET.parse(learnf_path)
        root = tree.getroot()
        root.append(node)
        tree.write(learnf_path, method="xml")

    def write_learnf_to_file(self, client_context, category):

        node = TemplateLearnfNode.create_category_xml_node(client_context, category)

        TemplateLearnfNode.write_node_to_learnf_file(client_context, node)
