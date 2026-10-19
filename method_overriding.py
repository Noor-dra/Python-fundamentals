class Parent:
    def show (self): #overriden method
      print("Inside parent.")

class Child(Parent):
    def show (self): #overriding method
       print("Inside child.")    

obj1=Child()     
obj1.show()