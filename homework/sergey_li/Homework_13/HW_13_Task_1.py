import os
import datetime

base_path = os.path.dirname(__file__)
# print(base_path)
homework_path = os.path.dirname(os.path.dirname(base_path))
# print(homework_path)
eugene_file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")
print(eugene_file_path)

with open(eugene_file_path, encoding="utf-8") as eugene_file:
    lines = eugene_file.readlines()

for line in lines:
    parts = line.split()
    if len(parts) < 3:
        continue

    line_number = parts[0].rstrip(".")
    date_str = parts[1]
    date = datetime.datetime.fromisoformat(date_str)

    if line_number == "1":
        new_date = date + datetime.timedelta(days=7)
        print(new_date)
    elif line_number == "2":
        new_date = date.strftime("%A")
        print(new_date)
    elif line_number == "3":
        new_date = datetime.datetime.now() - date
        print(new_date)
