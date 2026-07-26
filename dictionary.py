person = {
    "name": "Suresh",
    "age": 30,
    "city": "Helsingborg"
}

print(person["name"])
print(person["age"])


person["country"] = "Sweden"

print(person)

for key, value in person.items():
    print(key, value)

employee = {}
employee["name"] = "Suresh"
employee["age"] = 30
employee["city"] = "Helsingborg"
print(employee)