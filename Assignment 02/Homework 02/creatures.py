class Creature(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is " + self.name + " and I am Creature.")


class Dog(Creature):

    def speak(self):
        print("My name is " + self.name + " and I am a Dog: woof.")


class Cow(Creature):

    def speak(self):
        print("My name is " + self.name + " and I am a Cow: moo.")


creature = Creature("Alex")
dog = Dog("Buddy")
cow = Cow("Bessie")

creature.speak()
dog.speak()
cow.speak()
