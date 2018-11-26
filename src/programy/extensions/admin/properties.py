from programy.utils.logging.ylogger import YLogger

from programy.extensions.base import Extension
from programy.parser.template.nodes.get import TemplateGetNode
from programy.parser.template.nodes.bot import TemplateBotNode

class PropertiesAdminExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, client_context, data):
        YLogger.debug(client_context, "Properties Admin - [%s]", data)

        properties = ""

        splits = data.split()
        if splits[0] == 'GET':

            if splits[1] == 'BOT':
                properties = TemplateBotNode.get_bot_variable(client_context, splits[2])

            elif splits[1] == "USER":
                local = bool(splits[2].upper == 'LOCAL')
                properties = TemplateGetNode.get_property_value(client_context, local, splits[3])

        elif splits[0] == 'BOT':
            properties += "Properties:<br /><ul>"
            for pair in client_context.brain.properties.pairs:
                properties += "<li>%s = %s</li>"%(pair[0], pair[1])
            properties += "</ul>"
            properties += "<br />"

        elif splits[0] == "USER":
            if client_context.bot.has_conversation(client_context):
                conversation = client_context.bot.conversation(client_context)

                properties += "Properties:<br /><ul>"
                for name, value in conversation.properties.items():
                    properties += "<li>%s = %s</li>"%(name, value)
                properties += "</ul>"
                properties += "<br />"

            else:
                properties += "No conversation currently available"

        return properties
