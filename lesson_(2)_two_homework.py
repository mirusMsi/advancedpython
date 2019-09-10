import csv
import json
from pprint import pprint
import yaml


data_list = [
    ["header1", "header2", "header3", "header4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"],
    ["data1", "data2", "data3", "data4"]
]

data_dict = [
    {"header1": "data1", "header2": "data2", "header3": "data3", "header4": "data4"},
    {"header1": "data1", "header2": "data2", "header3": "data3", "header4": "data4"},
    {"header1": "data1", "header2": "data2", "header3": "data3", "header4": "data4"},
    {"header1": "data1", "header2": "data2", "header3": "data3", "header4": "data4"},
    {"header1": "data1", "header2": "data2", "header3": "data3", "header4": "data4"},
    {"header1": "data1", "header2": "data2", "header3": "data3", "header4": "data4"}
]

data_yaml = {
    'attr1': 'value1',
    'attr2': 'value2',
    'attr3': 'value3',
    'attr4': ['value1', 'value2', 'value3']
}

columns = ["header1", "header2", "header3", "header4"]


def csv_read():
    type_reader = input("Введите формат чтения данных: ")
    csv_read_answer = []
    with open("notebook/data/read.csv") as file:

        if type_reader == "base":
            reader = csv.reader(file)
        elif type_reader == "dict":
            reader = csv.DictReader(file)
        else:
            print("error")
            return

        for row in reader:
            csv_read_answer.append(row)

        return csv_read_answer


def csv_write(need_data, headers):
    type_writer = input("Введите формат записи данных: ")
    with open("notebook/data/write.csv", "w") as file:

        if type_writer == "base":
            writer = csv.writer(file)
        elif type_writer == "dict":
            writer = csv.DictWriter(file, fieldnames = headers)
            writer.writeheader()
        else:
            print("error")
            return

        for row in need_data:
            writer.writerow(row)


def json_read():
    json_read_answer = []
    with open("notebook/data/read.json") as file:
        json_read_answer = json.load(file)

    return json_read_answer


def json_write(need_data):
    with open("notebook/data/write.json", "w") as file:
        json.dump(need_data, file, indent = 4)


def yaml_read():
    yaml_read_answer = []
    with open("notebook/data/read.yml") as file:
        ppyaml_read_answer = yaml.safe_load(file)

    return yaml_read_answer


def yaml_write(need_data):
    with open("notebook/data/write.yml", "w") as file:
        yaml.safe_dump(need_data, file)


my_object = yaml_read()

for row in my_object:
    pprint(row)
