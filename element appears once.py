#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

a = [4,1,2,1,2]
dict1 = {}


for element in a:
    if element in dict1:
        dict1[element]+=1
    else:
        dict1[element] = 1
        
one_freq = 0
        
for key,values in dict1.items():
    if values == 1:
        one_freq = key
        
print(one_freq)