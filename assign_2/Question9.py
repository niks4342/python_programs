# Write a program which accept number from user and return number of digits in that number.  
# Input : 5187934      Output : 7 


##################################################
def CountDigit(no):
    count=0
    digit=0
    while(no!=0):
        digit=no%10
        count=count+1
        no=int(no/10)
    
        
    return count


def main():
    no=int(input("Enter the number:"))
    
    iret=CountDigit(no)
    print("Count of digits is:",iret)
    
    
if __name__=="__main__":
    main()