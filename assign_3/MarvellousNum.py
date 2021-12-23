def CheckPrime(data):
    sum=0
    value=0

    for i in range(len(data)):
        flag=True
        value=int(data[i]/2)
        for j in range(2,value+1):
            if(data[i]%j==0):
                flag=False
                break
            else:
                flag=True

        if flag==True:
            sum=sum+data[i]
            
    return sum