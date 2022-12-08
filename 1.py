lst = []

# number of elements as input
n = int(input("Enter number of elements : "))
print("Enter the elements")

# iterating till the range
for i in range(0, n):
	ele = int(input())


	lst.append(ele)                     # adding the element

print(lst)

largest_number = lst[0]
 
for number in lst:                      #to find the largest number in list
    if number > largest_number:
        largest_number = number
print("the largest element is ")
print(largest_number)

smallest = lst[0]
for number in lst:
    if number < smallest:               #to fine the smallest number in the list
        smallest = number
print("the smallest number is ")
print(smallest)

i = int(input("enter the number to know its existence"))    
if i in lst:
    print("exist")
else:
    print("not exist")

n = int(input("enter the number to be inserted"))
lst.append(n)                            #to append new number to the list
print(lst)

m = int(input("enter ement to be removed"))
lst.remove(m)                            #to remove an element
print(lst)