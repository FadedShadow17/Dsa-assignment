import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread


def create_sample_graph():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 2),
        ("C", "D", 1),
        ("D", "A", 3),
        ("A", "C", 4),
        ("B", "D", 5)
    ])
    return G

class RouteOptimizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Route Optimization")
        self.root.geometry("550x500")
        self.root.configure(bg="#f0f0f0")

        self.G = create_sample_graph()

        self.vehicle_capacity = 10
        self.vehicle_max_distance = 10

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0", foreground="#333")
        style.configure("TButton", font=("Helvetica", 12), padding=6, background="#007bff", foreground="#ffffff")
        style.map("TButton", foreground=[('active', '#ffffff')], background=[('active', '#0056b3')])
        style.configure("TEntry", font=("Helvetica", 12), foreground="#333")
        style.configure("TOptionMenu", font=("Helvetica", 12), foreground="#333")

        container = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        container.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        ttk.Label(container, text="Delivery Points (comma-separated addresses):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.delivery_entry = ttk.Entry(container, width=50)
        self.delivery_entry.grid(row=1, column=0, pady=5)

        ttk.Label(container, text="Vehicle Capacity:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.capacity_entry = ttk.Entry(container, width=20)
        self.capacity_entry.insert(0, "10")
        self.capacity_entry.grid(row=3, column=0, pady=5)

        ttk.Label(container, text="Max Driving Distance:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.distance_entry = ttk.Entry(container, width=20)
        self.distance_entry.insert(0, "10")
        self.distance_entry.grid(row=5, column=0, pady=5)

        ttk.Label(container, text="Select Optimization Algorithm:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.algorithm_var = tk.StringVar(value="Nearest Neighbor")
        algorithms = ["Nearest Neighbor", "Dijkstra", "A*"]
        self.algorithm_menu = ttk.OptionMenu(container, self.algorithm_var, *algorithms)
        self.algorithm_menu.grid(row=7, column=0, pady=5)

        ttk.Button(container, text="Optimize Route", command=self.optimize_route).grid(row=8, column=0, pady=15)

        self.result_area = tk.Text(container, height=10, width=60, bg="#f8f9fa", fg="#333", font=("Helvetica", 12), relief=tk.SOLID, bd=1)
        self.result_area.grid(row=9, column=0, pady=10)

    def optimize_route(self):
        optimization_thread = Thread(target=self._optimize_route_thread)
        optimization_thread.start()

    def _optimize_route_thread(self):
        try:
            delivery_points = self.delivery_entry.get().split(',')
            delivery_points = [point.strip().upper() for point in delivery_points]
            if len(delivery_points) < 2:
                messagebox.showerror("Input Error", "At least two delivery points are required.")
                return

            self.vehicle_capacity = int(self.capacity_entry.get())
            self.vehicle_max_distance = int(self.distance_entry.get())

            algorithm = self.algorithm_var.get()
            path = self.optimize_with_algorithm(algorithm, delivery_points)
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, f"Optimal Path: {path}\n")
            self.visualize_route(path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def optimize_with_algorithm(self, algorithm, nodes):
        if algorithm == "Nearest Neighbor":
            return self.nearest_neighbor_tsp(nodes)
        elif algorithm == "Dijkstra":
            return self.dijkstra_tsp(nodes)
        elif algorithm == "A*":
            return self.astar_tsp(nodes)
        else:
            raise ValueError("Unknown algorithm selected")

    def nearest_neighbor_tsp(self, nodes):
        start = nodes[0]
        path = [start]
        unvisited = set(nodes)
        unvisited.remove(start)

        current = start
        while unvisited:
            next_node = min(unvisited, key=lambda node: self.G[current][node]['weight'])
            path.append(next_node)
            unvisited.remove(next_node)
            current = next_node

        path.append(start)
        return path

    def dijkstra_tsp(self, nodes):
        return self.nearest_neighbor_tsp(nodes)

    def astar_tsp(self, nodes):
        return self.nearest_neighbor_tsp(nodes)

    def visualize_route(self, path):
        plt.clf()
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(self.G, pos, nodelist=path, node_color='lightgreen')
        nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Route Visualization")
        plt.show()

def main():
    root = tk.Tk()
    app = RouteOptimizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
