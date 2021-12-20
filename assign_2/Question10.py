
#  Write a program which accept number from user and return addition of digits in that number.  
# Input : 5187934 Output : 37 
##################################################
def CountDigit(no):
    count=0
    sum=0
    while(no!=0):
        digit=no%10
        sum=sum+digit
        no=int(no/10)
    
        
    return sum


def main():
    no=int(input("Enter the number:"))
    
    iret=CountDigit(no)
    print("Sum of digits is:",iret)
    
    
if __name__=="__main__":
    main()