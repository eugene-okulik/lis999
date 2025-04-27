import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port="25060",
    database="st-onl",
)

cursor = db.cursor(dictionary=True)

# 1. To create a new student
cursor.execute(
    "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL)",
    ("Tester", "QA"),
)
student_id = cursor.lastrowid
print(f"Student ID: {student_id}")

# 2. To create a new group
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("SEA109", "Apr 2025", "Jun 2025"),
)
group_id = cursor.lastrowid
print(f"Group ID: {group_id}")

# 3. To assign the student to the group
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id)
)

# 4. To create books
cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
    ("RED Book", student_id),
)
cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
    ("BLUE Book", student_id),
)

# 5. To create subjects
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ("Monday",))
sub_mon_id = cursor.lastrowid

cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ("Tuesday",))
sub_tue_id = cursor.lastrowid

# 6. To create lessons
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ("First day", sub_mon_id)
)
lesson_first_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
    ("Second day", sub_tue_id),
)
lesson_second_id = cursor.lastrowid

# 7. Get marks for the student
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (3, lesson_first_id, student_id),
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    (3, lesson_second_id, student_id),
)

# 8. Save all changes in database
db.commit()

# 9. Student's marks
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
print("Marks:", marks)

# 10. Student's books
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
print("Books:", books)

# 11. All student's info in a one request
cursor.execute(
    """
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
WHERE s.id = %s
""",
    (student_id,),
)
full_info = cursor.fetchall()
print("Full student info:", full_info)


db.close()
