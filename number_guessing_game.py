import random
x=random.randint(1,10)
while True:
 y=int(input("Guess a number between 1-10 : ").strip())
 if y<1 or y>10:
  print("Invalid Input!")
 elif y==x:
  print("Woah!You guessed it correctly 🥳")
  break
 elif y<x:
  print("Your guess is too low 🥺 ") 
 else:
  print("Your guess is too high 🥺") 