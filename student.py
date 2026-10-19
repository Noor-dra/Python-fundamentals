class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    def __str__(self):
        return f"{self.phy} {self.chem} {self.maths}"    

    @property
    def percent(self):
         return str((self.phy+self.chem+self.maths)/3) + " %"
     
     #operator overloading
    def __add__(self,other):
        m1=self.phy+other.phy
        m2=self.chem+other.chem
        m3=self.maths+other.maths
        return Student(m1,m2,m3)
    def __sub__(self,other):
        m1=self.phy-other.phy
        m2=self.chem-other.chem
        m3=self.maths-other.maths
        return Student(m1,m2,m3)
    
    def __gt__(self,other):
        m1=self.phy+self.chem+self.maths
        m2=other.phy+other.chem+other.maths
        if m1>m2:
            return True
        else:
            return False
    
s1=Student(71,95,93)
s2=Student(80,65,74)
print(s1)
print(s2)
print(s1+s2)
print(s1-s2)
if s1>s2:
    print("s1 wins!")
else:
    print("s2 wins!")    