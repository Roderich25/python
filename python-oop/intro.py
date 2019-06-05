# Programación Orientada a Objetos con Python3
import datetime


class Employee:
    nums_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        ''' Employee constructor '''
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.nums_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __repr__(self):  # for debug and devleopment
        return (f"Employee('{self.first}', '{self.last}', '{self.pay})'")

    def __str__(self):  # for the end-user
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


def intro():
    emp_1 = Employee('John', 'Doe', 500)
    emp_2 = Employee('Karl', 'Foo', 100)

    print(emp_2.fullname())
    print(Employee.fullname(emp_1))

    print(emp_1.pay)
    Employee.set_raise_amt(1.05)
    emp_1.apply_raise()
    print(emp_1.pay)

    # print(Employee.__dict__)
    print(Employee.nums_of_emps)

    emp_3_str = "Rod-Av-200"
    emp_3 = Employee.from_string(emp_3_str)
    print(emp_3.__dict__)

    print(Employee.nums_of_emps)

    my_date = datetime.date(2019, 6, 1)
    print(Employee.is_workday(my_date))

    print(emp_3)
    print(repr(emp_3))
    print(str(emp_3))
    print(emp_3.__repr__())
    print(emp_3.__str__())

    # magic/dunder

    print(1 + 2)
    print('a' + 'b')
    print(int.__add__(1, 2))
    print(str.__add__('a', 'b'))
    print(len('Rodrigo'))
    print('Rodrigo'.__len__())

    print(emp_1 + emp_2)
    print(emp_3.fullname())
    print(len(emp_3))

if __name__ == '__main__':
    intro()
