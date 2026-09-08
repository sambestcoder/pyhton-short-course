#    List fuction......#

l = [45,67,89,44,66,7]
print(len(l))
print() #...space. .
for k in range (len(l)):
	print(l[k], k)
print() #...space..
#..... 'list' ke andhar ke sare number ke index number nikale.......
del l[3]
print(l)  #.... '44' ko delete kiya                       hai......
print()   #...space....#
print()   #...space....#


list = [ "sam", "rohit", "aditay", "abhay", "pratham"]
del list[2]
print(list)  #...'aditay' ko delete kar diya hai ....#
print()   #...space....#
print()   #...space....#


sam = [11,22,33,44,55,66,77,88]
sam.remove(66)
print(sam)
print()  #..space..
#.... '66' ko remove kiya hai .......... issme 'index no.' ka use nahi hota hai ......

k = ["free fire", "call of cuty", "pubg", "GTA 5"]
k. remove("GTA 5")
print(k)
print()   #...space....#
print()   #...space....#


G = [ 2, 4, 5, 6, 78]
G[4] = 7    # 78 = change = 7
print(G)
print() # ........space 
#...'list' ke andhar ki value ko update kiya ....

classroom = [ "samrat", "vinay", "harshal", "abhay", "sumit", "vikas"]
print(classroom.index("sumit"))
classroom [4] = ("priyanka")
print(classroom)
print()   #...space....#
print()   #...space....#
#...'sumit' ke jagapar 'priyanka' ko laya.....#



