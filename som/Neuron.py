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
        # self.input_weight = 0.0  # weight for every input neuron (only 1st layer)
        self.expected_value = 0
        self.learning_rate = 0.5

    def find_max_value(self):
        max_val = list()
        for k in self.input_synapses.keys():
            max_val.append(k.output_value)
        return max(max_val)

    def find_min_value(self):
        min_val = list()
        for k in self.input_synapses.keys():
            min_val.append(k.output_value)
        return min(min_val)

    # SOM
    def add_input_neuron(self, neuron, min_value, max_value):
        min_value = (max_value - min_value) / 100
        max_value = (max_value - min_value) / 10
        self.input_synapses[neuron] = random.uniform(min_value, max_value)

    def add_input(self, neuron):
        self.input_synapses[neuron] = random.uniform(-0.1, 0.1)

    def add_output(self, neuron):
        self.output_synapses[neuron] = random.uniform(-0.1, 0.1)

    def calculate_weighted_sum(self):
        self.weighted_sum = 0.0
        for k, v in self.input_synapses.items():
            self.weighted_sum += k.output_value * v
        self.weighted_sum += self.bias

    # sigmoid activation function
    def calculate_output_value(self):
        self.output_value = 1.0 / (1.0 + math.exp(-self.weighted_sum))

    def transfer_derivative(self):
        return self.output_value * (1 - self.output_value)

    def calculate_delta_param(self):
        if len(self.output_synapses) == 0:
            self.delta_param = self.expected_value - self.output_value
        else:
            for k, v in self.output_synapses.items():
                self.delta_param += k.delta_param * v * (1 - k.output_value) * k.output_value

    def update_weight(self):
        for k, v in self.output_synapses.items():
            self.output_synapses[k] = v - self.learning_rate * k.delta_param * (1 - k.output_value) * k.output_value * \
                                          self.output_value
            k.input_synapses[self] = self.output_synapses[k]
