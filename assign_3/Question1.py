# Write a program which accept N numbers from user and store it into List. Return addition of all 
# elements from that List. 
# Input : Number of elements : 6 
# Input Elements : 13 5 45 7 4 56 
# Output : 130 

########################################################################

def Addition(data):
    sum=0
    for i in range(len(data)):
        sum=sum+data[i]
    return sum
        

def main():
    size=0
    data=[]
    
    print("Enter how many number of elements you want:")
    size=int(input())
    
    for i in range(size):
        data.append(int(input("Enter the elements:")))
    
    print("Your entered elements are: ",data)
    
    ret=Addition(data)
    print("Addition of all enterd elements is:",ret)
        
    
if __name__=="__main__":
    main()
