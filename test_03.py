import unittest
from unittest.mock import patch, Mock, create_autospec, mock_open

def test_open_file():
    with patch('builtins.open', mock_open(read_data='data')) as m:
        with open('foo', 'r') as f:
            result = f.read()
        
        assert result == 'data'
        m.assert_called_once_with('foo', 'r')

