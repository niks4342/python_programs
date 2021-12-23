# Write a program which accept N numbers from user and store it into List. Return Maximum 
# number from that List. 
# Input : Number of elements : 7 
# Input Elements : 13 5 45 7 4 56 34 
# Output : 56

##################################################################################


def Maximum(data):
    max=data[0]
    
    for i in range(len(data)):
        if(data[i]>max):
            max=data[i]
    return max        


def main():
    size=0;
    data=[]
    
    size=int(input("Enter how many elements you want:"))
    
    for i in range(size):
        data.append(int(input("Enter the elements:")))
    
    print("Your entred elements are:",data)
    
    iret=Maximum(data)
    print("Maximum number from the entred list is:",iret)
    
    
    
if __name__=="__main__":
    main()