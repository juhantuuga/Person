from Person import *

if __name__ == '__main__':
    p = Person('Juhan Tuuga')
    print(p.__str__())

    p1 = Person('Lennart-Georg Meri', '29.03.1929')
    p2 = Person('Arnold Rüütel', '10.05.1928', 'Pahavalla küla')
    p3 = Person('Alar Karis', place='Kadriorg')
    print(p1.__str__())
    print(p2.__str__())
    print(p3.__str__())

    # GETTERS
    print(p.name, p.birthday, p.place)
