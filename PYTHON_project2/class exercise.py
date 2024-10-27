class Main():
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'Hi I am {self.name}')
jhon=Main('Murshid')
jhon.talk()
bob=Main('BOB')
bob.talk()