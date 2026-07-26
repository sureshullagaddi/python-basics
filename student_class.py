class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def collage(self):
        print(f"{self.name} is going to college.")

s1 = Student("Tilda1", 15, "a")
s2 = Student("Tilda2", 16, "b")
s3 = Student("Tilda3", 17, "c")
s4 = Student("Tilda4", 18, "d")

student_list = [s1, s2, s3, s4]
student_dictionary = {}
for student in student_list:
    student_dictionary[student.name] = {"age": student.age, "grade": student.grade}
print(student_dictionary)


