print('''
Addition:- '+'
Substraction:- '-'
Multiplycation:- '*'
division:- '/'
into division:- '//'
''')
num1=eval(input("Enter the first value:- "))
num2=eval(input("Enter the second value:- "))
oparetor=input("Enter your sign:- ")

if oparetor=='+':
      print("your answer:- ", num1+num2)
if oparetor=='-':
      print("your answer:- ", num1-num2)
if oparetor=='*':
      print("your answer:- ", num1*num2)
if oparetor=='/':
      print("your answer:- ", num1/num2)
if oparetor=='//':
      print("your answer:- ", num1//num2)
if oparetor!='+' and oparetor!='-' and oparetor!='*' and oparetor!='/' and oparetor!='//':
      print("wrong Number/sign")
