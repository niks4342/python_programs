# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.

###############################################################################

import threading

def EvenFactor(no):
    for i in range(1,no+1):
        if((no%i==0) and (i%2==0)):
            Evenfact.append(i)
            
def OddFactor(no):
    for i in range(1,no+1):
        if((no%i==0) and (i%2!=0)):
            Oddfact.append(i)
            

if __name__=="__main__":
    Evenfact=[]
    Oddfact=[]
    no=int(input("Enter the number:"))
    evenfactor=threading.Thread(target=EvenFactor,args=(no,))
    evenfactor.start()
    oddfactor=threading.Thread(target=OddFactor,args=(no,))
    oddfactor.start()
    
    print("List of even factors of given number is:")
    print(Evenfact)
    print("List of odd factors of given number is:")
    print(Oddfact)
    
    evenfactor.join()
    oddfactor.join()
    
    print("End from main")