

class PersonModel:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.work = ""
        self.AddressModel = ""


class AddressModel:

    def __init__(self, street, dist, state, pin):
        self.street = street
        self.dist = dist
        self.state = state
        self.pin = pin


        