#_____ Method Overloding___,

class Area:
    def area(self, a = None, b = None):
            if (a!=None  and b!=None):                                
                print("Rectangle of Area :- ", a*b)
            
            elif (a!=None):             
                print(" Square of Area :- ", a*a)
             
            else:
                print("Nothing to find....")
                     
obj = Area()

obj.area(2,5)
obj.area()
obj.area(9)
print()#..space
print()#..space

#_____Method Overriding____


class A:    
    def viralData(self):
        print("Welcome to my world")
                               
class B(A):
    def viralData(self):
        print("Welcome to sam digit center..")

obj = B()

obj.viralData()                                                           
                                                         
                        
            
            
       