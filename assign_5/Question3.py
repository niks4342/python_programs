#  Write a program which contains one class named as Arithmetic.  
# Arithmetic class contains three instance variables as Value1 ,Value2.  
# Inside init method initialise all instance variables to 0.  
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),  Multiplication(), Division(). 
# Accept method will accept value of Value1 and Value2 from user. 
# Addition() method will perform addition of Value1 ,Value2 and return result. Subtraction() method will 
# perform subtraction of Value1 ,Value2 and return result. Multiplication() method will perform multiplication 
# of Value1 ,Value2 and return result. Division() method will perform division of Value1 ,Value2 and return result. 
# After designing the above class call all instance methods by creating multiple objects.

#########################################################################################################
class Arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self):
        self.value1=int(input("Enter first  number:"))
        self.value2=int(input("Enter second number:"))
        
    def Addition(self):
        Add=self.value1+self.value2
        return Add
    
    def Subtraction(self):
        Sub=self.value1-self.value2
        return Sub
    
    def Multiplication(self):
        Mult=self.value1*self.value2
        return Mult
    
    def Division(self):
        if(self.value2==0):
            print("Invalid number , enter the valid number for division")
            return -1
        else:
            Div=self.value1/self.value2
            return Div


def main():
    obj1=Arithmatic()
    obj1.Accept()
    choice=0
    while(choice!=5):
        
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4. Division\n5. Exit")
        print("Which operation do you want to perform:")
        choice=int(input())
        
        if(choice>5):
            print("Invalid choice")
            break
        
        if(choice==1):
            ret=obj1.Addition()
            print("Addition is:",ret)
            
            
        elif(choice==2):
            ret=obj1.Subtraction()
            print("Subtraction is:",ret)
            
            
        elif(choice==3):
            ret=obj1.Multiplication()
            print("Multiplication is:",ret)
            
        
        elif(choice==4):
            ret=obj1.Division()
            if(ret==-1):
                break
            else:
                print("Division is:",ret)

            
        elif(choice==5):
            print("Thank you for using this application")
            break  
    
if __name__=="__main__":
    main()
    

