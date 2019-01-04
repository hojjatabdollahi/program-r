import unittest

from programr.dynamic.variables.datetime import GetTime
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient

class GetTimeDynamicVarTests(unittest.TestCase):

    def setUp(self):
        self._client_context = ClientContext(TestClient(), "testid")

    def test_gettime(self):
        dyn_var = GetTime(None)
        self.assertIsNotNone(dyn_var)
        time = dyn_var.get_value(self._client_context)
        self.assertIsNotNone(time)

