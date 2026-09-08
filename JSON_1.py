#..................JSON......................
#  :- ye 'javascrift' ka part hai .. or json aur programinig languange me use hota hai...
# 1) iska use data transfer ke liye hota hai...
#  2) JSON function me 'dumps' function ka bhi use hota hai..

import json

dic = {
"course": "python",
"fees": 15000,
"duretion": "2 hours"
}

print(type(dic))  #..'server' chance kiya 

l = (json.dumps(dic))
print(type(l))  #...'dictionary' ko 'string' kiya hai....
print() #....space

list = [
"king", "sam", "rohit", "abhid"
]

print(type(list))
k = json.dumps(list)
print(type(k))
