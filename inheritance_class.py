#__________Inheritance_________

#:- issme hum dono kono ko call kar sakte hai...
#    ex(1)  :-  class(A) ke function aur class(b) ke function dono ko call kar sakte hai...

class A:
    def screen1(self):                   
         print("sam is smart.....A")
         #...'self' ye ek aregument hai aur ye dena zaruri hai....

class B(A):
    def screen2(self):
        print("sam is smart.....B")
           
obj = B()  #...call karna chalu hai

obj.screen1() #..call kiya
obj.screen2()  #...call kiya 

#...multipling.. ka use kare :-

class C(B):
    def screen3(self):
        print("sam is smart .... C")

obj1 = C()  #...call karne ke liye                 
obj1.screen3()  #..call kiya 'screen'
obj1.screen3() 
print()    #...space 

#___________Multiple___________#
         
class s1:
    def display1(self):
        print("Addition (50 + 50) :- ", 50 + 50)
                   
class s2:
    def display2(self):
        print("Substraction(60 - 30):- ", 60 -  30)

class s3(s1,s2):  #...multiple..
    def display3(self):
        print("Multiplication(6 * 7):- ", 6 * 7)
        
dis = s3()   #...call karna chalu hai..

dis.display1()  #...call kiya              
dis.display2()   #...call kiya  
dis.display3()    #....call kiya  
        
                                        