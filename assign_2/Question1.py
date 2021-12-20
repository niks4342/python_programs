# Create on module named as Arithmetic which contains 4 functions as 
# Add() for addition, Sub()  for subtraction, Mult() for multiplication and Div() for division. 
# All functions accepts two  parameters as number and perform the operation. Write on python program 
# which call all the  functions from Arithmetic module 
# by accepting the parameters from user.  
import arithmatic

def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    ret=arithmatic.Addition(no1,no2)
    print("Addition is :",ret)
    
    ret=arithmatic.Subtraction(no1,no2)
    print("Subtraction is:",ret)
    
    ret=arithmatic.Multiplication(no1,no2)
    print("Multiplication is:",ret)
    
    ret=arithmatic.Division(no1,no2)
    print("Division is:",ret)
       
    
if __name__=="__main__":
    main()