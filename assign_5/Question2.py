#  Write a program which contains one class named as Circle.  
# Circle class contains three instance variables as Radius ,Area, Circumference.  That class contains one class variable 
# as PI which is initialise to 3.14.  
# Inside init method initialise all instance variables to 0.0.  
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,  
# CalculateCircumference(), Display(). 
# Accept method will accept value of Radius from user. 
# CalculateArea() method will calculate area of circle and store it into instance variable Area. CalculateCircumference()
# method will calculate circumference of circle and store it into instance  variable Circumference. 
# And Display() method will display value of all the instance variables as Radius , Area,  Circumference. 
# After designing the above class call all instance methods by creating multiple objects. 

##################################################################################
class Circle:
    PI=3.14
    
    def __init__(self):
        self.Radius=0.0
        self.area=0.0
        self.circum=0.0
        
    def Accept(self):
        self.Radius=float(input("Enter the radius:")) 
        
    def Area(self):  
        self.area=Circle.PI*self.Radius*self.Radius
       
    
    def Circum(self):
        self.circum=2*self.PI*self.Radius
        
    def Display(self):
        print("Area of circle is:",self.area)
        print("Circumference of circle is:",self.circum)
        
        
def main():
    #radius=float(input("Enter the radius of circle:"))
    
    obj1=Circle()
    obj1.Accept()
    
    obj1.Area()
    
    obj1.Circum()
    obj1.Display()
    
if __name__=="__main__":
    main()