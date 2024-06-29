import pytest

class Person:
    def greet(self):
        return "Hello"

# Using a fixture helps create it automatically for each test
@pytest.fixture
def person():
    return Person()

# automatically sees that it needs a person fixture, and creates it
def test_greet(person):
    greeting = person.greet()
    assert greeting == "Hello"

# Can auto create the fixture again for another test