class Person:
    " This is a person class"
    age=110
    
    def greet(self):
        print("hello")

harry = Person()
print(harry.greet)
print(Person.greet)
print(harry.greet)
print(Person.greet)

harry.greet()