import unittest
import tempfile
import os
import sys
from pathlib import Path

# Add the server directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Server')))

from server import StringSearchServer

class TestStringSearchServer(unittest.TestCase):

    def setUp(self):
        # Create a temporary file and write test data
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.write(b"hello\nworld\n")
        self.test_file.close()

        # Create a temporary config file
        self.test_config = tempfile.NamedTemporaryFile(delete=False, mode='w')
        self.test_config.write(f"""
        [DEFAULT]
        Port = 12345
        linuxpath = {self.test_file.name}
        REREAD_ON_QUERY = True
        [SSL]
        enabled = False
        certfile =
        keyfile =
        """)
        self.test_config.close()

        self.server = StringSearchServer(self.test_config.name)

    def tearDown(self):
        os.remove(self.test_file.name)
        os.remove(self.test_config.name)

    def test_search_string_exists(self):
        self.assertTrue(self.server.search_string_in_file("hello"))

    def test_search_string_not_exists(self):
        self.assertFalse(self.server.search_string_in_file("goodbye"))

if __name__ == '__main__':
    unittest.main()
