from pyowm import OWM

from programr.utils.logging.ylogger import YLogger
from programr.services.service import Service


class WeatherAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key

    # Get the current weather at a given location.
    # Location is a string of the form 'Denver, CO'
    def weather(self, location):
        return OWM(self.api_key).weather_at_place(location)


class WeatherService(Service):

    def __init__(self, config=None, api=None):
        Service.__init__(self, config)

        api_key = 'b42dab02ba31304c08ae33bd9c63d0a4'

        if api is None:
            self._api = WeatherAPI(api_key)
        else:
            self._api = api

    def get_weather_info(self, observation):
        weather = observation.get_weather()
        return weather.get_temperature(unit='fahrenheit')

    def ask_question(self, client_context, question: str):
        try:
            words  = question.split()
            question = " ".join(words[1:])
            if words[0] == 'WEATHER':
                observation = self._api.weather(question)
                search = str(self.get_weather_info(observation)['temp'])
                search += ' degrees fahrenheit'
                YLogger.debug(client_context, f"weather report: {search}")
            # elif words[0] == 'SEARCH':
            #     results = self._api.search(question)
            #     search = ", ".join(results)
            else:
                YLogger.error(client_context, "Unknown Open Weather Map command [%s]", words[0])
                search = ""
            return search
        except Exception as ex:
            YLogger.error(client_context, "General error querying Open Weather Map for question [%s]", question)
            YLogger.error(client_context, f"Exception message: {ex}")
        return ""