# Write a program which accept one number form user and return addition of its factors.  
# Input : 12 Output : 16 (1+2+3+4+6) 

########################################################
def AddFact(no):
    sum=0
    for i in range(1,no):
        if(no%i==0):
            sum=sum+i
           
    return sum

def main():
    no=int(input("Enter the number:"))
    ret=AddFact(no)
    print("Addition of factor is:",ret)
    
    
if __name__=="__main__":
    main()