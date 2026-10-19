rows=int(input("Enter the number of rows: "))
if rows<0:
    print("Error!Enter a positive integer!")
elif rows==0:
   print("Error! 0 is not allowed!")    
else:
  for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=" ") # end=" " means that it will print a whitespace after the value of i in the same line
    print()    #for next line after iterating over all the columns of a row
       