import pytest
from unittest.mock import patch, Mock, create_autospec, mock_open

def test_open_file():
    with patch('builtins.open', mock_open(read_data='data')) as m:
        with open('foo', 'r') as f:
            result = f.read()
        
        assert result == 'data'
        m.assert_called_once_with('foo', 'r')

# need to name the input same as the args
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), pytest.param("6+9", 42, marks=pytest.mark.xfail)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    # first 2 pass, last fails

