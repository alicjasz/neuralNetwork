from math import sqrt, exp

from Neuron import Neuron


class Node(Neuron):
    def __init__(self, x, y):
        self.x = x  # x position in the grid
        self.y = y  # y position in the grid
        self.input_synapses = dict()
        self.output_synapses = dict()
        self.distance = 0.0
        self.learning_rate = 1  # initial
        self.const_of_narrowing = 1000
        self.weight = 0
        self.radius = self.x  # the grid will be always a square
        # param for assigning neighbourhood
        self.output_value = 0

    def calculate_distance(self):
        for k, v in self.input_synapses.items():
            self.distance += (k.output_value - v) ** 2
        self.distance = sqrt(self.distance)
        self.output_value = self.distance
        return self.distance

    # neighbour - distance between winner and each node in the grid
    def update_node_weight(self, iteration, neighbour):
        self.radius *= exp(-iteration / self.const_of_narrowing)
        self.learning_rate *= exp(-iteration / self.const_of_narrowing)
        for k, v in self.input_synapses.items():
            delta = exp(-(neighbour ** 2 / 2 * (self.radius ** 2)))
            self.input_synapses[k] = v + delta * self.learning_rate * (k.output_value - v)
