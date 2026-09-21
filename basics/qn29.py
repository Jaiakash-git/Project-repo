class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("Name:",self.name)
        print("Name:",self.regno)
t1=teacher("Akash","61")
t2=teacher("Jai","10")

t1.display()
t2.display()