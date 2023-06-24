x=1 #We can see the output as <class 'int'>. It means all the datatypes are actually part of a class.
# So, above x equals to the object '1' which is a type integer. (Object is an instance of a class)
def hello():
    print('Hello')
print(type(hello)) # Output will be <class 'function'>

# Now let's see what methods are:
string = 'Hello'
print(string.upper()) # The object 'string' has a method 'upper()'.