import matplotlib.pyplot as plt
import math
import heapq
from node import *
from segment import *
from path import Path, AddNodeToPath, ContainsNode, Distance
from matplotlib.patches import FancyArrowPatch  # Import for arrows

# Classe que representa un graf
class Graph:
    def __init__(self):
        self.nodes = {}  # Diccionari {nom_node: Node}
        self.segments = []  # Llista de segments

    def AddNode(self, name, x=0, y=0):
        if name in self.nodes:
            return False
        self.nodes[name] = Node(name, x, y)
        return True

    def AddSegment(self, nameOriginNode, nameDestinationNode):
        if nameOriginNode not in self.nodes or nameDestinationNode not in self.nodes:
            return False
        origin = self.nodes[nameOriginNode]
        destination = self.nodes[nameDestinationNode]
        name = nameOriginNode + nameDestinationNode
        segment = Segment(name, origin, destination)
        self.segments.append(segment)

        AddNeighbor(origin, destination)
        return True

    def Plot(self):
        """Dibuixa el graf amb nodes i segments (ara com a fletxes)"""
        plt.figure(figsize=(8, 6))

        # Dibuixar segments com a fletxes
        for segment in self.segments:
            # Crear una fletxa des del node origen al node destinació
            arrow = FancyArrowPatch((segment.origin.x, segment.origin.y),
                                    (segment.destination.x, segment.destination.y),
                                    mutation_scale=15, color='black', arrowstyle='->')
            plt.gca().add_patch(arrow)

            # Afegir el cost a la meitat del segment
            plt.text((segment.origin.x + segment.destination.x) / 2,
                     (segment.origin.y + segment.destination.y) / 2,
                     f'{segment.cost:.2f}', color='red')

        # Dibuixar nodes
        for node in self.nodes.values():
            plt.scatter(node.x, node.y, color='gray')
            plt.text(node.x, node.y, node.name, fontsize=12, ha='right')

        plt.show()

    def GetClosest(self, x, y):
        closest_node = None
        min_distance = float('inf')
        for node in self.nodes.values():
            distance = math.hypot(node.x - x, node.y - y)
            if distance < min_distance:
                min_distance = distance
                closest_node = node
        return closest_node

    def PlotNode(self, nameOrigin):
        if nameOrigin not in self.nodes:
            return False
        origin = self.nodes[nameOrigin]
        neighbors = origin.neighbors
        plt.figure(figsize=(8, 6))
        for segment in self.segments:
            if (segment.origin == origin and segment.destination in neighbors) or \
                    (segment.destination == origin and segment.origin in neighbors):
                plt.plot([segment.origin.x, segment.destination.x],
                         [segment.origin.y, segment.destination.y], 'r-')
                plt.text((segment.origin.x + segment.destination.x) / 2,
                         (segment.origin.y + segment.destination.y) / 2,
                         f'{segment.cost:.2f}', color='red')
            else:
                plt.plot([segment.origin.x, segment.destination.x],
                         [segment.origin.y, segment.destination.y], 'k-')
        for node in self.nodes.values():
            if node == origin:
                plt.scatter(node.x, node.y, color='blue')
            elif node in neighbors:
                plt.scatter(node.x, node.y, color='green')
            else:
                plt.scatter(node.x, node.y, color='gray')
            plt.text(node.x, node.y, node.name, fontsize=12, ha='right')
        plt.show()
        return True

    def DeleteNode(self, name):
        if name not in self.nodes:
            return False
        self.segments = [seg for seg in self.segments if seg.origin.name != name and seg.destination.name != name]
        for node in self.nodes.values():
            node.neighbors = [n for n in node.neighbors if n.name != name]
        del self.nodes[name]
        return True

    def SaveToFile(self, filename):
        with open(filename, "w") as f:
            for node in self.nodes.values():
                f.write(f"{node.name} {node.x} {node.y}\n")
            for segment in self.segments:
                f.write(f"{segment.origin.name} {segment.destination.name}\n")

    def IsReachable(self, nameOrigin, nameDestination):
        if nameOrigin not in self.nodes or nameDestination not in self.nodes:
            return False
        visited = set()
        to_visit = [self.nodes[nameOrigin]]
        while to_visit:
            current = to_visit.pop()
            if current.name == nameDestination:
                return True
            visited.add(current)
            for neighbor in current.neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return False

    def Reachability(self, start_node_name):
        if start_node_name not in self.nodes:
            return None
        start_node = self.nodes[start_node_name]
        reachable_nodes = set()
        visited = set()
        self._dfs_reachability(start_node, visited, reachable_nodes)
        return reachable_nodes

    def _dfs_reachability(self, node, visited, reachable_nodes):
        if node.name in visited:
            return
        visited.add(node.name)
        reachable_nodes.add(node)
        for neighbor in node.neighbors:
            self._dfs_reachability(neighbor, visited, reachable_nodes)

    def FindShortestPath(self, origin_name, destination_name):
        if origin_name not in self.nodes or destination_name not in self.nodes:
            return None
        origin = self.nodes[origin_name]
        destination = self.nodes[destination_name]
        current_paths = []
        start_path = Path([origin], 0)
        estimated = Distance(origin, destination)
        heapq.heappush(current_paths, (estimated, start_path))
        while current_paths:
            _, current_path = heapq.heappop(current_paths)
            last_node = current_path.LastNode()
            if last_node == destination:
                return current_path
            for neighbor in last_node.neighbors:
                if ContainsNode(current_path, neighbor):
                    continue
                segment_cost = Distance(last_node, neighbor)
                estimated_remaining = Distance(neighbor, destination)
                new_path = AddNodeToPath(current_path, neighbor, segment_cost, estimated_remaining)
                total_cost = new_path.cost + estimated_remaining
                heapq.heappush(current_paths, (total_cost, new_path))
        return None

def CreateGraphFromFile(filename):
    f = open(filename, "r")
    G = Graph()
    lineas = [line.strip() for line in f.readlines()]
    f.close()
    for i in range(len(lineas)):
        partes = lineas[i].split(" ")
        if len(partes) == 3:
            G.AddNode(partes[0], eval(partes[1]), eval(partes[2]))
        elif len(partes) == 2:
            G.AddSegment(partes[0], partes[1])
    G.Plot()
    return G
