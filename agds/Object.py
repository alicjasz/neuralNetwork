class Object:

    def __init__(self):
        self.similarity = 1
        self.attributes = []

    def add_attributes(self, sle_value, swi_value, ple_value, pwi_value, class_value_value):
        self.attributes.append(sle_value)
        self.attributes.append(swi_value)
        self.attributes.append(ple_value)
        self.attributes.append(pwi_value)
        self.attributes.append(class_value_value)

    # def calculate_similarity(self, attr):
    #    self.similarity = 0.2 * attr[0] + 0.2 * attr[1] + 0.2 * attr[2] + 0.2 * attr[3] + 0.2 * attr[4]
