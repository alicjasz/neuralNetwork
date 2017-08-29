import Parser
from Attribute import Attribute
from Object import Object


def delete_repetition(param_list):
    checked = []
    for e in param_list:
        if e not in checked:
            checked.append(e)
    return checked


def add_value(param_list, value):
    param_list.append(value)


if __name__ == "__main__":

    iris = Parser.read_file()
    sle_attr = Attribute("sle")
    swi_attr = Attribute("swi")
    ple_attr = Attribute("ple")
    pwi_attr = Attribute("pwi")
    class_value_attr = Attribute("class_value")

    sle = list()
    swi = list()
    ple = list()
    pwi = list()
    class_value = list()

    for row in range(len(iris)):
        add_value(sle, iris[row][0])
        add_value(swi, iris[row][1])
        add_value(ple, iris[row][2])
        add_value(pwi, iris[row][3])
        add_value(class_value, iris[row][4])

    sle = delete_repetition(sle)
    swi = delete_repetition(swi)
    ple = delete_repetition(ple)
    pwi = delete_repetition(pwi)
    class_value = delete_repetition(class_value)

    sle.sort()
    swi.sort()
    ple.sort()
    pwi.sort()
    class_value.sort()

    for i in sle:
        sle_attr.add_x_value(i)

    for i in swi:
        swi_attr.add_x_value(i)

    for i in ple:
        ple_attr.add_x_value(i)

    for i in pwi:
        pwi_attr.add_x_value(i)

    for i in class_value:
        class_value_attr.add_x_value(i)

    ''''
    sle_keys = list(sle_attr.nodes.keys())
    sle_attr.calculate_weight(sle_keys)

    swi_keys = list(swi_attr.nodes.keys())
    swi_attr.calculate_weight(swi_keys)

    ple_keys = list(ple_attr.nodes.keys())
    ple_attr.calculate_weight(ple_keys)

    pwi_keys = list(pwi_attr.nodes.keys())
    pwi_attr.calculate_weight(pwi_keys)

    class_value_keys = list(class_value_attr.nodes.keys())
    class_value_attr.calculate_weight(class_value_keys)
    '''
    print(len(sle_attr.nodes))
    dupa = list(sle_attr.nodes.keys())
    sle_attr.calculate_weight()
    object_model = Object()
    object_model.add_attributes(float(iris[0][0]), float(iris[0][1]), float(iris[0][2]), float(iris[0][3]), float(iris[0][4]))

    list_of_objects = []

    for i in iris:
        object = Object()
        object.add_attributes(float(i[0]), float(i[1]), float(i[2]), float(i[3]), float(i[4]))
        # print("sle " + str(i[0]))
        list_of_objects.append(object)

    tab = []
    param = [sle_attr, swi_attr, ple_attr, pwi_attr, class_value_attr]

    for i in list_of_objects:
        x = param[0].nodes[i.attributes[0]]
        # print("sle " + str(i.attributes[0]))
        tab.append(x)

        x = i.attributes[1]
        # print("swi " + str(x))
        tab.append(x)

        x = i.attributes[2]
        # print("ple " + str(x))
        tab.append(x)

        x = i.attributes[3]
        # print("pwi " + str(x))
        tab.append(x)

        x = i.attributes[4]
        # print("class " + str(x))
        tab.append(x)




