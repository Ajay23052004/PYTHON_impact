class person:
    def __init__(s,name,age):
        s.name=name
        s.age=age
    def myfunc(self):
        print("Hello my name is  "+self.name)
        print("I am "+str(self.age)+" years old")
p1=person("John",25)

p1.myfunc()
