from programy.utils.logging.ylogger import YLogger
from programy.dynamic.variables.variable import DynamicVariable

class GetSentiment(DynamicVariable):

    def __init__(self, config):
        DynamicVariable.__init__(self, config)

    def get_value(self, client_context, value=None):
        userid = client_context.userid
        variables = client_context.bot.conversations[userid].properties
        text = variables["data"]
        try:
            sentiment, sentiment_distribution = client_context.bot.brain.corenlp.get_sentence_sentiment(text)
        except Exception as exception:
            YLogger.exception(self, "sentiment analysis module broke", exception)
            raise exception

        if client_context.bot.facial_expression_recognition is not None:
            if len(client_context.bot.facial_expression_recognition.values):
                last_fer_value = client_context.bot.facial_expression_recognition.last_fer_value


                #the logic of mixing fer and sentiment goes here
                alpha = 0.1
                threshold1 = 0.2
                threshold2 = -0.2
                sentiment_value = self.expected_sentiment_value(sentiment, sentiment_distribution)

                print("FER: ", last_fer_value)
                print("Sentiment:", sentiment_value)

                final_sentiment_value = alpha * last_fer_value + (1-alpha)*sentiment_value
                print("Final sentiment: ", final_sentiment_value)
                if final_sentiment_value > threshold1:
                    sentiment = "positive"
                elif final_sentiment_value < threshold1 and final_sentiment_value > threshold2:
                    sentiment = "neutral"
                else:
                    sentiment = "negative"


        print(sentiment)
        return sentiment

    def expected_sentiment_value(self, sentiment, sentiment_distribution):
        shorten_sentiment_distribution = [sentiment_distribution[0]+sentiment_distribution[1],
                                          sentiment_distribution[2],
                                          sentiment_distribution[3]+ sentiment_distribution[4]]
        value = -shorten_sentiment_distribution[0] + shorten_sentiment_distribution[2]

        return value
