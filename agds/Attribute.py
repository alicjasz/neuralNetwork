class Attribute:

    def __init__(self, name):
        self.name = name
        self.nodes = dict()  # keys -> params form file, # values -> weights
        self.nodes_keys = list(self.nodes.keys())
        # self.x_value = 0
        self.conn_weight = 0

    def add_x_value(self, node):
        self.nodes[node] = 0

    def calculate_min_value(self):
        min_value = []
        for i in self.nodes.keys():
            min_value.append(i)
        return min(min_value)

    def calculate_max_value(self):
        max_value = []
        for i in self.nodes.keys():
            max_value.append(i)
        return max(max_value)

    def calculate_weight(self):
        temp = self.nodes_keys[0]
        min_val = self.calculate_min_value()
        max_val = self.calculate_max_value()
        for k in self.nodes_keys[1:]:
            self.nodes[k] = 1 - abs(temp - k) / (max_val - min_val)
            # print("nodes[k] " + str(self.nodes[k]))
            temp = k
        # print(str(self.nodes))



