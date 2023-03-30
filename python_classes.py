class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = last_name + '.' + first_name +'@gmail.com'

    def full_name(self):
        return (f'{self.first_name} {self.last_name}')

emp_1 = Employee('Fran', 'Cili', 10000)#INSTANCA KLASE-objekt
emp_2 = Employee('Luka', 'Smaić', 20000)#INSTANCA KLASE-objekt

print(emp_1.full_name())
#Atributi instance emp_1
#emp_1.first_name = 'Fran'
#emp_1.last_name = 'Cili'
#emp_1.email = 'cili.fran@gmail.com'
#emp_1.salary = 10000

#Atributi instance emp_2
#emp_2.first_name = 'Luka'
#emp_2.last_name = 'Smaic'
#emp_2.email = 'smaic.luka@gmail.com'
#emp_2.salary = 20000

#POMOĆU __init__()metode gore navedene atribute možemo puno krače zapisati
