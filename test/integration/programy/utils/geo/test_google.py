import unittest
import os

from programr.utils.geo.google import GoogleMaps, GoogleDistance, GoogleDirections
from programr.utils.geo.latlong import LatLong

#############################################################################
#

class GoogleMapsTests(unittest.TestCase):

    def test_location(self):
        googlemaps = GoogleMaps(None)

        latlng = googlemaps.get_latlong_for_location("KY3 9UR")
        self.assertIsNotNone(latlng)
        self.assertIsInstance(latlng, LatLong)
        self.assertEquals(latlng.latitude, 56.0720397)
        self.assertEquals(latlng.longitude, -3.1752001)

    def test_distance_uk_driving_imperial(self):
        googlemaps = GoogleMaps(None)

        distance = googlemaps.get_distance_between_addresses("Edinburgh", "London", country="UK", mode="driving", units="imperial")
        self.assertIsNotNone(distance)
        self.assertIsInstance(distance, GoogleDistance)
        self.assertEquals("409 mi", distance._distance_text)

    def test_directions(self):
        googlemaps = GoogleMaps(None)

        directions = googlemaps.get_directions_between_addresses("Edinburgh", "London")
        self.assertIsNotNone(directions)
        self.assertIsInstance(directions, GoogleDirections)

