#....Nesten function in dictionary...

classroom = {
         "class1": {"samiksha": 45, "priti": 43, "priya": 89},
         
        "class2": {"sumit": 80, "rahul": 42, "amit": 90},
                
        "class3": {"om": 23, "radhika": 22, "vishal": 67, "abhay": 56}
             
}

print()     #......space
print(classroom["class2"]) 
                   #... 'class2' ko print kiya
print()   #....soace              
print(classroom["class1"])
print()    #......space


print(classroom["class2"] ["sumit"])   #...'class2' me se key 'sumit' ki value nikali....
print()  #....space

print(classroom["class3"] ["abhay"])
print()     #....space

#...................Update karna .........

room = {
         "room1": {"samiksha": 456, "priti": 4377, "priya": 8977},
         
        "room2": {"sumit": 80, "rahul": 4256, "amit": 9034},
                
        "room3": {"om": 2367, "radhika": 2223, "vishal": 6709, "abhay": 5600}
           
}

room["room2"] ["rahul"] = 5555
      #....'room2' me se 'rahul' ki value ko change kiya 5555 me....

room["room1"] ["priya"] = 6485      
room["room3"] ["vishal"] = 12345
print(room)

print()  # space 

# sabhi class ko ek sath print karna...

for a in classroom:
    print(a, classroom[a])
