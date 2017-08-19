from math import sqrt

from Node import Node


class Grid:

    def __init__(self, dim):
        self.dim = dim      # size of the grid, dim x dim
        self.grid = []
        self.nodes = []
        self.iteration = 0

    def create_grid(self):
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                node = Node(i,j)
                row.append(node)
                self.nodes.append(node)
            self.grid.append(row)
        # print(self.grid)
        print(self.nodes)

    def fix_winner(self):
        all_distances = dict()
        for row in self.grid:
            for n in row:
                all_distances[n] = n.calculate_distance()
                # all_distances.append(n.calculate_distance())
        return min(all_distances.items(), key=lambda x: x[1])[0]

    def learn_algorithm(self):
        winner = self.fix_winner()
        for row in self.grid:
            for n in row:
                neighbour = sqrt((n.x - winner.x) ** 2 + (n.y - winner.y) ** 2)
                n.update_node_weight(neighbour, self.iteration)
        self.iteration += 1


if __name__ == "__main__":

    grid = Grid(3)
    grid.create_grid()
