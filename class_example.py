class Account:
    """
    Parent/Base Class
    """

    # Class Variable
    bank_name = "Microsoft Bank"

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name

        # Encapsulation (Private Variable)
        self.__balance = balance

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")

    # Withdraw Money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance")

    # Check Balance
    def check_balance(self):
        return self.__balance

    # Static Method
    @staticmethod
    def calculate_interest(balance, rate):
        return balance * rate / 100

    # Display Account Details
    def display(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Bank:", Account.bank_name)
        print("Account No:", self.account_number)
        print("Holder:", self.holder_name)
        print("Balance:", self.__balance)


# ---------------------
# Savings Account
# ---------------------
class SavingsAccount(Account):

    interest_rate = 5

    def add_interest(self):

        interest = Account.calculate_interest(
            self.check_balance(),
            SavingsAccount.interest_rate
        )

        self.deposit(interest)

        print(
            f"Interest Added: {interest}"
        )

    # Method Overriding
    def display(self):

        print("\n----- SAVINGS ACCOUNT -----")
        print("Holder:", self.holder_name)
        print("Balance:", self.check_balance())
        print("Interest Rate:", self.interest_rate, "%")


# ---------------------
# Current Account
# ---------------------
class CurrentAccount(Account):

    minimum_balance = 1000

    # Method Overriding
    def withdraw(self, amount):

        current_balance = self.check_balance()

        if (
            current_balance - amount
            < CurrentAccount.minimum_balance
        ):
            print(
                "Withdrawal denied."
            )
            print(
                f"Minimum balance "
                f"{CurrentAccount.minimum_balance}"
                f" must be maintained."
            )
        else:
            super().withdraw(amount)

    def display(self):

        print("\n----- CURRENT ACCOUNT -----")
        print("Holder:", self.holder_name)
        print("Balance:", self.check_balance())
        print(
            "Minimum Balance:",
            self.minimum_balance
        )


# ---------------------
# MAIN PROGRAM
# ---------------------

print("=== SAVINGS ACCOUNT ===")
s1 = SavingsAccount(101,"Suresh",5000)
s1.display()
s1.deposit(1000)
s1.withdraw(500)
s1.add_interest()
print("Final Balance:",s1.check_balance())
print("\n")

print("=== CURRENT ACCOUNT ===")
c1 = CurrentAccount(201,"John",10000)
c1.display()
c1.deposit(2000)
c1.withdraw(5000)
c1.withdraw(7000)
print("Final Balance:",c1.check_balance())