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


from unittest.mock import patch, Mock, create_autospec

@patch('test_01.Dog')
def test_class_called(mockdog): # mockdog is specced as Dog
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



def function(a, b, c):
    pass

def test_autospec():
    # Create a mock object with the same signature as function
    mock_function = create_autospec(function)
    # Call the mock object with the correct arguments
    mock_function(1, 2, 3)
    # Assert that the call was successful
    mock_function.assert_called_once_with(1, 2, 3)

# If a class is used as a spec then the return value of the mock (the instance of the class) will have the same spec. 
def test_autospec_with_class():
    mock_dog = create_autospec(Dog)
    dog = mock_dog('doggy')
    assert isinstance(dog, Dog)
    # assert dog.name == 'doggy' # This will fail because the mock object does not have the name attribute. Have to set it manually, like below.

# create_autospec(Dog) creates a mock object with the same signature as the Dog class but does not instantiate a real Dog object.
# When you call mock_dog('doggy'), it does not call the actual __init__ method of the Dog class and does not set the name attribute.

def test_autospec_with_class_manual():
    mock_dog = create_autospec(Dog)
    mock_instance = mock_dog.return_value
    mock_instance.name = 'doggy'

    dog = mock_dog('doggy')
    assert isinstance(dog, Dog)
    assert dog.name == 'doggy'

@patch('test_01.Dog', autospec=True)
def test_autospec_with_class_autospec(mock_dog):
    # Set the instance returned by the mock constructor
    mock_instance = mock_dog.return_value
    mock_instance.name = 'doggy'
    
    # Create an instance of Dog using the mock
    dog = Dog('doggy')
    
    # Verify that the constructor was called with the correct argument
    mock_dog.assert_called_once_with('doggy')
    assert dog.name == 'doggy'


class SomeClass:
    @classmethod
    def class_method(cls, arg):
        pass

# Use patch.object to mock a class method
@patch.object(SomeClass, 'class_method')
def test(mock_method):
    # call the original method
    SomeClass.class_method(3)
    # verify that the method was called with the correct argument
    mock_method.assert_called_with(3)


from unittest.mock import sentinel

class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

def test_same_object_with_sentinel():
    real = ProductionClass()
    real.method = Mock(name='method') #name is optional
    # monkey patch method (replace func method on the class) to return sentinel.fixed_value
    real.method.return_value = sentinel.fixed_value #  The sentinel attributes now preserve their identity when they are copied or pickled.
    result = real.method()
    assert result == sentinel.fixed_value