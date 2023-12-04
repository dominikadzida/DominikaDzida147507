# ćw 1

class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


Student1 = Student("Marek", [60, 70, 80])
Student2 = Student("Jacek", [10, 30, 20])

wynik1 = Student1.is_passed()
print(f"Czy {Student1.name} zdał/a? {wynik1}")

wynik2 = Student2.is_passed()
print(f"Czy {Student2.name} zdał/a? {wynik2}")
