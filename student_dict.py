# Dictionary of 4 students with name as key, grade and age as values
students = {
    "Alice": {"grade": "A", "age": 20},
    "Bob": {"grade": "B", "age": 21},
    "Carol": {"grade": "A", "age": 20},
    "David": {"grade": "B", "age": 22}
}

print(students)

# Access individual student information
for name, info in students.items():
    print(f"{name}: Grade {info['grade']}, Age {info['age']}")
