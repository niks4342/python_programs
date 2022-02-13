# Design python application which creates three threads as small, capital, digits. 
# All the  threads accepts string as parameter. Small thread display number of small characters,  
# capital thread display number of capital characters and digits thread display number of  digits. 
# Display id and name of each thread. 

#############################################################################################


import threading
import os

def Small(data):
    print("PID of Small is:",os.getpid())
    SmallData=[]
    for i in range(len(data)):
        if(data[i].islower()==True):
            SmallData.append(data[i])
    print("List with small charachter from the string is:",SmallData)
    
def Capital(data):
    print("PID of Capital is:",os.getpid())
    CapitalData=[]
    for i in range(len(data)):
        if(data[i].isupper()==True):
            CapitalData.append(data[i])
    print("List with small charachter from the string is:",CapitalData)
    
def Digit(data):
    print("PID of Digit is:",os.getpid())
    DigitData=[]
    for i in range(len(data)):
        if(data[i].isdigit()==True):
            DigitData.append(data[i])
    print("List with small charachter from the string is:",DigitData)

if __name__=="__main__":
    
    print("PID of main is:",os.getpid())
    str=input("Enter the string:")
    small=threading.Thread(target=Small,args=(str,))
    small.start()
    capital=threading.Thread(target=Capital,args=(str,))
    capital.start()
    digit=threading.Thread(target=Digit,args=(str,))
    digit.start()
    
    small.join()
    capital.join()
    digit.join()