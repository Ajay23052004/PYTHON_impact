class Bird:
    def __init__(self):
        print("Bird is ready")
    def whois(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Pengin is ready")
    def whois(self):
        print("Penguin")
    def run(self):
        print("run Fast")
peggy = penguin()
peggy.whois()
peggy.swim()
peggy.run()