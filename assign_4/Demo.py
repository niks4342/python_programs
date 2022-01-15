
from functools import reduce

def FilterX(data):
    newdata=[]
    for i in range(len(data)):
        if(data[i]>=70 and data[i]<=90):
            newdata.append(data[i])
    return newdata  
            
def MapX(data):
    newlist=[]
    for i in range(len(data)):
        no=data[i]+10
        newlist.append(no)
    return newlist
    
def ReduceX(data):
    result=1
    for i in range(len(data)):
        result=result*data[i]
    return result

