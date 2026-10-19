n=int(input("Enter an positive integer:"))
if n<0:
    print("Enter a positive integer!")
elif n==0:
   print(f"sum is {n}")    
else:    
 sum=0
 i=1
 while i<=n:
    sum+=i
    i+=1
 print(f"Sum of first {n} natural numbers is {sum}")    
 