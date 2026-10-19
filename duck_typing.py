class Duck:
    def fly (self):
        print("The duck is flying.")
    def swim(self):
        print("The duck is swimming.") 

class Bird:
    def fly(self):
        print("The bird is flying.")  
    def swim(self):
        print("The bird is swimming.")   

class Albatross: 
    def swim(self):
        print("The albatross is swimming.")    

Birds=[Duck(),Bird(),Albatross()]
for bird in Birds: 
  if hasattr(bird,'fly') :
    bird.fly()
  if hasattr(bird,'swim'):
     bird.swim()

