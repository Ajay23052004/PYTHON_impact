#EXample of polymorephism 

class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")
class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Peguin can swim")

def flying_test(bird):
    bird.fly()
def swim_test(obj):
    obj.swim()
    
p = Parrot()
peggy = Penguin()

flying_test(p)
flying_test(peggy)

swim_test(p)
swim_test(peggy)

        
