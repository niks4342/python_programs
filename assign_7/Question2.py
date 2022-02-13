#  Write a recursive program which display below pattern.  
# Input : 5 
# Output : 1 2 3 4 5 

##################################################

def DisplayR(no):
    
    if(no!=0): 
        DisplayR(no-1)# Backtracking 
        print(no,end=" ")
        
def main():
    no=int(input("Enter the number:"))
    DisplayR(no)
    
if __name__=="__main__":
    main()