from unittest.mock import patch
from app import get_next_person

# I want to test get_next_person,
# but it depends on get_random_person
# So I mock get_random_person
@patch('app.get_random_person') 
def test_get_next_person(mock_get_random_person):
    # arrange
    user = {'people_seen': []}
    mock_get_random_person.return_value = 'Person 1'
    # action and assert
    assert get_next_person(user) == 'Person 1'

from model import Application

@patch.object(Application, 'get_random_person') 
def test_get_next_person_class(mock_get_random_person):
    # arrange
    app = Application()
    user = {'people_seen': []}
    expected_person = 'Person 1'
    mock_get_random_person.return_value = expected_person

    # action
    actual_person = app.get_next_person(user)
    # assert
    assert actual_person == expected_person

