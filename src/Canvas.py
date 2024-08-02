import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import List

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

        # Use a spring layout or another suitable layout
        pos = nx.spring_layout(self.graph, seed=42, k=0.3, iterations=50)

        # Draw the nodes and edges with customizations
        nx.draw(self.graph, pos, with_labels=True, node_color='red', edge_color='black',
                node_size=2000, font_size=16, ax=ax, arrows=True, arrowsize=20)

        # Draw the graph on the canvas
        self.canvas.draw()