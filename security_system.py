names=["Noor Sarif","Taslima","Ness","Harvey Specter","Mike Ross","Donna Paulsen"]
while True:
    print("Hi!My name is Alexa.",end=" ")
    name=input("What's your name?: ").strip().title()
    if name in names:
        print(f"Welcome {name}.Hope you are doing good.")
        remove=input("Do you want to be removed from the system? (Y/N): ").strip().title()
        if remove=="Y":
            names.remove(name)
    else:
        print(f"Hmm! I don't think I have met you yet,{name}.",end=" ")
        add=input("Would you like to be added to the system? (Y/N):  ").strip().title()
        if add=='Y':
            names.append(name)   
       
