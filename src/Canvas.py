import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import List
import numpy as np

class LeGraph:
    graph: nx.DiGraph
    canvas: FigureCanvasTkAgg
    figure: plt.Figure
    page: tk.Tk
    graph_liste: List[str]

    def __init__(self, liste):
        self.page = tk.Tk()
        self.page.title("Graph Visualization")
        self.page.geometry("825x675")
        self.graph_liste = liste
        self.create_directed_graph()
        self.figure = plt.Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.page)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.draw_graph()
        self.page.mainloop()

    def create_directed_graph(self):
        self.graph = nx.DiGraph()
        self.graph.add_edges_from(self.graph_liste)
        return self.graph

    def draw_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Compute the levels for the shell layout
        pos = self.get_shell_layout()
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16, ax=ax)
        self.canvas.draw()

    def get_shell_layout(self):
        # Determine the level of each node based on the length of its label
        levels = {}
        for node in self.graph.nodes:
            level = len(str(node))
            if level not in levels:
                levels[level] = []
            levels[level].append(node)

        # Create shell layout positions
        pos = {}
        for level, nodes in levels.items():
            num_nodes = len(nodes)
            angle_step = 2 * np.pi / num_nodes
            radius = level  # The radius can be adjusted for spacing
            for i, node in enumerate(nodes):
                angle = i * angle_step
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                pos[node] = (x, y)
                
        return pos