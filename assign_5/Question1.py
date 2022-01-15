# Write a program which contains one class named as Demo.  
# Demo class contains two instance variables as no1 ,no2.  
# That class contains one class variable as Value.  
# There are two instance methods of class as Fun and Gun which displays values of instance  variables.  
# Initialise instance variable in init method by accepting the values from user.   
# After creating the class create the two objects of Demo class as 
# Obj1 = Demo(11,21) 
# Obj2 = Demo(51,101) 
# Now call the instance methods as 
# Obj1.Fun() 
# Obj2.Fun() 
# Obj1.Gun() 
# Obj2.Gun()

####################################################################################
class Demo:
    def __init__(self,a,b):
        self.no1=a
        self.no2=b
        
    def Fun(self):
        print("value of no1 from Fun:",self.no1)
        print("value of no2 from Fun:",self.no2)
        
    def Gun(self):
        print("value of no1 from Gun:",self.no1)
        print("value of no2 from Gun:",self.no2)

def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    obj1=Demo(no1,no2)
    obj1.Fun()
    obj1.Gun()
    
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    
    obj2=Demo(no1,no2)
    obj2.Fun()
    obj2.Gun()

    
if __name__=="__main__":
    main()
