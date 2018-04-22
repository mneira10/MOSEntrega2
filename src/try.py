#dummy code for testing purposes

import numpy as np
import json, codecs
# import json

sizes = [5, 5, 10]
weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

# arr =  [[1,2,3],
#          [4,4,5]]


# arr = np.array(arr)
# print(weights)
# temp = (jt.dumps({'mydata': weights}))

# arr = jt.loads(temp)

# print(arr['mydata'])
nameOfNetwork = "net1"


a = np.arange(10).reshape(2,5) # a 2 by 5 array
b = a.tolist() # nested lists with same data, indices
file_path = "./coso.json" ## your path variable

wc = weights[:]
for i in range(len(weights)): 
    weights[i]= weights[i].tolist()

json.dump(weights, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format


#load

obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
b_new = json.loads(obj_text)
a_new = (b_new)
for i in range(len(a)):
    a_new[i] = np.array(a_new[i])

# print (a_new.==wc.all())
print (a_new)
print "===================="
print wc