from path import PlotPath
from graph import *
from node import *
from segment import *

def CreateGraph_1():
    G = Graph()
    # Afegim nodes amb les seves coordenades
    G.AddNode("A", 1, 20)
    G.AddNode("B", 8, 17)
    G.AddNode("C", 15, 20)
    G.AddNode("D", 18, 15)
    G.AddNode("E", 2, 4)
    G.AddNode("F", 6, 5)
    G.AddNode("G", 12, 12)
    G.AddNode("H", 10, 3)
    G.AddNode("I", 19, 1)
    G.AddNode("J", 13, 5)
    G.AddNode("K", 3, 15)
    G.AddNode("L", 4, 10)
    G.AddSegment("A", "B")
    G.AddSegment("A", "E")
    G.AddSegment("A", "K")
    G.AddSegment("B", "A")
    G.AddSegment("B", "C")
    G.AddSegment("B", "F")
    G.AddSegment("B", "K")
    G.AddSegment("B", "G")
    G.AddSegment("C", "D")
    G.AddSegment("C", "G")
    G.AddSegment("D", "G")
    G.AddSegment("D", "H")
    G.AddSegment("D", "I")
    G.AddSegment("E", "F")
    G.AddSegment("F", "L")
    G.AddSegment("G", "B")
    G.AddSegment("G", "F")
    G.AddSegment("G", "H")
    G.AddSegment("I", "D")
    G.AddSegment("I", "J")
    G.AddSegment("J", "I")
    G.AddSegment("K", "A")
    G.AddSegment("K", "L")
    G.AddSegment("L", "K")
    G.AddSegment("L", "F")

    G.Plot()
    return G

def CreateGraph_2():
    G = Graph()

    # Afegir nodes al grafo
    G.AddNode("X", 0, 0)
    G.AddNode("Y", 3, 4)
    G.AddNode("Z", 5, 12)
    G.AddNode("W", 8, 15)
    G.AddNode("V", 10, 18)
    G.AddSegment("X", "Y")
    G.AddSegment("Y", "Z")
    G.AddSegment("Z", "W")
    G.AddSegment("W", "V")
    G.AddSegment("X", "W")
    G.AddSegment("Y", "V")

    G.Plot()
    return G

if __name__ == "__main__":
    G1 = CreateGraph_1()
    G2 = CreateGraph_2()
    G3 = CreateGraphFromFile("data.txt")

    # Test GetClosest on G1
    print("Closest node to (5, 5) in G1:")
    closest_node = G1.GetClosest(5, 5)
    if closest_node:
        print(f" -> {closest_node.name} at ({closest_node.x}, {closest_node.y})")

    # Test GetClosest on G2
    print("Closest node to (6, 14) in G2:")
    closest_node = G2.GetClosest(6, 14)
    if closest_node:
        print(f" -> {closest_node.name} at ({closest_node.x}, {closest_node.y})")

    # Test PlotNode on G1
    print("Plotting neighbors of node 'B' in G1:")
    G1.PlotNode("B")

    # Test PlotNode on G2
    print("Plotting neighbors of node 'Y' in G2:")
    G2.PlotNode("Y")

    # Test PlotNode with a node that doesn't exist
    print("Trying to plot non-existent node 'Zz' in G1:")
    result = G1.PlotNode("Zz")
    if not result:
        print(" -> Node 'Zz' not found.")

    G = CreateGraph_1()

    print("\n🔎 Testing GetClosest (5,5):")
    closest = G.GetClosest(5, 5)
    print(f"Closest node to (5,5): {closest.name} ({closest.x}, {closest.y})")

    print("\n🌐 Testing Reachability from node 'D':")
    reachable = G.Reachability("D")
    if reachable:
        print("Nodes reachable from D:", ', '.join(sorted([n.name for n in reachable])))
    else:
        print("Node D not found.")

    print("\n📍 Testing Shortest Path from 'B' to 'F':")
    shortest = G.FindShortestPath("B", "F")
    if shortest:
        print("Shortest path found:", ' -> '.join([n.name for n in shortest.nodes]))
        PlotPath(G, shortest)
    else:
        print("No path found from B to F.")

    print("\n📍 Testing Shortest Path from 'A' to 'I':")
    shortest2 = G.FindShortestPath("A", "I")
    if shortest2:
        print("Shortest path found:", ' -> '.join([n.name for n in shortest2.nodes]))
        PlotPath(G, shortest2)
    else:
        print("No path found from A to I.")