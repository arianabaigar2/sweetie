class Person:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


person = Person("Arianie")
print(person.get_name())
person.set_name("Arianna")
print(person.get_name())
