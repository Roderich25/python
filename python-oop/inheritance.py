# Herencia/Inheritance

from intro import Employee


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"** {emp.fullname()} **")


dev_1 = Developer('Johnny', 'Doe', 400, 'C++')
dev_2 = Developer('Carl', 'Foo', 200, 'Java')

print(dev_2)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# print(help(Developer))


mgr_1 = Manager('Simon', 'Doe', 1000, [dev_2])
print(mgr_1.email)
mgr_1.add_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Employee, Developer))
