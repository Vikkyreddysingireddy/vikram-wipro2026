class BankAccount():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount<=0:
                raise ValueError("Enter the amount more than Zero")
            self.balance += amount
        except Exception as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount<=0:
                raise ValueError("Enter the amount more than Zero")
            elif amount > self.balance:
                raise ValueError("Enter the amount less than Current Balance")
            else:
                self.balance -= amount
                print(f"withdrawal is done and your current balance is {self.balance}")
        except Exception as e:
            print(e)

    def __del__(self):
        print("Execution Done and all the objects are cleared")

b=BankAccount("Vikky", 1000)
b.deposit(0)
b.withdraw(10000)