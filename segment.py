import math

class Segment:
    def __init__(self, name, origin, destination):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        return math.sqrt((self.destination.x - self.origin.x) ** 2 + (self.destination.y - self.origin.y) ** 2)

    def __repr__(self):
        return (f"Segment '{self.name}' from {self.origin} to {self.destination} "
                f"with cost {self.cost:.2f}")
