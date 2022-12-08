from collections import Counter
from functools import reduce

def wordcount(fname):
     with open(fname) as f:
        return Counter(f.read().split())


d=wordcount("lose_yourself.txt")

print(d)
print(type(d))
lst=list(d.items())

lst.sort(reverse=True,key=lambda x:x[1])
print("the top 10 mst occuinr words are")
list2=[]

for i in range(10):
    print(lst[i][0],"\n")
    list2.append(lst[i][1])
avg = reduce(lambda a,b:a+b , list2)/len(list2)
print("the average is",avg)

list2=[x*x for x in list2 if x%2!=0]
print("the final list is ",list2)




