import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from graph import *
from node import *
from segment import *
from test_graph import CreateGraph_1, CreateGraph_2
from path import PlotPath

class GraphInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualizer")
        self.graph = None

        # Títol
        tk.Label(root, text="Graph Visualizer", font=("Impact", 20)).pack(pady=10)

        # Botons per carregar grafos
        tk.Button(root, text="Show Graph 1", width=30, command=self.load_graph1).pack(pady=5)
        tk.Button(root, text="Show Graph 2", width=30, command=self.load_graph2).pack(pady=5)
        tk.Button(root, text="Open Graph from File", width=30, command=self.load_graph_from_file).pack(pady=5)

        # Botons per crear o editar grafos
        tk.Button(root, text="Create Empty Graph", width=30, command=self.create_empty_graph).pack(pady=20)
        tk.Button(root, text="Add Node", width=30, command=self.add_node).pack(pady=5)
        tk.Button(root, text="Add Segment", width=30, command=self.add_segment).pack(pady=5)
        tk.Button(root, text="Delete Node", width=30, command=self.delete_node).pack(pady=5)
        tk.Button(root, text="Save Graph to File", width=30, command=self.save_graph).pack(pady=5)

        # Botó per mostrar veïns
        tk.Button(root, text="Show Neighbors of a Node", width=30, command=self.show_neighbors).pack(pady=20)

        # 🔵 Noves funcionalitats de la versió 2.0
        tk.Button(root, text="Show Reachable Nodes", width=30, command=self.show_reachability).pack(pady=5)
        tk.Button(root, text="Find Shortest Path", width=30, command=self.show_shortest_path).pack(pady=5)

    # Funcions per carregar grafos
    def load_graph1(self):
        self.graph = CreateGraph_1()
        messagebox.showinfo("Graph Loaded", "Graph 1 loaded and plotted.")

    def load_graph2(self):
        self.graph = CreateGraph_2()
        messagebox.showinfo("Graph Loaded", "Graph 2 loaded and plotted.")

    def load_graph_from_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            self.graph = CreateGraphFromFile(filename)
            messagebox.showinfo("Graph Loaded", f"Graph loaded from {filename}")

    # Funcions per editar grafos
    def create_empty_graph(self):
        self.graph = Graph()
        messagebox.showinfo("Graph Created", "An empty graph has been created.")

    def add_node(self):
        if not self.graph:
            messagebox.showerror("Error", "Create or load a graph first.")
            return
        name = simpledialog.askstring("Add Node", "Enter the node name:")
        if not name:
            return
        x = simpledialog.askfloat("Add Node", "Enter x coordinate:")
        y = simpledialog.askfloat("Add Node", "Enter y coordinate:")
        if x is not None and y is not None:
            success = self.graph.AddNode(name, x, y)
            if success:
                messagebox.showinfo("Node Added", f"Node '{name}' added.")
                self.graph.Plot()
            else:
                messagebox.showerror("Error", f"Node '{name}' already exists.")

    def add_segment(self):
        if not self.graph:
            messagebox.showerror("Error", "Create or load a graph first.")
            return
        origin = simpledialog.askstring("Add Segment", "Enter the origin node name:")
        destination = simpledialog.askstring("Add Segment", "Enter the destination node name:")
        if origin and destination:
            success = self.graph.AddSegment(origin, destination)
            if success:
                messagebox.showinfo("Segment Added", f"Segment from '{origin}' to '{destination}' added.")
                self.graph.Plot()
            else:
                messagebox.showerror("Error", "Invalid nodes. Segment not added.")

    def delete_node(self):
        if not self.graph:
            messagebox.showerror("Error", "Create or load a graph first.")
            return
        name = simpledialog.askstring("Delete Node", "Enter the name of the node to delete:")
        if name:
            success = self.graph.DeleteNode(name)
            if success:
                messagebox.showinfo("Node Deleted", f"Node '{name}' deleted.")
                self.graph.Plot()
            else:
                messagebox.showerror("Error", f"Node '{name}' does not exist.")

    def save_graph(self):
        if not self.graph:
            messagebox.showerror("Error", "Create or load a graph first.")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt")])
        if filename:
            self.graph.SaveToFile(filename)
            messagebox.showinfo("Graph Saved", f"Graph saved to {filename}")

    def show_neighbors(self):
        if not self.graph:
            messagebox.showerror("Error", "You must load a graph first.")
            return
        name = simpledialog.askstring("Node Selection", "Enter the name of the node:")
        if name:
            result = self.graph.PlotNode(name)
            if not result:
                messagebox.showerror("Node Not Found", f"Node '{name}' does not exist.")
            else:
                messagebox.showinfo("Node Plot", f"Neighbors of node '{name}' shown.")

    # Versió 2.0 - Reachability
    def show_reachability(self):
        if not self.graph:
            messagebox.showerror("Error", "You must load a graph first.")
            return
        origin = simpledialog.askstring("Reachability", "Enter the origin node:")
        if origin:
            reachable = self.graph.Reachability(origin)
            if not reachable:
                messagebox.showinfo("Result", f"No reachable nodes or node '{origin}' does not exist.")
            else:
                names = ', '.join(sorted([node.name for node in reachable]))
                messagebox.showinfo("Reachability", f"Nodes reachable from '{origin}':\n{names}")

    # Versió 2.0 - Shortest Path (A*)
    def show_shortest_path(self):
        if not self.graph:
            messagebox.showerror("Error", "You must load a graph first.")
            return
        origin = simpledialog.askstring("Shortest Path", "Enter the origin node:")
        destination = simpledialog.askstring("Shortest Path", "Enter the destination node:")
        if origin and destination:
            path = self.graph.FindShortestPath(origin, destination)
            if not path:
                messagebox.showinfo("Result", f"No path found between '{origin}' and '{destination}'.")
            else:
                names = ' -> '.join([node.name for node in path.nodes])
                messagebox.showinfo("Shortest Path", f"Path found:\n{names}")
                PlotPath(self.graph, path)

# Programa principal
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphInterface(root)
    root.mainloop()