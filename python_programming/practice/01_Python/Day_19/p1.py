# serialization and deserialization


import json 
l = [1, 2, 3, 4, 5]

with open('demo.json', 'w') as f :
    json.dump(l,f)



# dict  

d = {
    'name' : 'yogesh',
    'age' : 21,
    'gender' : 'male'
}

with open('demo.json', 'w')as f :
    json.dump(d,f,indent=4) 


# deserialization

import json

with open('demo.json','r') as f :
    d = json.load(f)
    print(d)
    print(type(d))


#serialize and deserialize tuple

import json 

t = (1,2,3,4,5)

with open ('demo.json','w') as f :
    json.dump(t,f)