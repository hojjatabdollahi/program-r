import unittest

from programr.dynamic.sets.numeric import IsNumeric
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient

class IsNumericDynamicSetTests(unittest.TestCase):

    def setUp(self):
        self._client_context = ClientContext(TestClient(), "testid")

    def test_isnumeric(self):
        dyn_var = IsNumeric(None)
        self.assertIsNotNone(dyn_var)
        self.assertTrue(dyn_var.is_member(self._client_context, "12345"))
        self.assertFalse(dyn_var.is_member(self._client_context, "ABCDEF"))
        self.assertFalse(dyn_var.is_member(self._client_context, None))
