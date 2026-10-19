import random

class Pound:
    def __init__(self,rare=False):
       self.rare=rare
       if self.rare:
           self.value=1.25
       else:
           self.value=1    
       self.color='gold'
       self.diameter=22.5 #mm
       self.thickness=3.15 #mm
       self.heads=True
    
    def rust(self):
        self.color="greenish"
    def clean(self):
        self.color='gold'

        
    def flip(self):
        self.heads=random.choice([True,False])

    @staticmethod
    def __del__():
        print("Coin spent!")

coin2=Pound(True) #object 2
print(coin2.heads)
print(coin2.value)
del coin2.thickness
try:
 print(coin2.thickness)
except: 
 del coin2
 print(coin2.value)