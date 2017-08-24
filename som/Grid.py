import operator
from math import sqrt

from Neuron import Neuron
from Node import Node


class Grid:
    def __init__(self, dim):
        self.dim = dim  # size of the grid, dim x dim
        self.grid = []
        self.nodes = []
        self.iteration = 0

    def create_grid(self):
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                node = Node(i, j)
                row.append(node)
                self.nodes.append(node)
            self.grid.append(row)

    def fix_winner(self):
        all_distances = []
        for n in self.nodes:
            distance = n.calculate_distance()
            all_distances.append({"dist": distance, "node": n})
        return min(all_distances, key=lambda d: d["dist"])["node"]

    def learn_algorithm(self):
        winner = self.fix_winner()
        for n in self.nodes:
            neighbour = sqrt((n.x - winner.x) ** 2 + (n.y - winner.y) ** 2)
            n.update_node_weight(neighbour, self.iteration)
        self.iteration += 1

