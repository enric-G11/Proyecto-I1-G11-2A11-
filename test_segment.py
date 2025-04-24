from node import *
from segment import *

# Creació de nodes
node1 = Node("A", 0, 0)
node2 = Node("B", 3, 4)
node3 = Node("C", 6, 8)

# Creació de segments
segment1 = Segment("AB" , node1, node2)
segment2 = Segment("BC", node2, node3)

# Mostrar nodes
print("Nodes:")
print(node1)
print(node2)
print(node3)

# Mostrar segments amb la seva distància
print("\nSegments:")
print(segment1)
print(segment2)