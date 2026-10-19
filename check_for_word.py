file_name=input("Enter the filename ")
def check_for_word(word):
   with open(f"{file_name}","r") as f:
     content= f.read()
     words=content.split()
     if word in words:
        print("Found!")
     else:
      print("Not found!")  

check_for_word("learning")
 