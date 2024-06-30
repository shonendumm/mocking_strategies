class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self, times):
        return "Woof!" * times

import unittest
from unittest.mock import create_autospec

class TestDog(unittest.TestCase):
    def setUp(self):
        # Setup code, runs before each test method
        self.dog_name = 'Fido'
        self.dog_instance = Dog(self.dog_name)

    def test_dog_instance_with_autospec(self):
        # Create an autospec mock for the Dog instance
        mock_dog = create_autospec(self.dog_instance, instance=True)

        # Enforce method signature
        mock_dog.bark(3)  # This should work fine
        with self.assertRaises(TypeError):
            mock_dog.bark()  # This should raise a TypeError

        # Manually set attributes
        mock_dog.name = self.dog_name

        # Verify the attributes
        self.assertEqual(mock_dog.name, self.dog_name)

    def tearDown(self):
        # Teardown code, runs after each test method
        pass

if __name__ == '__main__':
    unittest.main()
