class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("mica: bark!")

mica = Dog()
mica.bark()