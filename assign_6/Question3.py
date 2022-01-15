# Write a program which contains one class named as Numbers.  
# Arithmetic class contains one instance variables as Value.  
# Inside init method initialise that instance variables to the value which is accepted from user.  
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),  Factors(). 
# ChkPrime() method will returns true if number is prime otherwise return false. ChkPerfect() method will 
# returns true if number is perfect otherwise return false. Factors() method will display all factors of 
# instance variable. 
# SumFactors() method will return addition of all factors. Use this method in any another method  as a 
# helper method if required. 
# After designing the above class call all instance methods by creating multiple objects. 

#################################################################################################
class Number:
    
    def __init__(self,value):
        self.no=value
        
    def CheckPrime(self):
        flag=True
        i=2
        if(self.no==1):
            flag=False
            
        while(i<self.no):
            if(int(self.no%i)==0):
                flag=False
                break
            i=i+1
        return flag
                
    def CheckPerfect(self):
        i=1
        sum=0
        flag=False
        while(i<self.no):
            if(self.no%i==0):
                sum=sum+i
            i=i+1
                
        if(sum==self.no):
            flag=True
            
        else:
            flag=False
            
        return flag

    
    def SumFactor(self):
        i=1
        sum=0
       
        while(i<=self.no):
            if(self.no%i==0):
                sum=sum+i
            i=i+1
            
        return sum        
    
    def Factor(self):
        fact=[]
        i=1
        while(i<=self.no):
            if(self.no%i==0):
                fact.append(i)
            i=i+1
        return fact

def main():
    no=int(input("Enter the number:"))
    choice=0
    obj=Number(no)
    
    while(choice!=5):
        print("1. CheckPrime\n2. CheckPerfect\n3. Sum of Factors\n4. Factors\n5. Exit") 
        choice=int(input("Enter your choice:"))
        
        if(choice>5):
            print("Invalid choice")
            break
        
        if(choice==1):
            ret=obj.CheckPrime()
            if(ret==True):
                print("Number is prime")
            else:
                print("Number is not prime")
        
        elif(choice==2):
            ret=obj.CheckPerfect()
            if(ret==True):
                print("Number is perfect")
            else:
                print("Number is not perfect")
        
        elif(choice==3):
            iret=obj.SumFactor()
            print("Sum of factor(including that number) is:",iret)
    
        elif(choice==4):
            data=obj.Factor()
            print("Factors of given numbers are:",data)
            
        elif(choice==5):
            print("Thank you for using this application")
            break
            
if __name__=="__main__":
    main()