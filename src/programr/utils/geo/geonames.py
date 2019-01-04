import json
import urllib.request

from programr.utils.geo.latlong import LatLong


class GeoNamesApi(object):

    POSTALCODESEARCH = "http://api.geonames.org/postalCodeSearchJSON?postalcode={0}&country={1}&maxRows=10&username={2}"
    get_latlong_for_postcode_response_file = None

    def __init__(self, license_keys):

        if license_keys.has_key('GEO_NAMES_ACCOUNTNAME'):
            self.account_name = license_keys.get_key('GEO_NAMES_ACCOUNTNAME')
        else:
            raise Exception("No valid license key GEO_NAMES_ACCOUNTNAME")

        if license_keys.has_key('GEO_NAMES_COUNTRY'):
            self.country = license_keys.get_key('GEO_NAMES_COUNTRY')
        else:
            raise Exception("No valid license key GEO_NAMES_COUNTRY")

        self.latlong_response_file = None
        if license_keys.has_key('GEONAMES_LATLONG'):
            self.country = license_keys.get_key('GEONAMES_LATLONG')


    def _get_latlong_for_postcode_response(self, postcode):

        if self.latlong_response_file is not None:
            return self.load_get_latlong_for_postcode_from_file(self.latlong_response_file)

        postcode = "".join(postcode.split(" "))
        url = GeoNamesApi.POSTALCODESEARCH.format(postcode, self.country, self.account_name)

        response = urllib.request.urlopen(url)
        if response is None:
            raise Exception("Invalid url: ", url)

        content = response.read()
        if response is None:
            raise Exception("Invalid response from GeoNames")

        return json.loads(content.decode('utf8'))

    def load_get_latlong_for_postcode_from_file(self, filename):
        with open(filename, "w+", encoding="utf-8") as response_file:
            return json.load(response_file)

    def store_get_latlong_for_postcode_to_file(self, postcode, filename):
        content = self._get_latlong_for_postcode_response(postcode)
        with open(filename, "w+", encoding="utf-8") as response_file:
            json.dump(content, response_file, sort_keys=True, indent=2)

    def get_latlong_for_postcode(self, postcode):

        if GeoNamesApi.get_latlong_for_postcode_response_file is None:
            data = self._get_latlong_for_postcode_response(postcode)
        else:
            with open(GeoNamesApi.get_latlong_for_postcode_response_file, "r", encoding="utf-8") as datafile:
                data = json.load(datafile)

        if 'postalCodes' not in data:
            raise Exception("Invalid/Unknown post code")
        if not data['postalCodes']:
            raise Exception("Invalid/Unknown post code")
        if 'lat' not in data['postalCodes'][0] or 'lng' not in data['postalCodes'][0]:
            raise Exception("Invalid/Unknown post code")

        return LatLong(data['postalCodes'][0]['lat'], data['postalCodes'][0]['lng'])
