import csv
import numpy as np
import random
from Layer import Layer
from Neuron import Neuron
from Network import Network


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
    # random.shuffle(iris)
    return iris


iris = read_file()
network = Network()
# layer with imputs
layer0 = Layer()
layer1 = Layer()
layer2 = Layer()
layer3 = Layer()

for i in range(4):
    layer0.add_neuron(Neuron())

for i in range(5):
    layer1.add_neuron(Neuron())

for i in range(4):
    layer2.add_neuron(Neuron())

for i in range(3):
    layer3.add_neuron(Neuron())

network.add_layer(layer0)
network.add_layer(layer1)
network.add_layer(layer2)
network.add_layer(layer3)

# creating connections
# for i in range(4):
#    layer0.get_all_neurons()[i].output_value = iris[i]
#    print(str(layer0.get_neuron(i).output_value))

for i in range(len(layer0.neurons)):
    for j in range(len(layer1.neurons)):
        layer0.neurons[i].add_output(layer1.neurons[j])
        layer1.neurons[j].add_input(layer0.neurons[i])

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


def back_propagation():
    for d in iris[0:98]:
        input_values = d[0:4]
        output_values = d[4:7]
        for i in range(len(layer0.neurons)):
            layer0.neurons[i].output_value = input_values[i]

        # for i in range(len(layer0.neurons)):
        #    print("Layer0 neurons output values " + str(layer0.neurons[i].output_value))

        for i in range(len(layer3.neurons)):
            layer3.neurons[i].expected_value = output_values[i]

        # for i in range(len(layer3.neurons)):
        #    print("Layer3 neurons expected values " + str(layer3.neurons[i].expected_value))

        for i in range(len(layer1.neurons)):
            layer1.neurons[i].calculate_weighted_sum()
            layer1.neurons[i].calculate_output_value()
            layer1.neurons[i].transfer_derivative()

        # print("Layer 1: ")
        # for i in range(len(layer1.neurons)):
        #    print("Output value " + str(layer1.neurons[i].output_value) + " weighted sum " + str(layer1.neurons[i].weighted_sum))

        for i in range(len(layer2.neurons)):
            layer2.neurons[i].calculate_weighted_sum()
            layer2.neurons[i].calculate_output_value()
            layer2.neurons[i].transfer_derivative()

        # print("Layer 2: ")
        # for i in range(len(layer2.neurons)):
        #    print("Output value " + str(layer2.neurons[i].output_value) + " weighted sum " + str(layer2.neurons[i].weighted_sum))

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
    for d in iris[98:len(iris)-1]:
        input_data = d[0:4]
        print("Input data " + str(input_data))
        exp_output_data = d[4:7]
        output_table = []

        for i in range(len(layer0.neurons)):
            layer0.neurons[i].output_value = input_data[i]

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
        back_propagation()
    test_network()
