import csv
import numpy as np
import random
from Layer import Layer
from Neuron import Neuron
from Network import Network
from Grid import Grid


def read_file():
    iris = []
    expected_values = []
    i = 0
    with open("IrisDataTrain.csv", newline='\n') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            if row[4] == "Iris-setosa":
                expected_values = [1.0, 0.0, 0.0]
            elif row[4] == "Iris-versicolor":
                expected_values = [0.0, 1.0, 0.0]
            elif row[4] == "Iris-virginica":
                expected_values = [0.0, 0.0, 1.0]
            iris.append([float(x.replace(",", ".")) for x in row[0:4]] + expected_values)

    return iris


iris = read_file()
network = Network()
# layer with imputs
input_vector = Layer()
layer1 = Layer()
layer2 = Layer()
layer3 = Layer()

for i in range(4):
    input_vector.add_neuron(Neuron())

for i in range(5):
    layer1.add_neuron(Neuron())

for i in range(4):
    layer2.add_neuron(Neuron())

for i in range(3):
    layer3.add_neuron(Neuron())

network.add_layer(input_vector)

network.add_layer(layer1)
network.add_layer(layer2)
network.add_layer(layer3)

# creating connections for MLP layers
for i in range(len(layer1.neurons)):
    for j in range(len(layer2.neurons)):
        layer1.neurons[i].add_output(layer2.neurons[j])
        layer2.neurons[j].add_input(layer1.neurons[i])

for i in range(len(layer2.neurons)):
    for j in range(len(layer3.neurons)):
        layer2.neurons[i].add_output(layer3.neurons[j])
        layer3.neurons[j].add_input(layer2.neurons[i])


# setting weights for the rest of layers, only for testing
# for key, value in layer3.neurons[2].input_synapses.items():
#        print("Key " + str(key) + "value " + str(value))


def som():
    grid = Grid()
    grid.create_grid()
    for d in iris[0:98]:
        input_values = d[0:4]
        output_values = d[4:7]
        # initializing neurons in input vector
        for i in range(len(input_vector.neurons)):
            input_vector.neurons[i].output_value = input_values[i]

        # creating connections between input vector and grid nodes
        for i in range(len(input_vector.neurons)):
            for j in range(len(grid.nodes)):
                grid.nodes[j].add_input(input_vector.neurons[i].output_value)

        # creating connections between grid nodes and layer1
        for i in range(len(grid.nodes)):
            for j in range(len(layer1.neurons)):
                layer1.neurons[j].add_input(grid.nodes[i])  # to change!

        # traing som
        grid.learn_algorithm()

        for i in range(len(layer1.neurons)):
            layer1.neurons[i].calculate_weighted_sum()
            layer1.neurons[i].calculate_output_value()
            layer1.neurons[i].transfer_derivative()

        for i in range(len(layer2.neurons)):
            layer2.neurons[i].calculate_weighted_sum()
            layer2.neurons[i].calculate_output_value()
            layer2.neurons[i].transfer_derivative()

        for i in range(len(layer3.neurons)):
            layer3.neurons[i].calculate_weighted_sum()
            layer3.neurons[i].calculate_output_value()
            layer3.neurons[i].transfer_derivative()

        # print("Layer 3: ")
        # for i in range(len(layer3.neurons)):
        #    print("Output value " + str(
        #        layer3.neurons[i].output_value) + " weighted sum " + str(layer3.neurons[i].weighted_sum))

        # calculating delta_param and updating weights
        # for l in reversed(range(len(network.layers))):
        #    for n in range(len(network.layers[l].neurons)):
        #        print("delta param " + str(network.layers[l].neurons[n].calculate_delta_param()))
        for l in reversed(range(len(network.layers))):
            for n in range(len(network.layers[l].neurons)):
                network.layers[l].neurons[n].calculate_delta_param()

        for l in reversed(range(len(network.layers))):
            # print("Layer " + str(l))
            for n in range(len(network.layers[l].neurons)):
                network.layers[l].neurons[n].update_weight()


def test_network():
    counter = 0
    grid = Grid()
    grid.create_grid()
    for d in iris[0:98]:
        input_values = d[0:4]
        exp_output_data = d[4:7]
        output_table = []

        # initializing neurons in input vector
        for i in range(len(input_vector.neurons)):
            input_vector.neurons[i].output_value = input_values[i]

        # creating connections between input vector and grid nodes
        for i in range(len(input_vector.neurons)):
            for j in range(len(grid.nodes)):
                grid.nodes[j].add_input(input_vector.neurons[i].output_value)

        # creating connections between grid nodes and layer1
        for i in range(len(grid.nodes)):
            for j in range(len(layer1.neurons)):
                layer1.neurons[j].add_input(grid.nodes[i])  # to change!

        # traing som
        grid.learn_algorithm()

        for i in range(len(layer1.neurons)):
            layer1.neurons[i].calculate_weighted_sum()
            layer1.neurons[i].calculate_output_value()
            layer1.neurons[i].transfer_derivative()

        for i in range(len(layer2.neurons)):
            layer2.neurons[i].calculate_weighted_sum()
            layer2.neurons[i].calculate_output_value()
            layer2.neurons[i].transfer_derivative()

        for i in range(len(layer3.neurons)):
            layer3.neurons[i].calculate_weighted_sum()
            layer3.neurons[i].calculate_output_value()
            layer3.neurons[i].transfer_derivative()

        # for i in range(len(layer3.neurons)):
        #    print("Output value " + str(layer3.neurons[i].output_value))

        for i in range(len(layer3.neurons)):
            output_table.append(layer3.neurons[i].output_value)

        index_max = np.argmax(output_table)
        exp_index_max = np.argmax(exp_output_data)

        print("Output table " + str(output_table))
        print("Expected output table " + str(exp_output_data))

        if index_max == exp_index_max:
            print("Indices are the same")
            counter += 1

    result = counter / len(iris[98:len(iris) - 1]) * 100
    print("Result " + str(result))


if __name__ == "__main__":
    for i in range(100):
        som()
    test_network()
