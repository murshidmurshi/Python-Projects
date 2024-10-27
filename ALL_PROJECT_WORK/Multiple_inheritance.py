class Father():
    def skill(self):
        print('Gardening,program')
class Mother():
    def skill(self):
        print('Cooking,art')
class Child(Father,Mother):
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print('Sport')

c=Child()
c.skill()