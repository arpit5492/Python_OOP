# Class attributes are the attributes that are specific to the class
# not to the instance or to the object of that class

class Person:
    no_of_people=0
    def __init__(self,name):
        self.name =name
        Person.add_person()
        
    @classmethod
    def no_of_people_(cls):
        return cls.no_of_people
    
    @classmethod
    def add_person(cls):
        cls.no_of_people+=1
p1=Person("Jimmy")
# print(p1.no_of_people)
p2=Person("Jane")
# print(p2.no_of_people)
print(Person.no_of_people_())
# Person.no_of_people=8
