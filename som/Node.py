from Neuron import Neuron


class Node(Neuron):

    def __init__(self, x, y):
        self.x = x          # x position in the grid
        self.y = y          # y position in the grid
        self.inputs = []