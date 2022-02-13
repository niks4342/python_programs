# Write a recursive program which accept number from user and return  summation of its digits. 
# Input : 879 
# Output : 24 

##################################################################
sum=0
def Addition(no):
    global sum
    if(no!=0):
        digit=int(no%10)
        sum=sum+digit
        no=int(no/10)
        Addition(no)
    return sum

def SmartAddition(Func_name):
    def Inner(no):
        if(no<0):
            no=-no
        return Func_name(no)
    return Inner

Addition=SmartAddition(Addition)

def main():
    no=int(input("Enter the number:"))
    ret=Addition(no)
    print("Simmation of digits iS:",ret)
    
if __name__=="__main__":
    main()