class Application:
    def get_random_person(self):
        pass

    def get_next_person(self, user):
        person = self.get_random_person()
        while person in user['people_seen']:
            person = self.get_random_person()
        return person