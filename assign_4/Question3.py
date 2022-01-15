# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000 

###############################################################################################
from functools import reduce

FilterX=lambda no:(no>=70 and no<=90)

MapX=lambda no:(no+10)

ReduceX=lambda no1,no2:(no1*no2)

def main():
    data=[]
    size=int(input("Enter the size of list:"))
    
    for i in range(size):
        data.append(int(input("Enter element:")))
    print("Your enterd list is:",data)

    newdata=list(filter(FilterX,data))
    print("Data after filter is:",newdata)
    
    Incrementdata=list(map(MapX,newdata))
    print("Data after maping(incrementing by 10) is:",Incrementdata)

    ret=reduce(ReduceX,Incrementdata)
    print("Data after reducing(multiplication of filterd and maped data) is:",ret)
    
if __name__=="__main__":
    main()