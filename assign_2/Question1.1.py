import arithmatic

def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    print("Enter your choice:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice=int(input("Choice is:"))
    
    if(choice==1):
        
        ret=arithmatic.Addition(no1,no2)
        print("Addition is :",ret)
        
  
    elif(choice==2):
        ret=arithmatic.Subtraction(no1,no2)
        print("Subtraction is:",ret)
    
    
    elif(choice==3):
        ret=arithmatic.Multiplication(no1,no2)
        print("Multiplication is:",ret)
    
        
    elif(choice==4):
        ret=arithmatic.Division(no1,no2)
        print("Division is:",ret)
       
        
    
if __name__=="__main__":
    main()