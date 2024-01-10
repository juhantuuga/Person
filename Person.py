class Person:
    def __init__(self, name, birthday=None, place=None):
        self.__name = name
        if birthday is not None:
            self.__birthday = birthday
        else:
            self.__birthday = None

        if place is not None:
            self.__place = place
        else:
            self.__place = None

    def __str__(self):
        return f'{self.__name}, {self.__birthday}, {self.__place}'

    # GETTERS

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday

    @property
    def place(self):
        return self.__place

    # SETTERS
    @name.setter
    def name(self, value):
        self.__name = value
