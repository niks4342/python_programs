# 1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.

##############################################################################
import threading

def CheckEven(x):
    if(x%2==0):
       Edata.append(x)
            
def CheckOdd(x):
    if(x%2!=0):
       Odata.append(x)

if __name__ == "__main__":
   
    count=0
    Edata=[]
    Odata=[]
    
    for i in range(1,11):
        
        even=threading.Thread(target=CheckEven,args=(i,))
        even.start()
        odd=threading.Thread(target=CheckOdd,args=(i,))     
        odd.start()
        
    print(Edata)
    print(Odata)
    
        
    even.join()
    odd.join()