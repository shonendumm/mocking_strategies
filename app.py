
def get_random_person():
    pass

def get_next_person(user):
    person = get_random_person()
    while person in user['people_seen']:
        person = get_random_person()
    return person


