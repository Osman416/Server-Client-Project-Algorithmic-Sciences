import unittest
from unittest.mock import patch
import sys
import os

# Add the client directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Client')))

import client

class TestClient(unittest.TestCase):

    @patch('builtins.input', return_value='hello')
    @patch('socket.socket')
    def test_send_query_to_server(self, mock_socket, mock_input):
        mock_socket_instance = mock_socket.return_value.__enter__.return_value
        mock_socket_instance.recv.return_value = b'STRING EXISTS\n'
        response = client.send_query_to_server('localhost', 12345)
        self.assertEqual(response, 'STRING EXISTS')

if __name__ == '__main__':
    unittest.main()
