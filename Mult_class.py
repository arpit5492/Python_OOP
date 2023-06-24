# There are a number of students in a class and some grades
# are assigned to the students and we have to create different
# methods to find maximum grade or minimum grade or average.
class Students:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade # grade is between 0-100
    def get_age(self):
        return self.age
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self,Crse_name,max_stu):
        self.Crse_name=Crse_name
        self.max_stu=max_stu
        self.students=list()
    
    def add_students(self,stu):
        if len(self.students)<self.max_stu:
            self.students.append(stu)
            return True
        return False
    def find_avg(self):
        v=0
        for i in self.students:
            v+=i.get_grade()
        return v/len(self.students)

s1=Students("Arpit",24,96)
s2=Students("Rahul",12,69)
s3=Students("Raj",25,76)

course=Course("Maths",2)
course.add_students(s1)
(course.add_students(s2))
print(course.add_students(s3))
print(course.students[0].name)

print(course.find_avg())


