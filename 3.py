class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def calculate(self):
        return self.salary

class Manager(Employee):
    def calculate(self):
        return self.salary + 2000

class Developer(Employee):
    def calculate(self):
        return self.salary + 1000

class Intern(Employee):
    def calculate(self):
        return self.salary - 500

a = Manager("Justin", 60000)
b = Developer("Simla", 40000)
c = Intern("Thrisha", 3000)

print("Monthly Salaries:")
print(a.name,"=",a.calculate())
print(b.name,"=",b.calculate())
print(c.name,"=",c.calculate())

