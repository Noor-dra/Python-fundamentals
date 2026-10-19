films=dict(Pathaan=[15,5],Dora=[10,5],Animal=[18,5],Spiderman=[5,5],Pushpa=[13,5])
while True:
    choice=input("Enter the film of your choice: ").strip().title()
    if choice in films:
        # checking the ager of user
        age=int(input("What's your age? : " ).strip())
        if age>=films[choice][0]:
            #checking the availability of tickets
            if films[choice][1]>0:
                print('Enjoy the film 🥰')
                films[choice][1]-=1
            else:
                print("Sorry,we are sold out 😟")
        else:
            print("Oops!you are too young to watch this film 😟")    
    else: 
        print("Sorry,we don't have this film 😞 ")    

    
