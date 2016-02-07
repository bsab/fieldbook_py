from unittest import TestCase

import fieldbook_py


class TestAlive(TestCase):
    def fieldbook_py_is_alive_returns_string(self):
        s = fieldbook_py.alive()
        self.assertTrue(isinstance(s, basestring))

    def fieldbook_py_is_alive(self):
        s = fieldbook_py.alive()
        print(s)
        self.assertEqual(s, "fieldbook_py is alive!")
