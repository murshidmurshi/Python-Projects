class Vehicle:
    name='BMW'
    color='white'
    kind='Car'
    value=100.0

    def func(self):
        result=f'{self.name} is with {self.color} color  and value is {self.value}'
        return result

v=Vehicle()
print(v.func())
print(v.color)