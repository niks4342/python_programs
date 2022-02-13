# Design python application which contains two threads named as thread1 and thread2.  
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on  screen. 
# After execution of thread1 gets completed then schedule thread2. 

#################################################################################

import threading

def Sequence(no):
    data1=[]
    for i in range(1,no+1):
        data1.append(i)
    print("List of Numbers in sequence is:",data1)
    
    
def Reverse(no):
    data2=[]
    for i in range(no,0,-1):
        data2.append(i)
    print("List of Numbers in reverse sequence is:",data2)
    

if __name__=="__main__":
    
    no=int(input("How many numbers you want to display:"))
    
    Thread1=threading.Thread(target=Sequence,args=(no,))
    Thread1.start()
    Thread1.join()
    
    Thread2=threading.Thread(target=Reverse,args=(no,))
    Thread2.start() 
    Thread2.join()