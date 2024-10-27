class Dog():
    def walk(self):
        print('Slowly !')
    def eat(self):
        print('Eaten!!')
class Cat(Dog):
    pass
dog=Dog()
dog.walk()
dog.eat()

cat=Cat()
cat.walk()
cat.eat()
