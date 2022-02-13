# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.

##################################################################################

import threading

def EvenSum(data):
    Esum=0
    for i in range(len(data)):
        if(data[i]%2==0):
            Esum=Esum+data[i]
    print("Sum of even elements from the list is:",Esum)
    
def OddSum(data):
    Osum=0
    for i in range(len(data)):
        if(data[i]%2!=0):
            Osum=Osum+data[i]
    print("Sum of odd elements from the list is:",Osum)

if __name__=="__main__":
    size=int(input("Enter the size of the list:"))
    data=[]
    for i in range(size):
        data.append(int(input("Enter element:")))
        
    print("Your enterd list is:",data)
    
    
    evenlist=threading.Thread(target=EvenSum,args=(data,))
    evenlist.start()
    oddlist=threading.Thread(target=OddSum,args=(data,))
    oddlist.start()
    
    evenlist.join()
    oddlist.join()