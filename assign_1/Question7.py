# Write a program which contains one function that accept one number from user and 
# returns  true if number is divisible by 5 otherwise return false.  
# Input : 8 Output : False  
# Input : 25 Output : True  

##########################################################################
def CheckDivisible(no):
    if(no%5==0):
        return True
    else:
        return False

def main():
    no=int(input("Enter the number:"))
    
    bret=CheckDivisible(no)
    
    if(bret==True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
    
if __name__=="__main__":
    main()