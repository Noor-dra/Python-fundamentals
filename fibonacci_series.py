# we are using the 1 based indexing
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
num_of_values=int(input("Enter the number upto which the series is required: "))
if num_of_values==0:
    print("Invalid input!")
else:    
  print("fibonacci series is as follows: ")
  for i in range(0,num_of_values):
    print(fibonacci(i),end=" ")