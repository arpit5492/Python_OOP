# Now for the below example, as we can see the __init__ method
# in both the classes are same. So we can define a parent class above
# and then inherit both the child classes i.e Cat and Dog from
# the parent class i.e Pet in this case
class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to do")

class Cat(Pet):

    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} and I am {self.color}")
    
    def speak(self):
        print("Meow")
    

class Dog(Pet):
    
    def speak(self):
        print("bark")

class Wolf(Pet):
    pass
    

c = Cat("Jim",78,"White")
d = Dog("Hopper",65)
p = Pet("Jimmy",68)
w = Wolf("Handy",12)
w.speak() # O/p: I don't know what to do bc it will take the output from the parent calss i.e Pet
p.show()
p.speak()
# c.speak()
# d.speak()
c.show() # I am Jim and I am 78 and I am White
d.show()
