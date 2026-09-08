
#..........Dictionary fuctions..........
#  use :-  update ,  clear, del...

ep1 = {67: 567, 
78: 234, 
90: 567}

ep2 = {45: 259,  70: 678}

ep1.update(ep2)
print(ep1)
print()  #...space
#.....  ep1 ki value ko ep2 me upadate kiya ....

marks_9th = {"shubham": 9, 
"sakshi": 45, 
"samiksha": 20}

marks_10th = {"sam": 100, 
"rohit": 90,  
"vinay": 56}

marks_10th.update(marks_9th)
print("marks_9th:- ",marks_9th)
print() #....space

#______________clear____________    clear :- ke issme sab kuch clear ho jata hai...

par1 = {67: 567, 
78: 234, 
90: 567}

par2 = {45: 259,  70: 678}

par1.clear()  #....par1 ki sari value                          clear ho gayi 
print(par1)
print(par2)
print() #....space

#_____________del_______________

# del:- kaa use dictionary me ke value ko delete karna hota hai....

value = {"five": 5, "six": 6,
"thousand": 1000,
"five thousand": 5000}

del value["six"]  #.. six name ke                          key ko delete kiya hai 
print(value)
print()  #....space

del value["five thousand"]
print(value)
print()   #....space

#_____________ get________________ use :- isska use dictionary me ke 'key' ke value nakalta hai...

d = {"rohan": 24, 
"krishana": 89,
"vishal": 70}

print(d.get ("vishal")) # 'key' ki                                       value nakali .....
print(d.get("rohan")) 

print(d.get("krishana"))





