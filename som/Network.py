class Network:

    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def get_layer(self, num):
        return self.layers[num]