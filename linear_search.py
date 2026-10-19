#Taking the list from the user
n=int(input("Enter the no. of items in the list: "))
fruits=[]
print("Enter the list:")
for i in range(0,n+1):
    fruit=input()
    fruits.append(fruit)

#searching an item in the list
target=input("Enter the fruit to be searched:")
i=0
len_fruits=len(fruits)
while i<len_fruits:
    if fruits[i]==target:
        print(f"Target found at index {i}")
        break #for terminating the loop once the item is found in the list
    i+=1
else: 
    print("Target not found in the list")
    #comment2:
    """ the statement in the else block will be executed only and if only the while condition
    evaluates to false """   
        



