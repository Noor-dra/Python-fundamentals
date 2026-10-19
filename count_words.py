#counting no of words in a string using len() and for loop

str1=input("Enter the sentence: ")
str_list=str1.split()
#using len()
#count=len(str_list) # no of words will be equal to the number of items in the list 
#using for loop
count=0
for ch in str_list:
    count+=1
print(f"no. of words in the sentence is {count} ")