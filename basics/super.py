class a():
    def __init__(self):
      print("A")
    def display(self):
       print("your in class a")

class b(a):
   def __init__(self):
      super().__init__()
      print("B")
   def display(self):
      print("your are in class b")

class c():
    
     def __init__(self):
      super().__init__()
      print("c")
     def display(self):
      print("your are in class c")
   
      

obj1=a()
obj1.display()


   