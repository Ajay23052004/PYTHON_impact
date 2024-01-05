class student:
    def __init__(self, name, age, gender, rollno):
        self.name = name
        self.age = age
        self.gender = gender
        self.rollno = rollno
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Roll No:", self.rollno)

# Create an object of the Student class
student1 = student("jaydeep", 20, "Male", 5054)
# Call the display method on the student1 object
student1.display()