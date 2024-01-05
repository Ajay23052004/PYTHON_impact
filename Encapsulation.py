class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price:{}".format(self.__maxprice))
    def setMaxprice(self,price):
        self.__maxprice = price
        
com1 = Computer()
com1.sell()

com1.__maxprice = 1000
com1.sell()

com1.setMaxprice(1000)
com1.sell()