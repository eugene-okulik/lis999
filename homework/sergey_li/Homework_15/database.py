import mysql.connector as mysql

# set connection to mysql database
db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port="25060",
    database="st-onl",
)

# operator that helps to work with a database
cursor = db.cursor(dictionary=True)

# this will convert database data to python dict format
# cursor doesn't save results. it returns only the latest data requested and we need to extract it before next request
# cursor.execute("SELECT * FROM students")
# data = cursor.fetchall()  # to read all the requested data
# for student in data:
#     print(student["second_name"])

# cursor.execute("SELECT * FROM students WHERE id = 2")
# data2 = cursor.fetchone()  # reads only one when you requested 1 item

# this structure with %s will secure your bd from injections
query = "SELECT * FROM students WHERE name = %s and second_name = %s"
cursor.execute(query, (input("name"), input("second_name")))
print(cursor.fetchall())

# request to insert data to a database
query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ("Vasia", "Pupkin")
cursor.execute(query, values)

db.close()
