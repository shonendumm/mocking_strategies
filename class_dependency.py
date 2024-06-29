class DB:
    def __init__(self):
        pass

    def persist(self):
        pass


class Person:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def save(self):
        self.db.persist()

    def greet(self):
        return f'Hello, my name is {self.name}'
    
class Dog:
    def __init__(self, name):
        self.name = name