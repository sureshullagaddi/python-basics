#Variables in python
name = "suresh ullagaddi"
age = 35
salary = 500000
is_active = True
country_live_in = "Sweden"
print(f"Name : {name.upper()} \nAge : {age} \nSalary : {salary}\nCountry live in: {country_live_in}")
print("-----------------")

#Input output
###user_name = input("Please enter your name : ")
###user_age = input("Please enter your age : ")
###user_salary = input("Please enter your salary : ")
##user_country = input("Please enter your country : ")
#print(f"User_name : {user_name}\nUser_age : {user_age}\nUser_Salary :{user_salary}\nUser country : {user_country}")

#operators
a = 10
b = 2

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b) # floor division
print(a % b)  # remainder
print(a ** b) # power
print("-----------------")

#Comparison Operators
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
print("-----------------")

#Logical Operators
age = 200
print(18 < age < 60)
print(age > 18 or age > 100)
print(not False)
print("-----------------")

if age > 18 or age > 100:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
print("-----------------")
#String Basics (10 min)
name = "Python"

print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("Python", "Java"))
first_name = "Suresh"
last_name = "Ullagaddi"

print(first_name + " " + last_name)
print("-----------------")


