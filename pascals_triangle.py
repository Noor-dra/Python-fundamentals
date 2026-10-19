def fact(num):
    if num<=1: 
        return 1
    else: return num*fact(num-1)

def combination(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))

def print_pascals_triangle(num_rows):
       for i in range(num_rows):
             for space in range(num_rows-(i+1)):
               print(end=" ")
             for column in range(i+1):
                  print(combination(i,column),end=" ") 
             print()      

num_rows=int(input("Enter the number of rows: "))    
if num_rows<0:
    print("Error!Enter a positive integer!")
elif num_rows==0:
   print("Error! 0 is not allowed!")    
else:   
  print_pascals_triangle(num_rows)