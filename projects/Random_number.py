import random

playing=input("Do you want to play the game ?")

if(playing.lower()!="yes"):
    quit()

print("Description of game:")
print("It is a ramdom number guess game.computer will print any random number in the range \nyou have given and you have to predict what will be that number")
top_range=input("Enter the number(range):")

if(top_range.isdigit()):
    top_range=int(top_range)
    
    if(top_range<=0):
        print("Please enter the number greater than 0 next time :(")
        quit()
else:
    print("Please enter the valid number next time :(")
    quit()


random_number=random.randint(0,top_range)

while True:
    user_guess=input("Please make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter the valid number next time :(")
        continue
        
    if (user_guess==random_number):
        print("You got is correct")
        break
    
    elif user_guess>random_number:
        print("You are above the number")
    else:
        print("You are below the number")
        
        
print("Thank you for Playing!!  :)")