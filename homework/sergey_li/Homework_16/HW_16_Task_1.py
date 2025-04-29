import mysql.connector as mysql
import dotenv
import csv
import os

dotenv.load_dotenv()

current_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# print(current_path)
file_path = os.path.join(
    current_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)
file_data = []
with open(file_path, newline="") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        file_data.append(row)

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

cursor = db.cursor(dictionary=True)
query = """
SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sub ON sub.id = l.subject_id
"""
cursor.execute(query)
db_data = cursor.fetchall()
data_dif = []

for row in file_data[1:]:
    file_row = tuple(row)
    found_in_db = False
    for db_row in db_data:
        db_row_tuple = (
            db_row["name"],
            db_row["second_name"],
            db_row["group_title"],
            db_row["book_title"],
            db_row["subject_title"],
            db_row["lesson_title"],
            db_row["mark_value"],
        )
        if file_row == db_row_tuple:
            found_in_db = True
            break

    if not found_in_db:
        data_dif.append(row)

if data_dif:
    for item in data_dif:
        print(item)

cursor.close()
db.close()
