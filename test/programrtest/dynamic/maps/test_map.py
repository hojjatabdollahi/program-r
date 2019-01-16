import unittest

from programr.dynamic.maps.map import DynamicMap
from programr.config.brain.brain import BrainDynamicsConfiguration


class DynamicMapTests(unittest.TestCase):

    def test_init(self):
        config = BrainDynamicsConfiguration()
        map = DynamicMap(config)
        self.assertIsNotNone(map)
        self.assertIsNotNone(map.config)
        self.assertEqual(config, map.config)

        with self.assertRaises(Exception):
            map.map_value(None, None, None)