import csv


def read_file():
    iris = []
    with open("IrisDataTrain.csv", newline='\n') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            iris.append([float(x.replace(",", ".")) for x in row[0:4]] + [row[4]])
    return iris


if __name__ == "__main__":
    print(read_file())