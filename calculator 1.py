# how to creat calculetar#

print('''
Addition :- +
substraction :- -
multiplycation:- *
divided:- /
into divided:- // 
''')
num1= eval(input("enter your 1st number:- " ))
num2= eval(input("enter your 2nd number:- "))
oparetor= input("enter the oparetor:- ")
if oparetor=='+':
    print(num1+num2)
elif oparetor=='-':
    print(num1-num2)
elif oparetor=='*':
    print(num1*num2)
elif oparetor=='/':
    print(num1/num2)
elif oparetor=='//':
    print(num1//num2)
else:
 print("invalid Number")
 

     