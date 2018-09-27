from programy.dynamic.variables.variable import DynamicVariable
from programy.utils.text.dateformat import DateFormatter


class GetSentiment(DynamicVariable):

    def __init__(self, config):
        DynamicVariable.__init__(self, config)

    def get_value(self, client_context, value=None):
        variables = client_context.bot.conversations["Console"].properties
        text = variables["data"]
        sentiment, sentiment_distribution = client_context.bot.brain.corenlp.get_sentence_sentiment(text)

        last_fer_value = client_context.bot.facial_expression_recognition.last_fer_value

        #the logic of mixing fer and sentiment goes here
        alpha = 0.8
        threshold = 0.5
        sentiment_value = self.expected_sentiment_value(sentiment, sentiment_distribution)

        final_sentiment_value = alpha * last_fer_value + (1-alpha)*sentiment_value

        if final_sentiment_value > threshold:
            sentiment = "positive"
        else:
            sentiment = "negative"



        return sentiment

    def expected_sentiment_value(self, sentiment, sentiment_distribution):
        shorten_sentiment_distribution = [sentiment_distribution[0]+sentiment_distribution[1],
                                          sentiment_distribution[2],
                                          sentiment_distribution[3]+ sentiment_distribution[4]]
        value = -shorten_sentiment_distribution[0] + shorten_sentiment_distribution[2]

        return value
