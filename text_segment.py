import math  # Importem la llibreria per calcular distàncies


# Definició de la classe Node
class Node:
    def __init__(self, name, x, y):
        """Constructor d'un node amb nom i coordenades (x, y)."""
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        """Representació en forma de text del node."""
        return f"{self.name}({self.x}, {self.y})"


# Definició de la classe Segment
class Segment:
    def __init__(self, origin, destination):
        """Constructor d'un segment entre dos nodes (origen i destinació)."""
        self.origin = origin
        self.destination = destination
        # Calculem la distància euclidiana entre els nodes
        self.cost = math.sqrt((destination.x - origin.x) ** 2 + (destination.y - origin.y) ** 2)

    def __repr__(self):
        """Representació en forma de text del segment, incloent-hi la distància."""
        return f"Segment from {self.origin} to {self.destination} with cost {self.cost:.2f}"


# Creació de nodes
node1 = Node("A", 0, 0)
node2 = Node("B", 3, 4)
node3 = Node("C", 6, 8)

# Creació de segments
segment1 = Segment(node1, node2)
segment2 = Segment(node2, node3)

# Mostrar nodes
print("Nodes:")
print(node1)
print(node2)
print(node3)

# Mostrar segments amb la seva distància
print("\nSegments:")
print(segment1)
print(segment2)