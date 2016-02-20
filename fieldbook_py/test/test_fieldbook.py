import unittest

import fieldbook_py


class FieldbookTests(unittest.TestCase):
    def fieldbook_py_is_alive_returns_string(self):
        s = fieldbook_py.alive()
        self.assertTrue(isinstance(s, basestring))

    def fieldbook_py_is_alive(self):
        s = fieldbook_py.alive()
        print(s)
        self.assertEqual(s, "fieldbook_py is alive!")

    def can_instantiate_new_fieldbook_client(self):
        fbc = fieldbook_py.FieldbookClient(
            'api_key',
            'api_secret',
            'url')
        self.assertIsInstance(fbc, fieldbook_py.FieldbookClient)
