import unittest

from programr.config.container import BaseContainerConfigurationData


class BaseContainerConfigurationDataTests(unittest.TestCase):

    def test_init(self):

        container = BaseContainerConfigurationData("container")
        self.assertEquals(container.section_name, "container")
        with self.assertRaises(NotImplementedError):
            container.load_configuration(None, None)