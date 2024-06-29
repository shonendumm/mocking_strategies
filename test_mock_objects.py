class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

from unittest.mock import Mock

def test_method():
    real = ProductionClass()
    real.something = Mock()
    real.method()
    real.something.assert_called_once_with(1, 2, 3)