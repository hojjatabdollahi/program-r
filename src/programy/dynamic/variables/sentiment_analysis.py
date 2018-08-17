from programy.dynamic.variables.variable import DynamicVariable
from programy.utils.text.dateformat import DateFormatter


class GetSentiment(DynamicVariable):

    def __init__(self, config):
        DynamicVariable.__init__(self, config)

    def get_value(self, client_context, value=None):
        variables = client_context.bot.conversations["Console"].properties
        text = variables["data"]
        sentiment, sentiment_value = client_context.bot.brain.corenlp.get_sentence_sentiment(text)

        # sentiments, sentiment_values = client_context.bot.brain.corenlp.get_sentence_sentiments(text)
        #
        # sentiment = sentiments[sentiment_values.index(max(sentiment_values))]
        # print(sentiment)

        return sentiment
