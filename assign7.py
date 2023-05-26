###..1..Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        pass


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says 'hmmm'")


class Horse(Animal):
    def make_sound(self):
        print(f"{self.name} says 'hihihi'")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says 'bow bow'")

cow = Cow("gouri", 4)
horse = Horse("badhsha", 2)
dog = Dog("jimbo", 1)

cow.eat()         
horse.sleep()     
dog.make_sound() 





###..2..Create a Bank Account in class which includes customer balance, day wise transactions, can transfer money to different person account, interest given to him with a specific percentage
class BankAccount:
    def __init__(self, customer_name, initial_balance=0):
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw {amount}")
        else:
            print("Insufficient balance.")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transactions.append(f"Transferred {amount} to {recipient.customer_name}")
        else:
            print("Insufficient balance.")

    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")

    def show_balance(self):
        print(f"Account balance for {self.customer_name}: {self.balance}")

    def show_transactions(self):
        print(f"Transaction history for {self.customer_name}:")
        for transaction in self.transactions:
            print(transaction)


account1 = BankAccount("shravan", 10000)
account2 = BankAccount("Ram", 5000)

account1.deposit(5000)
account2.withdraw(2000)

account1.show_balance()       
account2.show_balance()       

account1.transfer(200, account2)
account1.calculate_interest(5)

account1.show_balance()      
account2.show_balance()       

account1.show_transactions()

account2.show_transactions()


