#  Quize  Game
import time

print("Welcome to my Quize Game...Have a fun :)!!")
time.sleep(1)

playing=input("Do you want to play the game ?")

if(playing.lower()!="yes"):
    quit()


print("please wait....")
time.sleep(5)

print("Let's Play :))")
time.sleep(2)

count=0
answer=input("What is the full form of CPU?")
if(answer.lower()=="central processing unit"):
    print("Correct!! :)")
    count+=1
else:
    print("Incorrect..Better Luck Next Time....")   
    
     
time.sleep(2)
answer=input("What does the GUI stands for?")
if(answer.lower()=="graphic user interface"):
    print("Correct!! :)")
    count+=1
else:
    print("Incorrect..Better Luck Next Time....")  
    
    
time.sleep(2)   
answer=input("What is the full form of RAM?")
if(answer.lower()=="random access memory"):
    print("Correct!! :)")
    count+=1
else:
    print("Incorrect..Better Luck Next Time....")  
    
    
time.sleep(2)    
answer=input("What is the full form of CUI?")
if(answer.lower()=="command user interface"):
    print("Correct!! :)")
    count+=1
    
    print("Thank you for Playing!!  :)")
    quit()
else:
    print("Incorrect..Better Luck Next Time....")  
    
    print("Thank you for Playing!!  :)")
    quit()
    
