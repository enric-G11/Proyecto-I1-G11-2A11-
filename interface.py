import tkinter as tk
from tkinter import filedialog, messagebox
import graph
from graph import Graph
def load_graph_from_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        global self
        g = graph()
        self.LoadFromFile(filename)
        self.Plot()

def show_example_graph():
    global g
    g = self.CreateGraph_1()
    g.Plot()

def show_custom_graph():
    global self
    g = CreateGraph_2()
    self.Plot()

def show_neighbors():
    if not self.nodes:
        messagebox.showerror("Error", "No graph loaded.")
        return
    node_name = node_entry.get()
    if not any(node.name == node_name for node in g.nodes):
        messagebox.showerror("Error", "Node not found.")
        return
    g.PlotNode(node_name)

# Crear la ventana principal
root = tk.Tk()
root.title("Graph Interface")
root.geometry("400x300")

# Botones para mostrar gráficos
btn_example = tk.Button(root, text="Show Example Graph", command=show_example_graph)
btn_example.pack(pady=10)

btn_custom = tk.Button(root, text="Show Custom Graph", command=show_custom_graph)
btn_custom.pack(pady=10)

btn_load = tk.Button(root, text="Load Graph from File", command=load_graph_from_file)
btn_load.pack(pady=10)

# Entrada para seleccionar nodo
node_entry = tk.Entry(root)
node_entry.pack(pady=10)
btn_neighbors = tk.Button(root, text="Show Neighbors", command=show_neighbors)
btn_neighbors.pack(pady=10)

# Ejecutar la interfaz
g = Graph()
root.mainloop()
