import random
import math


class Neuron:
    def __init__(self):
        self.input_synapses = list()
        self.output_synapses = list()
        self.delta_param = 0
        self.weighted_sum = 0
        self.output_value = 0
        self.bias = 1
        self.input_weight = 0  # weight for every input neuron (only 1st layer)
        self.input_weights = []  # weights which go out the neuron from previous layer
        self.expected_value = 0
        self.learning_rate = 0.1
        self.bias = 0
        self.input_weight = 0  # weight for every input neuron (only 1st layer)
        self.input_weights = []  # weights which go out the neuron from previous layer
        self.expected_value = 0

    def calculate_random_weight(self):
        for i in range(len(self.input_synapses)):
            self.input_synapses[i].input_weights.append(random.randrange(-0.1, 0.1))

    def calculate_weighted_sum(self):
        for i in range(len(self.input_synapses)):
            self.weighted_sum += self.input_synapses[i].output_value * self.input_weights[i]

    # sigmoid activation function
    def calculate_output_value(self):
        self.output_value = 1.0 / (1.0 + math.exp(-self.weighted_sum))

    def transfer_derivative(self):
        return self.output_value * (1 - self.output_value)

    def calculate_delta_param(self):
        if len(self.output_synapses) == 0:
            self.delta_param = self.expected_value - self.output_value
        else:
            for i in range(len(self.output_synapses)):
                self.delta_param += self.output_synapses[i].delta_param * self.input_weights[i] * (
                1 - self.output_value) * self.output_value

    def update_weight(self):
        for i in range(len(self.input_synapses)):
            self.input_weights[i] += self.learning_rate * self.delta_param * (1 - self.output_value) * self.output_value
