# Write a program which accept N numbers from user and store it into List. Return Minimum 
# number from that List. 

# Input : Number of elements : 4 
# Input Elements : 13 5 45 7 
# Output : 5 

###################################################################################

def Minimum(data):
    min=data[0]
    
    for i in range(len(data)):
        if(data[i]<min):
            min=data[i]
    
    return min

def main():
    size=0
    data=[]
    
    size=int(input("Enter how many elements you want:"));
    
    for i in range(size):
        data.append(int(input("Enter the element:")));
    
    print("Your enterd list is:",data);
    
    iret=Minimum(data)
    print("Minimum element from the list is:",iret);
    
    
if __name__=="__main__":
    main()