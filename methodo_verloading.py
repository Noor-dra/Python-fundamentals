from multipledispatch import dispatch 
class Maths:
    @staticmethod
    @dispatch(int,int)
    def product(x,y):
        p=x*y
        return p

    @staticmethod
    @dispatch(int,int,int)
    def product(x,y,z):
        p=x*y*z
        return p
    
m1=Maths()    
print(m1.product(1,3,4))
print(m1.product(5,4))