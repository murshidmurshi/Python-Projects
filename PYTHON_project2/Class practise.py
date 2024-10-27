class Dog():

    def __init__(self,name):
        self.name=name

    def speak(self):
        return (self.name+' says bow!!' )

class Cat():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name+' says meow!!'




dog=Dog('niko')
cat=Cat('fido')
print(dog.name)
print(dog.speak())
print(cat.name)
print(cat.speak())