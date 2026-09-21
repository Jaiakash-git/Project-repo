class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("add=",self.a+self.b)
       
    def sub(self):
        print("a-b=",self.a-self.b)
       
    def mul(self):
        print("a*b=",self.a*self.b)
       
    def div(self):
        print("div=",self.a//self.b)
        
    
c1=calculator(10,5)

c1.add()
c1.sub()
c1.mul()
c1.div()