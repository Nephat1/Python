#The words in a certain number
list1 = []
print(type(list1)) #<class 'list'>
list1 = ['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11]
print(len(list1)) #6
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[-1])

#list updating
print(list1)
list1[2] = 'HP'
print(list1)

# list methods
list2 = [-11,2,12]
print(min(list2)) #-11
print(max(list2)) #12

list3 = ['a','b','c']
print(min(list3))
print(max(list3))

#adding a value at the end of the list
list1.append(100)
print(list1)

#1 deleting an element from a list
del list1[4]
print(list1)

#2 pop method/deletion method
list1.pop(0)
print(list1)

#3 removal method
list1.remove('HP')
print(list1)

#insertion of an element
print(list1)
list1.insert(2, 'Nortel')
print(list1)

#Interesting list operation a list to another list
list2 = [9,99,999]
list1.extend(list2)
print(list1)
print(list1.index(-11)) #3
list1.append(10)
list1.append(10)
print(list1)
print(list1.count(10)) #3
#adding elements(append)
list2.append(1)
list2.append(25)
list2.append(500)
print(list2)
#Arranging using (sort)
list2.sort()
print(list2)

#Reversing the list
list2.reverse()
print(list2)

#sorted function
list3 = sorted(list2)
print(list3)

#sorted function with reverse parameter
list3 = sorted(list2, reverse=True)
print(list3)

#Help function
print(help(sorted))

#Concatenation and replication
print(list1 + list3)
print(list2 * 3)

#Python 3 Lists - Slices

list4 = [1,2,3,'a','b','c']
#-ve indexes\slices
print(list4[-1:-7:-1])
# [1, 2, 3]
print(list4[0:3])
# [3,'a', 'b']
print(list4[2:5])
# [3, 'a', 'b', 'c']
print(list4[2:6])
# [1,2,3, 'a', 'b', 'c']
print(list4[2:])
