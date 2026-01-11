from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Amount {amount} deposited in the account \nNew balance {self.__balance}")
        else:
            print(f"Amount should be positive")
            
    @abstractmethod
    def calculate_interest(self):
        pass
    
class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        return f"Interest earned: {interest:.2f}"
    
class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            return f"Withdrew {amount}\nNew balance: {new_balance}"
        return "Overdraft limit exceeded"
    
    def calculate_interest(self):
        return "Checking Account earns no interest"

def print_account_info(account):
    print(f"\n--- Account: {account.account_number} ---")
    print(f"Owner: {account.owner}")
    print(f"Balance: ${account.get_balance()}")
    print(account.calculate_interest())
    

savings = SavingsAccount("SAV001", "John", 5000)
checking = CheckingAccount("CHK001", "Alice", 2000)

print(savings.deposit(1000))
print_account_info(savings)

print(checking.deposit(500))
print_account_info(checking)

# Polymorphism - same function, different behaviors
accounts = [savings, checking]
for account in accounts:
    print_account_info(account)