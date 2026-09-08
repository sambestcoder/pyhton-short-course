#.......... Encapsulation.......
#  :- issme 'private fuction' or 'private varibles' bana sskte hai..
# 1) varibles or fuction ko private karke call koya jaye ga....
# 2) __(name)  :- isska use private varibles ko bana ne ke liye hota hai...
#  3) issme 'def' function ka bhi use hoga...
# 4) 'def' function me '__init__' aregument ka bhi use hota hai...


class student:
    __name = "Sam.. "
    def __init__(self):
        print(self.__name)
        print(self.__name)
    
obj = student() #..call karne ke liye...
print() #...space

#ex(1)

class Room:
          __room1 = [
          "Samrat", "abhay",
          "vishal"    ]
          __room2 = [
          "Ankita", "priya", "chanchal"      ]
          def __init__(self):
              print(self.__room1)#..'room1' ko call kiay...
              print(self.__room2);
                                                                
obj = Room()


     
          
          
          
          
    