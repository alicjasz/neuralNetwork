class Object:

    def __init__(self):
        self.similarity = 1
        self.attributes = []

    def add_attributes(self, sle, swi, ple, pwi, class_value):
        self.attributes.append(sle)
        self.attributes.append(swi)
        self.attributes.append(ple)
        self.attributes.append(pwi)
        self.attributes.append(class_value)

