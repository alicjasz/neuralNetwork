import csv
import random
from Layer import Layer
from Neuron import Neuron
from Network import Network


def read_file():
    iris = []
    with open("IrisDataTrain.csv", newline='\n') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            iris.append([float(x.replace(",", ".")) for x in row[0:4]] + [row[4]])
    return iris


iris = read_file()[1]
print(iris)
network = Network()
# layer with imputs
layer0 = Layer()

layer1 = Layer()
layer2 = Layer()
layer3 = Layer()

for i in range(4):
    layer0.add_neuron(Neuron())

# setting weights for input layer
for i in range(4):
    layer0.get_all_neurons()[i].output_value = iris[i]
    print(str(layer0.get_neuron(i).output_value))

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

    for i in range(len(layer2.neurons)):
        layer2.neurons[i].calculate_weighted_sum()
        layer2.neurons[i].calculate_output_value()
        layer2.neurons[i].transfer_derivative()

    print("weighted sum layer2 " + str(layer2.neurons[0].weighted_sum))

    for i in range(len(layer3.neurons)):
        layer3.neurons[i].calculate_weighted_sum()
        layer3.neurons[i].calculate_output_value()
        layer3.neurons[i].transfer_derivative()

    print("weighted sum layer3" + str(layer3.neurons[0].weighted_sum))

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


if __name__ == "__main__":
    for i in range(200):
        back_propagation()

    print("1st neuron matches in 3rd layer " + str(layer3.neurons[0].matched))
    print("2nd neuron matches in 3rd layer " + str(layer3.neurons[1].matched))
    print("3rd neuron matches in 3rd layer " + str(layer3.neurons[2].matched))



