# Solution

class Person:
    # Your Own Code

    def __init__(self, first_name, last_name, gender, phone_number=None):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        if gender not in ('M', 'F'):
            raise ValueError('GENDER MUST BE M OR F')

        self.gender = gender
        self.phone_number = phone_number

    def __str__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name}, gender={self.gender}, phone_number={self.phone_number})"

    def __repr__(self):
        if self.gender == 'M':
            gender = 'Mr'
        else:
            gender = 'Mrs'
        return f"{gender}, {self.first_name}, {self.last_name}"


p = Person('jan', 'KOW/Alski', gender='M')
print(p.first_name)
print(p.last_name)
print(p)

p = Person('jOE', 'KOWAlski', gender='M')
print(p)
print(p)
