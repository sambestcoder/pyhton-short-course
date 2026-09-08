#........   Random numbers.......

import random 

print(random.randint(2,5))
        #....'randint' aap ko 2 ya 5 ke bich me ki konsa bhi ek number deta hai...
        
print(random.randint(1,9))
print() #...space

list = [56,78,33,44,23,80,96,45]
print(random.choice(list)) 
     #.... 'choice' function ka use konse bhi number ko chuunne ke liye kiya jata hai 
     

sam = ["samrat", "krishana", "vabhai", "sima", "samiksha"]
print(random.choice(sam))