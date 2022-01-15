# .Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64 

#######################################################################################
Power=lambda no:no**2
    

def main():
    no=int(input("Enter the number:"))
    iret=Power(no)
    print("Power of given number is:",iret)
    
if __name__=="__main__":
    main()