class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + ' ' + last + '@gmail.com'
    @property
    def email(self):
        return '{} {}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first =first
        self.last = last

emp1 = Employee('john', 'smit')
emp1.first ='jim'

emp1.fullname = "raam jane"
print(emp1.first)
print(emp1.email)
print(emp1.fullname)


