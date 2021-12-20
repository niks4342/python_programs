#  Write a program which accept one number and display below pattern.  
# Input : 5  
# Output :  * * * * *  
#           * * * *  
#           * * *  
#           * *  
#           * 

##############################################################
def Display(row,col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            if((i+j<=col+1)):
                print("* ",end="")
        print()

def main():
    row=int(input("Enter rows:"))
    col=int(input("Enter colmuns:"))
    
    Display(row,col)
    
if __name__=="__main__":
    main()