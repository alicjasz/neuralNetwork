import csv
import numpy as np
from Layer import Layer
from Neuron import Neuron
from Network import Network


def read_file():
    iris = []
    expected_values = []
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
print(iris)
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
for i in range(50):
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
    # calculating all parameters
    for i in range(len(layer1.neurons)):
        layer1.neurons[i].calculate_weighted_sum()
        layer1.neurons[i].calculate_output_value()
        layer1.neurons[i].transfer_derivative()

    for i in range(len(layer1.neurons)):
        print("Output value " + str(layer1.neurons[i].output_value))

    for i in range(len(layer2.neurons)):
        layer2.neurons[i].calculate_weighted_sum()
        layer2.neurons[i].calculate_output_value()
        layer2.neurons[i].transfer_derivative()

    print("weighted sum layer2 " + str(layer2.neurons[0].weighted_sum))
    for i in range(len(layer2.neurons)):
        print("Output value " + str(layer2.neurons[i].output_value))

    for i in range(len(layer3.neurons)):
        layer3.neurons[i].calculate_weighted_sum()
        layer3.neurons[i].calculate_output_value()
        layer3.neurons[i].transfer_derivative()

    print("weighted sum layer3" + str(layer3.neurons[0].weighted_sum))
    for i in range(len(layer3.neurons)):
        print("Output value " + str(layer3.neurons[i].output_value))

    # calculating delta_param and updating weights
    # for l in reversed(range(len(network.layers))):
    #    for n in range(len(network.layers[l].neurons)):
    #        print("delta param " + str(network.layers[l].neurons[n].calculate_delta_param()))
    for l in reversed(range(len(network.layers))):
        print("Layer " + str(l))
        for n in range(len(network.layers[l].neurons)):
            network.layers[l].neurons[n].calculate_delta_param()
            print("Delta param " + str(network.layers[l].neurons[n].delta_param))

    for l in reversed(range(len(network.layers))):
        print("Layer " + str(l))
        for n in range(len(network.layers[l].neurons)):
            for k, v in network.layers[l].neurons[n].output_synapses.items():
                print("Before improvements: " + str(v))
            network.layers[l].neurons[n].update_weight()
            for k, v in network.layers[l].neurons[n].output_synapses.items():
                print("Improved weight: " + str(v))


def test_network():
    counter = 0
    input_data = read_file()[75][0:4]
    print(input_data)
    exp_output_data = read_file()[75][4:7]
    print(exp_output_data)
    output_table = []
    for i in range(len(layer3.neurons)):
        output_table.append(layer3.neurons[i].output_value)
    index_max = np.argmax(output_table)

    exp_index_max = np.argmax(exp_output_data)

    if index_max == exp_index_max:
        counter += 1

    result = float(counter) / 200
    print("Counter " + str(counter) + " result " + str(result))

if __name__ == "__main__":
    back_propagation()
    test_network()




