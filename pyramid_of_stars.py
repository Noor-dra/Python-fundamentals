rows=int(input("Enter the number of rows: "))
if rows<0:
    print("Error!Enter a positive integer!")
elif rows==0:
   print("Error! 0 is not allowed!")  
else:   
 for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(end=" ")
    for star in range(1,i+1):
        print("*",end=" ")    
    print()    