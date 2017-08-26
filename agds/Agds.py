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

    param = [Attribute("sle"), Attribute("swi"), Attribute("ple"), Attribute("pwi"),
             Attribute("class_value")]

    param[0].nodes = sle
    param[1].nodes = swi
    param[2].nodes = ple
    param[3].nodes = pwi
    param[4].nodes = class_value

    print(param[1].nodes)
    # object to which other objects will be compared
    object_model = Object()
    object_model.add_attributes(float(iris[0][0]), float(iris[0][1]), float(iris[0][2]), float(iris[0][3]), float(iris[0][4]))

    list_of_objects = []

    for i in iris:
        object = Object()
        object.add_attributes(float(i[0]), float(i[1]), float(i[2]), float(i[3]), float(i[4]))
        list_of_objects.append(object)

    for n in range(len(param[0].nodes)):
        print(str(param[0].calculate_weight(param[0].nodes[n])))