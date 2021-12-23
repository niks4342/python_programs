# Write a program which accept N numbers from user and store it into List. Accept one another 
# number from user and return frequency of that number from List. 

# Input : Number of elements : 11 
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
# Element to search : 5 
# Output : 3 

############################################################################


def CountFreq(data,no):
    freq=0
    
    for i in range(len(data)):
        if(data[i]==no):
            freq=freq+1
    
    return freq;

def main():
    size=0;
    data=[]
    
    size=int(input("Enter how many elements you want:"))
    
    for i in range(size):
        data.append(int(input("Enter the element:")))
    
    print("Your enterd list is:",data);
    
    no=int(input("Enter number to find the frequency:"))
    
    iret=CountFreq(data,no)
    print("Frequency of entred number in the list is:",iret)
    
    
if __name__=="__main__":
    main()