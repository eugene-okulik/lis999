from HW_11_Task_1 import Book


class SchoolBook(Book):
    def __init__(
        self,
        title,
        author,
        pages,
        isbn,
        subject,
        grade,
        with_task=False,
        reserved=False,
    ):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.with_task = with_task

    def school_book_details(self):
        if self.reserved:
            print(
                f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Subject: {self.subject}, "
                f"Grade: {self.grade}, reserved"
            )
        else:
            print(
                f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Subject: {self.subject}, "
                f"Grade: {self.grade}"
            )


first_school_book = SchoolBook(
    "Algebra", "Chaika", 268, 12345, "Math", 10, reserved=True
)
second_school_book = SchoolBook("Chemistry", "Brosalina", 171, 23456, "Chemistry", 10)
third_school_book = SchoolBook(
    "Physics", "Bykova", 195, 34567, "Physics", 9, reserved=False
)
forth_school_book = SchoolBook("Geometry", "Vlasova", 113, 12345, "Geometry", 11)
fifth_school_book = SchoolBook(
    "English", "Loseva", 125, 12345, "English", 8, reserved=True
)

first_school_book.school_book_details()
second_school_book.school_book_details()
third_school_book.school_book_details()
forth_school_book.school_book_details()
fifth_school_book.school_book_details()
