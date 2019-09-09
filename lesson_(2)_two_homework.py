import csv


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

columns = ["header1", "header2", "header3", "header4"]


def csv_read():
    type_reader = input("Введите формат записи данных: ")
    with open("notebook/data/read.csv") as file:

        if type_reader == "base":
            reader = csv.reader(file)
        elif type_reader == "dict":
            reader = csv.DictReader(file)
        else:
            print("error")
            return

        for row in reader:
            print(row)


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



