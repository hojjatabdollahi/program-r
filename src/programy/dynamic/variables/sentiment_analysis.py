from programy.utils.logging.ylogger import YLogger
from programy.dynamic.variables.variable import DynamicVariable

class GetSentiment(DynamicVariable):

    def __init__(self, config):
        DynamicVariable.__init__(self, config)

    def get_value(self, client_context, value=None):
        userid = client_context.userid
        variables = client_context.bot.conversations[userid].properties
        bot = client_context.bot
        text = variables["data"]
        try:
            sentiment, sentiment_distribution = bot.brain.corenlp.get_sentence_sentiment(text)
        except Exception as exception:
            YLogger.exception(self, "sentiment analysis module broke", exception)
            raise exception

        sentiment_value = None
        final_sentiment_value = None

        if bot.facial_expression_recognition is not None:
            if len(bot.facial_expression_recognition.values):
                last_fer_value = bot.facial_expression_recognition.last_fer_value


                #the logic of mixing fer and sentiment goes here
                alpha = 0.1
                threshold1 = 0.2
                threshold2 = -0.2
                sentiment_value = bot.sentiment.expected_sentiment_value(sentiment_distribution)


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

        else:
            if sentiment == "positive":
                sentiment_value = 1
                final_sentiment_value = 1
            elif sentiment == "neutral":
                sentiment_value = 0
                final_sentiment_value = 0
            elif sentiment == "negative":
                sentiment_value = -1
                final_sentiment_value = -1


        bot.sentiment.append_sentiment(sentiment_value)
        bot.sentiment.append_sentiment_distribution(sentiment_distribution)
        bot.sentiment.append_final_sentiment(final_sentiment_value)


        print(sentiment)
        return sentiment
