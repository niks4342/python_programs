# Write a program which accept number from user and check whether that number is positive or  negative or zero.  
# Input : 11 Output : Positive Number  
# Input : -8 Output : Negative Number  
# Input : 0 Output : Zero 

##########################################################
def Check(no):
    if(no>0):
        print("Positive number")
    elif(no<0):
        print("Negative number")
    elif(no==0):
        print("Number is 0")


def main():
    print("Enter the number:")
    no=int(input())
    
    Check(no)
    
if __name__=="__main__":
    main()