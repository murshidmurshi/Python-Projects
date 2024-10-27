class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg

    def handle(self):
        print('Accident occured.take detour')


try:
    raise Accident('Crash between two car ')
except Accident as e:
    e.handle()