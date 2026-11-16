from abc import ABC , abstractmethod
class SmartDevices(ABC):
    def move(self):
        print("Hello world!")
class Human(SmartDevices):
    def move(self):
        print("HI ,BRO")
class Laptop(SmartDevices):
    def move(self):
        print("HI,USER")
class Mobile(SmartDevices):
    def move(self):
        print("HI,LOGGED IN")
class PC(SmartDevices):
    def move(self):
        print("HI,ACCOUNT")
R = Human()
R.move()
K = Laptop()
K.move()
R = Mobile()
R.move()
K = PC()
K.move()
