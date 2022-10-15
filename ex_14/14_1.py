class PartyAnimal:
    x = 0
    name = ""

    def __init__(self,z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("Deleted ", self.name, self.x)


class FootballFan(PartyAnimal):
    point = 0

    def touchdown(self):
        self.point = self.point + 7
        self.party()
        print(self.name, "points", self.point)


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
