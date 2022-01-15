def Perfect(no):
    
    i=1
    sum=0
    while(i<no):
        if(no%i==0):
            sum=sum+i
        i=i+1
    if(sum==no):
        print("Perfect")
    else:
        print("Not perfect")

def main():
    no=int(input("Enter the number:"))
    Perfect(no)
    
if __name__=="__main__":
    main()