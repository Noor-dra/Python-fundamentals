board=[" " for i in range(9)]
def print_board():
  for i in range(0,7,3):
      print(f"|{board[i]}|{board[i+1]}|{board[i+2]}|")
     

def player_move(icon):  
   print(f"Your turn player {1 if icon=="X" else 2}.")   
   choice=int(input("Enter your move(1-9): ").strip())
   if 1<=choice<=9 and board[choice-1]==" ":
      board[choice-1]=icon  
   elif choice<1 or choice>9:
      print("Error:Invalid input!.Enter a number between 1-9.")
      print()
      player_move(icon)
   else:
      print("This space is taken.")
      print()
      player_move(icon)

def is_victory(icon):
   win_conditions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
   for condtion in win_conditions:
      if board[condtion[0]]==icon and board[condtion[1]]==icon and board[condtion[2]]==icon :
          return True

def is_draw():
   if " " not in board:
      return True
   
while True:
   print_board() 
   player_move("X") 
   print_board()
   if is_victory("X"):
      print("Player 1 wins.Congratulations🥳")
      break
   elif is_draw():
      print("Draw!")
      break
   player_move("O")
   if is_victory("O"):
      print_board()
      print("Player 2 wins.Congratulations🥳")
      break
   elif is_draw():
      print_board()
      print("Draw!🤭")
      break

