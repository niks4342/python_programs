# Write a program which contains one function named as ChkNum() which accept one  parameter as number. 
# If number is even then it should display “Even number” otherwise  display “Odd number” on console.  
# Input : 11 Output : Odd Number  
# Input : 8 Output : Even Number  

#######################################################################
def CheckNum(no):
    if(no%2==0):
        print("Even number")
    else:
        print("Odd number")


def main():
    print("Enter the number:")
    no=int(input())
    
    CheckNum(no)
    
    
if __name__=="__main__":
    main()