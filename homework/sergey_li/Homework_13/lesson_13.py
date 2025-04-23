import os

base_path = os.path.dirname(__file__)
print(base_path)
file_path = os.path.join(base_path, "data.txt")
print(file_path)
new_path = os.path.join(base_path, "new_file")


def read_file():
    # We create a generator which will open a file using a path to it
    with open(file_path, "r") as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(new_path, "a") as new_file:
        data_line = data_line.replace(".", "").replace(",", "")
        new_file.write(data_line)
