class phone:
    chargertype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand",self.brand)
        print("price",self.price)
        print("chargetype",self.chargertype)
phone.chargertype="B-type"
samsung=phone("samsung","50000")
samsung.display()
iphone=phone("iphone","75000")
iphone.display()
google=phone("pixel","45000")
google.display()