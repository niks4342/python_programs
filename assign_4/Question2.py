# .Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18 

##############################################################################
Mult=lambda no1,no2:no1*no2


def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    iret=Mult(no1,no2)
    print("Multiplication of two enterd numbers is:",iret)    
    
if __name__=="__main__":
    main()