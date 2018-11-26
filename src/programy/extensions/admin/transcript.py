from programy.utils.logging.ylogger import YLogger

from programy.extensions.base import Extension


class TranscriptAdminExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, client_context, data):
        YLogger.debug(client_context, "Transcript Admin - [%s]", data)

        show_props = True if data == "PROPERTIES" else False

        transcript = ""

        if client_context.bot.has_conversation(client_context):
            conversation = client_context.bot.conversation(client_context)

            transcript += "Questions:<br /><ul>"
            for question in conversation.questions:
                transcript += "<li>%s - %s</li>"%(question.combine_sentences(), question.combine_answers())
            transcript += "</ul>"
            transcript += "<br />"

            if data == "PROPERTIES":
                transcript += "Properties:<br /><ul>"
                for name, value in conversation.properties.items():
                    transcript += "<li>%s = %s</li>"%(name, value)
                transcript += "</ul>"
                transcript += "<br />"

        else:
            transcript += "No conversation currently available"

        return transcript
