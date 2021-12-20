# Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

###############################################################
def Display(row,col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            if(i>=j):
                print(j,end=" ")
        print()


def main():
    row=int(input("Enter rows:"))
    col=int(input("Enter colmun:"))
    
    Display(row,col)
    
    
if __name__=="__main__":
    main()