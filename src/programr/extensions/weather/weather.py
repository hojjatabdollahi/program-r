from programr.utils.logging.ylogger import YLogger
import datetime

from programr.utils.weather.metoffice import MetOffice
from programr.utils.geo.google import GoogleMaps
from programr.extensions.base import Extension


class WeatherExtension(Extension):

    def get_geo_locator(self, context):
        return GoogleMaps()

    def get_met_office(self, license_keys):
        return MetOffice(license_keys)

    # WEATHER [OBSERVATION|FORECAST3|FORECAST24] LOCATION * WHEN *

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):

        splits = data.split()
        if len(splits) != 5:
            YLogger.debug(context, "Weather - Not enough paramters passed, [%d] expected 5", len(splits))
            return None

        type = splits[0]
        if type not in ['OBSERVATION', 'FORECAST5DAY', 'FORECAST24HOUR']:
            YLogger.debug(context, "Weather - Type not understood [%s]", type)
            return None

        if splits[1] == 'LOCATION':
            postcode = splits[2]
        else:
            YLogger.debug(context, "Weather - LOCATION missing")
            return None

        if splits[3] == 'WHEN':
            when = splits[4]
        else:
            YLogger.debug(context, "Weather - WHEN missing")
            return None

        if type == 'OBSERVATION':
            return self.current_observation(context, postcode)
        elif type == 'FORECAST5DAY':
            return self.five_day_forecast(context, postcode, when)
        elif type == 'FORECAST24HOUR':
            return self.twentyfour_hour_forecast(context, postcode, when)

    def current_observation(self, context, postcode):
        YLogger.debug(context, "Getting weather observation for [%s]", postcode)

        googlemaps = self.get_geo_locator(context)
        latlng = googlemaps.get_latlong_for_location(postcode)

        met_office = self.get_met_office(context.client.license_keys)

        observation = met_office.current_observation(latlng.latitude, latlng.longitude)
        if observation is not None:
            #TODO Use 'when" paramter to extract datapoints
            return observation.get_latest_observation().to_program_y_text()
        else:
            return "UNAVAILABLE"

    def twentyfour_hour_forecast(self, context, postcode, when):
        YLogger.debug(context, "Getting 24 hour weather forecast for [%s] at time [%s]", postcode, when)

        googlemaps = self.get_geo_locator(context)
        latlng = googlemaps.get_latlong_for_location(postcode)

        met_office = self.get_met_office(context.client.license_keys)

        forecast = met_office.twentyfour_hour_forecast(latlng.latitude, latlng.longitude)
        if forecast is not None:
            datapoint = forecast.get_forecast_for_n_hours_ahead(int(when))
            if datapoint is None:
                datapoint = forecast.get_latest_forecast().to_program_y_text()
            return datapoint
        else:
            return "UNAVAILABLE"

    def five_day_forecast(self, context, postcode, when):
        YLogger.debug(context, "Getting 5 day forecast for [%s] at time [%s]", postcode, when)

        googlemaps = self.get_geo_locator(context)
        latlng = googlemaps.get_latlong_for_location(postcode)

        met_office = self.get_met_office(context.client.license_keys)

        forecast = met_office.five_day_forecast(latlng.latitude, latlng.longitude)
        if forecast is not None:
            datapoint = forecast.get_forecast_for_n_days_ahead(int(when))
            if datapoint is None:
                datapoint = forecast.get_latest_forecast().to_program_y_text()
            return datapoint
        else:
            return "UNAVAILABLE"

