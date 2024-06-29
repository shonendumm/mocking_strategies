# https://www.youtube.com/watch?v=k99HSHQDsi4
import pytest

from person import Person

# Using a fixture helps create it automatically for each test
@pytest.fixture
def person():
    return Person()

# automatically sees that it needs a person fixture, and creates it
def test_greet(person):
    greeting = person.greet()
    assert greeting == "Hello"

# Can auto create the fixture again for another test