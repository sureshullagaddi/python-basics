# All IF Conditions in One Program
user_age = 25
has_license = True
user_role = "admin"
users_list = ["alice", "bob", "john"]
account_balance = 1000
username = ""

# 1. Simple If
if user_age > 0:
    print("✓ Age is valid")

# 2. If-Else
if user_age >= 18:
    print("✓ User is adult")
else:
    print("User is minor")

# 3. If-Elif-Else (multiple conditions)
if user_age < 13:
    print("Child")
elif user_age < 18:
    print("Teen")
elif user_age < 65:
    print("✓ Adult")
else:
    print("Senior")

# 4. Nested If
if user_age >= 18:
    if has_license:
        print("✓ Can drive")
    else:
        print("Get license first")

# 5. Logical Operators (AND, OR, NOT)
if user_age >= 18 and has_license:
    print("✓ Eligible to drive")

if user_role == "admin" or user_role == "moderator":
    print("✓ Has permissions")

if not username:
    print("⚠ Username is empty")

# 6. Comparison Operators
if user_age == 25:
    print("✓ Exact age match")

if user_age != 30:
    print("✓ Age is not 30")

if account_balance > 500:
    print("✓ Good balance")

if user_age <= 65:
    print("✓ Working age")

# 7. Membership Operators (in, not in)
if "john" in users_list:
    print("✓ John is in users list")

if "alice" not in users_list:
    print("Alice not found")
else:
    print("✓ Alice found in list")

# 8. Ternary (One-liner)
status = "Verified" if has_license else "Not verified"
print(f"✓ Status: {status}")

# 9. Type Checking
if isinstance(user_age, int):
    print("✓ Age is integer type")

if type(users_list) == list:
    print("✓ users_list is a list")

# 10. Truthiness (implicit True/False)
if account_balance:
    print(f"✓ Has balance: {account_balance}")

if username:
    print(f"Username: {username}")
else:
    print("⚠ Username is empty (falsy)")

# 11. Complex Combination
if user_age >= 18 and has_license and (user_role == "admin" or "john" in users_list):
    print("✓ All conditions passed!")

print("\n--- Summary ---")
print(f"Age: {user_age}")
print(f"License: {has_license}")
print(f"Role: {user_role}")
print(f"Users: {users_list}")
print(f"Balance: ${account_balance}")