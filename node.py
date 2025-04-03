import math
from tkinter.font import names

class Node:
    def __init__ (self, name:str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = [] #Llista de nodes veïns


def AddNeighbor(n1, n2):
    if n2 in n1.neighbors:
        return False
    else:
        n1.neighbors.append(n2)
        return True

def Distance(n1, n2):
    return math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)