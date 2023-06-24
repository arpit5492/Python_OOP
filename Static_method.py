# Static methods are the methods that are bound to a class rather
# than the objects of that class. Here we don't have to make an instance

class Math:

    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
    
    @staticmethod
    def run():
        print("Run")

print(Math.add5(5))
print(Math.add10(5))
Math.run()