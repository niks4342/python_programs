# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204 

####################################################################################
from functools import reduce

FilterX=lambda no:(no%2==0)

MapX=lambda no:(no**2)

ReduceX=lambda no1,no2:(no1+no2)

def main():
    data=[]
    size=int(input("Enter the size of list:"))
    
    for i in range(size):
        data.append(int(input("Enter element:")))
    print("Your enterd list is:",data)

    newdata=list(filter(FilterX,data))
    print("Data after filter is:",newdata)
    
    Incrementdata=list(map(MapX,newdata))
    print("Data after maping(by finding square) is:",Incrementdata)

    ret=reduce(ReduceX,Incrementdata)
    print("Data after reducing(Addition of filterd and maped data) is:",ret)

if __name__=="__main__":
    main()