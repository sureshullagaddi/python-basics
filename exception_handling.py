try:
    number = int(input("Enter number: "))
    print(number)
except Exception as e:
    print("Invalid input: " + str(e))