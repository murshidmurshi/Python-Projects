class Human():
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def do_work(self):
        if self.occupation=='tennis player':
            print(self.name+' plays tennis')
        elif self.occupation=='actor':
            print(self.name+' shoot short film')
    def speak(self):
        print(self.name+' says,how are you? ')

tom=Human('tom','actor')
tom.do_work()
tom.speak()
mos=Human('mos','tennis player')
mos.do_work()
mos.speak()