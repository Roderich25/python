# Property decorators: getters, setters and deleters

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = name + '.' + last + '@email.com'

    @property  # getter
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


per_1 = Person('Jim', 'Carey')
per_1.fullname = 'John Wick'

print(per_1.email)
print(per_1.fullname)
del per_1
#print(per_1)