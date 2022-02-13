#  Write a recursive program which accept number from user and return its  factorial.  
# Input : 5 
# Output : 120

########################################################################
fact=1
def DisplayR(no):
    global fact
    if(no>0):
        fact=fact*no
        no=no-1
        DisplayR(no)
    return fact

def SmartDisplayR(Func_name):
    def Inner(no):
        if(no<0):
            no=-no
        return Func_name(no)
    return Inner

DisplayR=SmartDisplayR(DisplayR)

def main():
    no=int(input("Enter the number:"))
    ret=DisplayR(no)
    print("Factorial is:",ret)
    
if __name__=="__main__":
    main()