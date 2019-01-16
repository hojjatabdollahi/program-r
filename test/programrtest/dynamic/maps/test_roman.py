import unittest

from programr.dynamic.maps.roman import MapDecimalToRoman
from programr.dynamic.maps.roman import MapRomanToDecimal
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class IsRomanNumeralDynamicSetTests(unittest.TestCase):

    def setUp(self):
        self._client_context = ClientContext(TestClient(), "testid")

    def test_romantodec(self):
        dyn_map = MapRomanToDecimal(None)
        self.assertIsNotNone(dyn_map)
        self.assertEquals("20", dyn_map.map_value(self._client_context, "XX"))
        self.assertEquals("4", dyn_map.map_value(self._client_context, "IV"))

    def test_dectoroman(self):
        dyn_map = MapDecimalToRoman(None)
        self.assertIsNotNone(dyn_map)
        self.assertEquals("XX", dyn_map.map_value(self._client_context, "20"))
        self.assertEquals("IV", dyn_map.map_value(self._client_context, "4"))
