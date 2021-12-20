# Write a program which contains one function named as Add() which accepts two numbers  
# from user and return addition of that two numbers.  
# Input : 11 5 Output : 16

##############################################################3
def Addition(value1,value2):
    result=value1+value2
    return result

def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    iret=Addition(no1,no2)
    print("Addition is:",iret)
    
    
if __name__=="__main__":
    main()