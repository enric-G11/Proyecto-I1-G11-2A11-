from node import Node, Distance
from path import Path, AddNodeToPath, ContainsNode, CostToNode, PlotPath
from graph import Graph

# Crear nodes d'exemple
a = Node("A", 0, 0)
b = Node("B", 3, 4)  # distancia AB = 5.0
c = Node("C", 6, 8)  # distancia BC = 5.0
d = Node("D", 10, 10)  # distancia CD = 5.0 aprox

# ===== Test Path class directament =====
print("🔹 Test inicial de Path")

p = Path([a], 0)
print("Path inicial:", [n.name for n in p.nodes], "| Cost:", p.cost)

# AddNodeToPath
print("\n🔹 Test AddNodeToPath")
p2 = AddNodeToPath(p, b, Distance(a, b), Distance(b, d))  # cost real AB + heurística BD
print("Noves nodes:", [n.name for n in p2.nodes])
print("Cost acumulat:", p2.cost)

# ContainsNode
print("\n🔹 Test ContainsNode")
print("Path conté A:", ContainsNode(p2, a))  # True
print("Path conté D:", ContainsNode(p2, d))  # False

# CostToNode
print("\n🔹 Test CostToNode")
print("Cost fins a B:", CostToNode(p2, b))  # Ha de ser 5.0
print("Cost fins a A:", CostToNode(p2, a))  # 0.0
print("Cost fins a D:", CostToNode(p2, d))  # -1 (no hi és)

# ===== Test integrat amb gràfic =====
print("\n🔹 Test gràfic amb PlotPath")

# Crear graf fictici amb els mateixos nodes
G = Graph()
G.AddNode("A", 0, 0)
G.AddNode("B", 3, 4)
G.AddNode("C", 6, 8)
G.AddSegment("A", "B")
G.AddSegment("B", "C")

# Crear un camí real entre A -> B -> C
pa = Path([a, b, c], Distance(a, b) + Distance(b, c))
print("Mostrant gràfic amb PlotPath...")
PlotPath(G, pa)