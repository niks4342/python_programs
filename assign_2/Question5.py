# Write a program which accept one number for user and check whether number is prime or not.  
# Input : 5    Output : It is Prime Number

##########################################################
def Prime(no):
    i=2
    flag=True
    while(i<(no/2)):
        if(no%i==0):
            flag=False
            break
        i+=1
        
    return flag

def main():
    no=int(input("Enter the number:"))
    bret=Prime(no)
    if(bret==True):
        print("prime")
    else:
        print("not Prime")
    
if __name__=="__main__":
    main()