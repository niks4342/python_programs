# Write a program which display first 10 even numbers on screen.  
# Output : 2 4 6 8 10 12 14 16 18 20 

######################################################
def DisplayEven(value):
    for i in range(1,value+1):
        print(i*2)

def main():
    no=int(input("Enter the number:"))
    DisplayEven(no)
    
if __name__=="__main__":
    main()