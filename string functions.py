class namedisplay:
   def __init__(self,name): 
       self.x=100
   def display(self):
       y=40
       print("instance variable",self.x)
       print("normal variable is",y)
n=number()
n.display()
print("outside method the value is ",n.x)
print()
