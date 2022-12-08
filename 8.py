from functools import reduce
list=[]
list1=[]

n = int(input("enter the number of elements:"))
for i in range(0,6):
    ele=int(input())
    list.append(ele)

print(list)
list1=[x*3 for x in list]
print(list1)
listsum = reduce(lambda a,b:a+b,list)
print("the sum of lists is",listsum)
listsum1= reduce(lambda c,d:c+d,list1)
print("the sum of list 2 is ",listsum1)

