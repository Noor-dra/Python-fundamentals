class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}k"

    def __add__(self,other):
       x=self.x+other.x
       y=self.y+other.y
       z=self.z+other.z
       return Vector(x,y,z)
    

    def dot(self,other):
         x=self.x*other.x
         y=self.y*other.y
         z=self.z*other.z
         return x+y+z

    def cross_product(self,other):
        x=(self.y*other.z)-(self.z*other.y)
        y=-((self.x*other.z)-(self.z*other.x))
        z=(self.x*other.y)-(self.y*other.x)
        return Vector(x,y,z)


v1=Vector(2,3,5)
print(v1)
v2=Vector(4,5,10)
print(v2)
print(v1+v2)
print(v1.dot(v2))
print(v1.cross_product(v2))
