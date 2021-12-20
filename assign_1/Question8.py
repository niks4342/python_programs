# Write a program which accept number from user and print that number of “*” on screen.  
# Input : 5 Output : * * * * * 

######################################################################3
def Display(no):
    for i in range(no):
        print("* ")

def main():
    no=int(input("Enter the number:"))
    Display(no)
    
if __name__=="__main__":
    main()