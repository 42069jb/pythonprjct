'''secret_number=8
limit=3
i=0
while i<3:
    number=int(input("guess::"))
    if number==secret_number:
        print("you win")
        break
    if i==2:
        print("you lose")
    i += 1 '''
#car game
string="QUIT"
flag=0
print('''CAR GAME
start--to start the car
stop---to stop the car
quit---to quit this game
help---to get help''')
while(flag!=1):
    keyboard = input(">").upper()
    if keyboard=="START":
        print("Car Started successfully")
    elif keyboard=="STOP":
        print("Car Stopped succesfully")
    elif keyboard == "QUIT":
        flag=1
    elif keyboard=="HELP":
        print('''
start--to start the car
stop---to stop the car
quit---to quit this game
help---to get help''')
    else:
        print("It's a wrong command buddy")


