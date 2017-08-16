class Layer:

    def __init__(self):
        self.neurons = []

    def add_neuron(self, neuron):
        self.neurons.append(neuron)

    def remove_neuron(self, neuron):
        self.neurons.remove(neuron)

    def get_all_neurons(self):
        return self.neurons

    def get_neuron(self, num):
        return self.neurons[num]
