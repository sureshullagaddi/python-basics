file = open("demo.txt", "w")
file.write("This is an example file where i m writing some content")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()

with open("demo.txt", "r") as file:
    print(file.read())