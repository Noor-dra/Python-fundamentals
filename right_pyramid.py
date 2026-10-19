rows=int(input("Enter the number of rows: "))
if rows<0:
    print("Error!Enter a positive integer!")
elif rows==0:
   print("Error! 0 is not allowed!")  
else:   
#for upper right triangle pattern
 for i in range(1,rows+1):
    for star in range(1,i+1):
        print("*",end=" ")
    print()
#for lower right triangle pattern
 rows_=rows-1
 for j in range(0,rows_):
    for star_ in range(1,rows_-j+1):
        print("*",end=" ")
    print()
