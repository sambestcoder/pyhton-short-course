#.…......…Random Number guessing game.................

import random
cnum = (random.randrange(1,101))
user = int(input("Enter your number :-  "))

if cnum>user:
    print("computer number:- ",cnum)
    print("computer number is high..")

if user>cnum:
     print("computer number:- ",cnum)
     print("computer number is low....")

if user==cnum:
    print("your number and computer number is equal...")