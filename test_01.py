class Person:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def save(self):
        self.db.persist()

    def greet(self):
        return f'Hello, my name is {self.name}'
    
class DB:
    def __init__(self):
        pass

    def persist(self):
        pass
    
class Dog:
    def __init__(self, name):
        self.name = name


from unittest.mock import patch, Mock

@patch('test_01.Dog')
def test_class_called(mockdog):
    name = "doggy"
    instance = Dog(name)
    assert mockdog is Dog
    assert mockdog.called
    assert mockdog.called_once_with(name)

def test_dog_created_instance_name():
    # no need to mock anything if just testing the instance creation
    name = 'doggy'
    dog = Dog(name)
    assert dog.name == name

# combine the two above tests
def test_dog_class_and_instance_name():
    name = "doggy"
    with patch('test_01.Dog') as MockDog:
        # Calling MockDog will return a mock object (instance)
        instance = MockDog.return_value 
        # Set the name attribute of the mock object
        instance.name = name
        # Call Dog => MockDog is called
        dog = Dog(name)
        assert dog.name == name
        assert MockDog.called
        assert MockDog.called_once_with(name)

# Using patch decorator to auto create MockDog
@patch('test_01.Dog')
def test_dog_class_and_instance_name_patch_style(MockDog):
    name = "doggy"
    # Calling MockDog will return a mock object (instance)
    instance = MockDog.return_value 
    # Set the name attribute of the mock object
    instance.name = name
    # Call Dog => MockDog is called
    dog = Dog(name)
    assert dog.name == name
    assert MockDog.called
    assert MockDog.called_once_with(name)



