from programr.utils.logging.ylogger import YLogger

from programr.utils.geo.google import GoogleMaps
from programr.extensions.base import Extension


class GoogleMapsExtension(Extension):

    def get_geo_locator(self):
        return GoogleMaps()

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):
        YLogger.debug(context, "GoogleMaps [%s]", data)

        splits = data.split(" ")
        command = splits[0]
        from_place = splits[1]
        to_place = splits[2]

        googlemaps = self.get_geo_locator()

        if command == "DISTANCE":
            distance = googlemaps.get_distance_between_addresses(from_place, to_place)
            return self._format_distance_for_programr(distance)
        elif command == "DIRECTIONS":
            directions = googlemaps.get_directions_between_addresses(from_place, to_place)
            return self._format_directions_for_programr(directions)
        else:
            YLogger.error(context, "Unknown Google Maps Extension command [%s]", command)
            return None

    def _format_distance_for_programr(self, distance):
        distance_splits = distance.distance_text.split(" ")
        value = distance_splits[0]
        if "." in value:
            value_splits = distance_splits[0].split(".")
            dec = value_splits[0]
            frac = value_splits[1]
        else:
            dec = value
            frac = "0"
        units = distance_splits[1]
        if units == 'mi':
            units = "miles"
        return "DISTANCE DEC %s FRAC %s UNITS %s"%(dec, frac, units)

    def _format_directions_for_programr(self, directions):
        return "DIRECTIONS %s"%directions.legs_as_a_string()
