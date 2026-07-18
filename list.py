names = ["suresh", "Rashmi", "Siddarooda"]

print(names)
names.append("Ramesh")
print(names)

names.remove("Rashmi")
print(names)


for name in names:
    print(name.upper())

print("---------------------")
numbers = [10, 20, 30, 40]

print(sum(numbers))
print(max(numbers))
print(min(numbers))