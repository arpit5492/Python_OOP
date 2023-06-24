class Dog:

    def __init__(self,name):
        self.name=name #self.name is an attribute
        print(name)
    def add_one(self,x):
        return x+1
    
    def bark(self): # This is a method of the class Dog
        print("bark")
# d = Dog() # d is an object which is an instance of a class 'Dog'
# d.bark() # We have called the method using the object of the class and the O/p: "bark"
# print(type(d)) # O/p is: <class '__main__.Dog'> Here __main__ means what module this class was defined. By 
# # default the module is '__main__'
# print(d.add_one(5)) #O/p will be 6
d1=Dog("Tim")
# print(d1.name)
d2=Dog("Arpit")
# print(d2.name)