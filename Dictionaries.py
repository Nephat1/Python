#unordered set of key-value pair, separated by comma and enclosed curly

dict1 = {}
print(type(dict1)) #<class 'dict'>

dict1 = {'Vendor':'Cisco','Model':2600,'IOS': 12.4,'Ports':4}
print(dict1) #Each element consists of a key, a colon and a value, followed by comma

d1 = {1:'First Element',2:'Second Element'}
print(d1)

#Dictionaries methods
print(dict1)
print(dict1['IOS']) #12.4
print(dict1['Ports']) 
print(dict1['Model'])

dict1['RAM'] = '128'
print(dict1)
print(dict1['IOS']) 


dict1['IOS'] = 12.3
print(dict1)
#changing 12.4 to 12.3
dict1['IOS'] = 12.3
print(dict1)
#deeleting ports
del dict1['Ports']  
print(dict1)

print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

#Challenge: create a dictionary with keys a,b and c whose values are lists[1,10], [11,20] and [21,30]
dict2 = {'a':list(range(1, 11)),'b':list(range(11,21)),'c':list(range(21,31))}
print(dict2)
#extract 13 from the dictionary created
print(dict2['b'][2])






