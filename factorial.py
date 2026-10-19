def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

number=int(input("Enter a positive interger: "))
if number>=0:
    fact=factorial(number)
    print(f"factorial of {number} is {fact}")
else:
    print("Invalid input!")    
    