###1.Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog
# Animal base class
'''class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("I am an animal!")

# Cow subclass
class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("hmmm")

# Horse subclass
class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("hihihi")

# Dog subclass
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("bow bow")

# Create an instance of each subclass
cow = Cow("gouri", 5)
horse = Horse("badhsha", 10)
dog = Dog("jimbo", 2)

# Call the make_sound() method on each instance
cow.make_sound()
horse.make_sound()
dog.make_sound()


###2..Create arithmetics class to calculate avg, mean, mode and standard deviation
class Arithmetics:

    def __init__(self, data):
        self.data = data

    def avg(self):
        return sum(self.data) / len(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def mode(self):
        mode = max(set(self.data), key=self.data.count)
        return mode

    def standard_deviation(self):
        mean = self.mean()
        variance = sum([(x - mean)**2 for x in self.data]) / len(self.data)
        return variance**0.5
arithmetics = Arithmetics([1, 2, 3, 4, 5])
average = arithmetics.avg()
print(average)
mean = arithmetics.mean()
print(mean)
mode = arithmetics.mode()
print(mode)
standard_deviation = arithmetics.standard_deviation()
print(standard_deviation)

###3..Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less than 18 should not be allowed to vote.
class VoterAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_voter_age(age):
    if age < 18:
        raise VoterAgeError("Voter age must be at least 18.")
def main():
    age = int(input("Enter voter age: "))

    try:
        validate_voter_age(age)
        print("You are eligible to vote.")
    except VoterAgeError as e:
        print(e)


if __name__ == "__main__":
    main()

'''
###.4 Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling. Person whose salary is less than 10K/ Month will not be eligible for the loan.

class LoanEligibility:
   

    def __init__(self, salary):
         self.salary = salary

    def is_eligible(self):
        if self.salary >= 10000:
            return True
        else:
            raise LoanNotEligibleError("Salary must be at least 10000.")


class LoanNotEligibleError(Exception):
   
    def __init__(self, message):
        super().__init__(message)


def main():
    salary = int(input("Enter your salary: "))

    try:
        loan_eligibility = LoanEligibility(salary)
        if loan_eligibility.is_eligible():
            print("You are eligible for loan.")
        else:
            print("You are not eligible for loan.")
    except LoanNotEligibleError as e:
        print(e)


if __name__ == "__main__":
    main()

