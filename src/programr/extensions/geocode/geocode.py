from programr.utils.logging.ylogger import YLogger

from programr.utils.geo.google import GoogleMaps
from programr.extensions.base import Extension


class GeoCodeExtension(Extension):

    def get_geo_locator(self):
        return  GoogleMaps()

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):
        YLogger.debug(context, "GeoCode [%s]", data)

        words = data.split(" ")
        if words[0] == 'POSTCODE1':
            location = words[1]
        elif words[0] == 'POSTCODE2':
            location = words[1] + words[2]
        elif words[0] == 'LOCATION':
            location = " ".join(words[1:])
        else:
            return None

        googlemaps = self.get_geo_locator()

        latlng = googlemaps.get_latlong_for_location(location)
        if latlng is not None:
            str_lat = str(latlng.latitude)
            str_lng = str(latlng.longitude)

            lats = str_lat.split(".")
            lngs = str_lng.split(".")

            return "LATITUDE DEC %s FRAC %s LONGITUDE DEC %s FRAC %s"%(
                lats[0], lats[1],
                lngs[0], lngs[1]
            )

        return None
