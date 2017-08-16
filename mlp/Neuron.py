import random
import math


class Neuron:

    def __init__(self):
        self.input_synapses = dict()
        self.output_synapses = dict()
        self.delta_param = 0
        self.weighted_sum = 0
        self.output_value = 0
        self.bias = 1
        self.input_weight = 0.0  # weight for every input neuron (only 1st layer)
        # self.input_weights = []  # weights which go out the neuron from previous layer
        self.expected_value = 0.1
        self.learning_rate = 0.2
        self.matched = 0

    # do zmiany, nie moze tak byc, bo sie w zyciu nie nauczy!
    def add_input(self, neuron):
        self.input_synapses[neuron] = random.uniform(-0.1, 0.1)

    def add_output(self, neuron):
        self.output_synapses[neuron] = random.uniform(-0.1, 0.1)

    def calculate_weighted_sum(self):
        self.weighted_sum = 0
        for k, v in self.input_synapses.items():
            self.weighted_sum = self.weighted_sum + k.output_value * v

    # sigmoid activation function
    def calculate_output_value(self):
        self.output_value = 1.0 / (1.0 + math.exp(-self.weighted_sum))

    def transfer_derivative(self):
        return self.output_value * (1 - self.output_value)

    def calculate_delta_param(self):
        if len(self.output_synapses) == 0:
            self.delta_param = self.expected_value - self.output_value
            print("calculated delta param: " + str(self.delta_param))
            if self.delta_param < 0.2:
                self.matched += 1
        else:
            for k, v in self.output_synapses.items():
                self.delta_param += k.delta_param * v * (1 - k.output_value) * k.output_value

    def update_weight(self):
        for k, v in self.output_synapses.items():
            self.output_synapses[k] = v - self.learning_rate * k.delta_param * (1 - k.output_value) * k.output_value * \
                                          self.output_value
            k.input_synapses[self] = self.output_synapses[k]