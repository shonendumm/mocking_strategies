import pytest
from unittest.mock import Mock, patch
from class_dependency import Person, DB, Dog

@pytest.fixture
def mock_db():
    # returns a mock object that acts like DB
    return Mock(spec=DB)


def test_greet(mock_db):
    soo = Person('SOO', mock_db)
    soo.save()
    mock_db.persist.assert_called_once()


def test_person_creation():
    # Create a mock db object since we don't care about it
    mock_db = Mock(spec=DB)
    # Create an instance of Person
    person = Person('SOO', mock_db)

    # Check if the name is set correctly
    assert person.name == 'SOO'
    # Check if the db is set correctly
    assert person.db == mock_db


def test_person_creation_option_two(mock_db):
    # Create an instance of Person
    person = Person('SOO', mock_db)

    # Check if the name is set correctly
    assert person.name == 'SOO'
    # Check if the db is set correctly
    assert person.db == mock_db




# https://docs.python.org/3/library/unittest.mock-examples.html#mocking-classes
def test_dog_creation_instance_name():
    name = 'SOO'
    with patch('class_dependency.Dog') as MockDog:
        instance = MockDog.return_value
        instance.name = name
        dog = Dog(name)
        assert dog.name == name
    
    
def test_person_creation_with_args(mock_db):
    # Create a mock for Person.__init__
    mock_init = Mock(return_value=None)

    # Patch Person.__init__ with the mock
    with patch.object(Person, '__init__', mock_init):
        name = 'SOO'
        instance = Person(name, mock_db)

        # Assert that Person.__init__ was called once with the correct arguments
        mock_init.assert_called_once_with(name, mock_db)

        # Additional assertions on the created instance
        # assert instance.name == name #these will fail, need to use another method to test
        # assert instance.db == mock_db

    name = 'Alice'
    # Create an instance of Person with mock_db
    created_person = Person(name, mock_db)
    assert created_person.name == name
    assert created_person.db == mock_db

def test_person_creation_with_args():
    # Only mock the dependencies of Person
    mock_db = Mock(spec=DB) # or pass in the fixture
    name = 'Alice'

    # Create an instance of Person with mock_db
    created_person = Person(name, mock_db)

    assert created_person.name == name
    assert created_person.db == mock_db


