from programy.utils.logging.ylogger import YLogger
from programy.extensions.base import Extension


class SurveyExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):
        YLogger.debug(context, "Survey Storage - Storing data [%s]", data)

        # Data is bar delimited, so you could write to a file, add to a database, or send to another REST service
        for answer in data.split("|"):
            YLogger.debug(context, "Answer = %s", answer.strip())

        return "OK"
