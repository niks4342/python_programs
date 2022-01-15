# Write a program which contains one class named as BankAccount.  
# BankAccount class contains two instance variables as Name & Amount.  
# That class contains one class variable as ROI which is initialise to 10.5.  
# Inside init method initialise all name and amount variables by accepting the values from user.  
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),  CalculateIntrest(). 
# Deposit() method will accept the amount from user and add that value in class instance variable  Amount. 
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount  from class instance 
# variable Amount. 
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest  which is 
# Class variable as ROI. 
# And Display() method will display value of all the instance variables as Name and Amount. After designing 
# the above class call all instance methods by creating multiple objects.

#########################################################################################################

class BankAcount:
    
  
    ROI=10.5
    print("ROI(Rate of Interest) is:",ROI)
    
    def __init__(self,name,amount,withdraw,deposite):
        self.Name=name
        self.Amount=amount
        self.Depo_amou=deposite
        self.With_amou=withdraw
        
        
    def Deposite(self,deposite):
        self.Depo_amou=deposite
        self.Amount=self.Amount+self.Depo_amou

    def Withdraw(self,withdraw):
        self.With_amou=withdraw
        if(self.With_amou>self.Amount):
            print("Your withdrawal amount is greate than actul amount you have,\nyou can't withdraw")
        else:
            self.Amount=self.Amount-self.With_amou
    
    def CalculateIntrest(self):
        Intrest=(self.Amount*1*(BankAcount.ROI))/100
        print("Intrest on your anount after 1 year will be:",Intrest)
        
    def Display(self):
        print("Name is:",self.Name)
        print("Amount is:",self.Amount)
    
def main():
    name=input("Enter the name:")
    amount=int(input("Enter the initial amount:"))
    
    obj1=BankAcount(name,amount)
    
    choice=0
    while(choice!=5):
        print("1.Deposite\n2. Withdraw\n3. Calculate Interest for 1 year\n4. Display Amount\n5. Exit")
        print("Enter your choice:")
        choice=int(input())
        
        if(choice>5):
            print("Enter valid choice")
            break
        
        if(choice==1):
            Depo_amou=int(input("Enter how much amount you want to deposite: "))
            obj1.Deposite(Depo_amou)
    
        elif(choice==2):
            With_amou=int(input("Enter how much amount you want to withdraw:"))
            obj1.Withdraw(With_amou)

        elif(choice==3):
            obj1.CalculateIntrest()
    
        elif(choice==4):
            obj1.Display()
           
        else:
            print("Thank you for using this application")
            break
        
if __name__=="__main__":
    main()