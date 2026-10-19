num_str=input("Enter the numbers as a string: ")
num=num_str.split()
n=len(num)
for i in range(0,n):
    num[i]=int(num[i])
even_num=[]
odd_num=[]
for i in num:
    if i%2==0: even_num.append(i)
    else:odd_num.append(i)     
print(f"Even numbers: {even_num}")
print(f"Odd numbers: {odd_num}")