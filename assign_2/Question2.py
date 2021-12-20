#  Write a program which accept one number and display below pattern.  
# Input : 5  
# Output : * * * * *  
#          * * * * * 
#          * * * * *  
#          * * * * *  
#          * * * * * 

##########################################################3
def Display(row,col):
    for i in range(row):
        for j in range(col):
            print("* ",end=" ")
            
        print()


def main():
    row=int(input("Enter rows:"))
    col=int(input("Enter colmuns:"))
    
    Display(row,col)
    
if __name__=="__main__":
    main()
