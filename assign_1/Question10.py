# Write a program which accept name from user and display length of its name.  
# Input : Marvellous Output : 10 

#########################################################
def DisplayLength(name):
    return len(name)


def main():
    name=input("Enter the name:")
    ret=DisplayLength(name)
    print("Length of entered word/name is:",ret)
    
if __name__=="__main__":
    main()