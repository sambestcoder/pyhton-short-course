#.... User Defined function.......
# :- 'def' funtion ka use value or string ko defined karne ke liye hota hai...
#  2)  calling function ka bhi use hota hai..:-  user value()

def n1():
    print("I am smart")

n1()   #....call kiya hai...
n1()
n1()

print()      #...space


def sum (num1,num2):
    print(num1+num2)
   
sum(45,45)   #... mene 'sum' ko call kiya hai

sum(50,50)
#.....ye addition ke case me hota hai..
print()  #....space


def add(a,b=2):
    print("addition:- ",a+b)


add(5)  #.... '5' me 'b' ki value put                   hoja yegi ...
add(5,5)
add(9) #... ek value me hi 'b' ki                        value put hoti hai
print() #....space



#...... 'return' me print function ka use hota hai...
#...:- 'return' ka matalb konsi value ko usapar store karta hai..

def square(s):
    return s*s #...isska use us value ko uspar applied karna..
    
print(square(5)) #....issme call karne ki zaturat nahi hai..
print() #....space


def  mul(k):
    return k*k
    
print("multiplaction:- ",mul(9))


def add(add):
    return add+add
    
print("addition:- ", add(5))
print("addition:- ", add(12))















