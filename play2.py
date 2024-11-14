class Robot:

    def __init__(self, name:str, age:int, motto:str, is_gay:bool):
        self.name = name
        self.age = age
        self.motto = motto
        self.is_gay = True

    def say_hello(self):
        print(self.name +  " says hello")

    def sexuality(self):
        if self.is_gay:
            print("I love dick")
        else:
            print("I hate peener")

my_robot = Robot("john", 15, "i eat shit", True)
Robot.say_hello(my_robot)
Robot.sexuality(my_robot)