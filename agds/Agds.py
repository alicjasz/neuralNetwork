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

    object_model = Object()
    object_model.add_attributes(float(iris[2][0]), float(iris[2][1]), float(iris[2][2]), float(iris[2][3]),
                                float(iris[2][4]))

    list_of_objects = []

    for i in iris:
        object = Object()
        object.add_attributes(float(i[0]), float(i[1]), float(i[2]), float(i[3]), float(i[4]))
        # print("sle " + str(i[0]))
        list_of_objects.append(object)

    tab = []
    param = [sle_attr, swi_attr, ple_attr, pwi_attr, class_value_attr]

    for i in list_of_objects:
        a1 = i.attributes[0]
        tab1 = param[0].calculate_weight(object_model.attributes[0], a1)

        a2 = i.attributes[1]
        tab2 = param[1].calculate_weight(object_model.attributes[1], a2)

        a3 = i.attributes[2]
        tab3 = param[2].calculate_weight(object_model.attributes[2], a3)

        a4 = i.attributes[3]
        tab4 = param[3].calculate_weight(object_model.attributes[3], a4)

        a5 = i.attributes[4]
        tab5 = param[4].calculate_weight(object_model.attributes[4], a5)

        y = tab1 * 0.2 + tab2 * 0.2 + tab3 * 0.2 + tab4 * 0.2 + tab5 * 0.2
        tab.append(y)

    print(str(tab))



