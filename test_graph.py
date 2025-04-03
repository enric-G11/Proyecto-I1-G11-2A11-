from graph import *


def CreateGraph_1():
    """Crea i retorna el primer graf per provar."""
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

    # Afegim segments entre nodes
    edges = [
        ("A", "B"), ("A", "E"), ("A", "K"), ("B", "C"), ("B", "F"),
        ("B", "G"), ("C", "D"), ("C", "G"), ("D", "G"), ("D", "H"),
        ("E", "F"), ("G", "F"), ("G", "H"), ("I", "J"), ("J", "I"),
        ("K", "A"), ("K", "L"), ("L", "F")
    ]

    for edge in edges:
        G.AddSegment(*edge)

    return G


def CreateGraph_2():
    """Crea i retorna un segon graf amb nodes i segments diferents."""
    G = Graph()

    # Afegir nodes al grafo
    G.AddNode("X", 0, 0)
    G.AddNode("Y", 3, 4)
    G.AddNode("Z", 5, 12)
    G.AddNode("W", 8, 15)
    G.AddNode("V", 10, 18)

    # Afegir segments (conexions entre nodes)
    G.AddSegment("X", "Y")
    G.AddSegment("Y", "Z")
    G.AddSegment("Z", "W")
    G.AddSegment("W", "V")
    G.AddSegment("X", "W")
    G.AddSegment("Y", "V")

    # Mostrar el grafo
    G.Plot()

    return G  # Retorna el graf creat


def CreateGraphFromFile(filename):
    """Crea un graf llegint les dades des d'un fitxer."""
    G = Graph()

    try:
        G.LoadFromFile(filename)
    except FileNotFoundError:
        print(f"Error: El fitxer '{filename}' no s'ha trobat.")

    return G


''''''
# PROVES DELS GRAFS
print("🔹 Provant CreateGraph_1()")
G1 = CreateGraph_1()
G1.Plot()

print("🔹 Provant CreateGraph_2()")
G2 = CreateGraph_2()
print("🔹 Provant CreateGraphFromFile('data.txt')")
G3 = CreateGraphFromFile("data.txt")
G3.Plot()
'''
# --- TEST DEL GRAF ---
print("Probando el grafo...")

# Creem el graf mitjançant la funció CreateGraph_1
G = CreateGraph_1()

# --- 1. Mostrar el graf complet ---
print("Mostrant el graf complet...")
G.Plot()  # Dibuixa tots els nodes i segments

# --- 2. Mostrar el node C i els seus veïns ---
print("Mostrant el node 'C' i els seus veïns...")
G.PlotNode("C")  # Dibuixa el node "C" amb els seus veïns destacats

# --- 3. Buscar el node més proper a un punt donat ---
print("Buscant el node més proper a (15,5)...")
n = G.GetClosest(15, 5)
print(f"El node més proper a (15,5) és: {n.name}")  # Ha de ser "J"

print("Buscant el node més proper a (8,19)...")
m = G.GetClosest(8, 19)
print(f"El node més proper a (8,19) és: {m.name}")  # Ha de ser "B"
'''