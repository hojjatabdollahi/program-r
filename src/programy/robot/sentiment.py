


class Sentiment():

    def __init__(self):
        self._sentiment_values = []
        self._sentiment_distributions = []
        self._final_sentiment_values = []

    @property
    def values(self):
        return self._sentiment_values

    @property
    def sentiment_distributions(self):
        return self._sentiment_distributions

    @property
    def last_sentiment_value(self):
        return self._sentiment_values[-1]

    @property
    def final_sentiment_values(self):
        return self._final_sentiment_values

    def append_sentiment(self, sentiment):
        self._sentiment_values.append(sentiment)

    def append_sentiment_distribution(self, sentiment_distribution):
        self._sentiment_distributions.append(sentiment_distribution)

    def append_final_sentiment(self, final_sentiment):
        self._final_sentiment_values.append(final_sentiment)

    def expected_sentiment_value(self, sentiment_distribution):
        shorten_sentiment_distribution = [sentiment_distribution[0]+sentiment_distribution[1],
                                          sentiment_distribution[2],
                                          sentiment_distribution[3]+ sentiment_distribution[4]]
        value = -shorten_sentiment_distribution[0] + shorten_sentiment_distribution[2]

        return value


