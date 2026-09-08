
#.......... 'Zip'  ka istamal 'list' ke liye hi hota hai......


list = [10,20,30,40,50,60,70]
list2 = ["one", "two", "three", "four"]

for n1,n2 in zip(list,list2):
	print(n1,n2)
print()  #...space..

for k in range(len(list)):
	print(list[k], k)
print()  #....space...

for m in range(len(list2)):
	print(m)
