import csv


def read_file():
    iris = []
    expected_values = []
    i = 0
    with open("IrisDataTrain.csv", newline='\n') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            if row[4] == "Iris-setosa":
                expected_values = [1.0]
            elif row[4] == "Iris-versicolor":
                expected_values = [2.0]
            elif row[4] == "Iris-virginica":
                expected_values = [3.0]
            iris.append([float(x.replace(",", ".")) for x in row[0:4]] + expected_values)
    return iris