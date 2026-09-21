class laptop():
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("processor:",self.processor)
        print("ram:",self.ram)

hp=laptop()


hp.ram="16gb"
hp.processor="intel"

dell=laptop()

dell.ram="8gb"
dell.processor="ryzen"

hp.display()
dell.display()