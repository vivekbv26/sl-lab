dict={1:"Hydrogen",2:"Helium",3:"Lithium",5:"Boron"}
def AtomicDictionary():							#Run another file Atomic.py and it will give same results.
	while True:							#AtomicDictionary() is being called from Atomic.py file as well.	
		print("Enter the atomic number.Enter 0 to stop :")	#At the time of run time, try giving duplicate and unique values.
		num=int(input())					#Duplicate keys wont be added, while duplicate values will be added
		if(num==0):						#Unique values will be added.
			break
		else:
			print("Enter the element name :")
			nam=str(input())
			dict.update({num:nam})
			print(dict)
	print("No of elements = ",len(dict))
	print("Enter an element to search :")
	search=str(input())
	flag=0
	for i in dict:
		if(dict[i].lower()==search.lower()):
			print("Search found :")
			print({i,dict[i]})
			flag=1 
			break
			
	if(flag!=1):	
		print("Element not found")
AtomicDictionary()