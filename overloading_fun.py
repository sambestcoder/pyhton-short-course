#            Over Loading
# :- kisi bhi 'string' ya 'numbers' ko bar bar likhana....

class A:
    def screen1(self, name = ' '):
        print("welcome to sam world.." +name) # or ke string jodne ke liye....
        
obj = A()
obj.screen1() #...call kiya   
#... string jodne ke liye likha hai...
obj.screen1('i am sam')
print()#..space

#ex(1)

class B:
    def display(self, name = ' '):
          print("i Am "+name)
          
    
obj = B()   
obj.display('Sam')
print()#..space


