class Laptop:
    chargertype = "c-type"   # class variable

    def __init__(self):
        self.price = 34      # instance variable
        self.brand = ""

    def setprice(self, price):
        self.price = price

    def getprice(self):
        print("Price:", self.price)
        print("Charger Type:", self.chargertype)

    @classmethod
    def changechargertype(cls):
        cls.chargertype = "B-type"
        print("Charger type is changed")

    @staticmethod
    def info():
        print("This is Laptop class")


hp = Laptop()

hp.setprice(20000)

# Before changing charger type
hp.getprice()

# Change charger type
Laptop.changechargertype()

# After changing charger type
hp.getprice()

hp.info()