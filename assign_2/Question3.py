#  Write a program which accept one number from user and return its factorial.  
# Input : 5 Output : 120  

##################################################
def Factorial(no):
    fact=1
    for i in range(no,1,-1):     
        fact=fact*i
    return fact

def main():
    no=int(input("Entr the number:"))
    
    ret=Factorial(no)
    print("Factorial is:",ret)
    
if __name__=="__main__":
    main()