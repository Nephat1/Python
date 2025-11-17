#Thursday 23rd October 2025
#A set is basically an unordered coleection of unique elements
#create a set ,there are two ways
list4=[1,2,3,4,5,2,3]
set1 =set(list4)
print(set1)
print(type(set1)) #<class 'set'>

#the set function removed the duplicate elements in list 4 which is a useful festure to have at hand
#you can aalso cretae a set by passing a raw sequence to the () funcion,like a variable
set1=set([11,12,13,14,15,15,15,11])
print(set1)
print(type(set1))

# the second way is to use curly braces
#it is available in versions of python starting with 2.7 ,so ours is
set2 = {11,12,13,14,15,15,15,11}
print(set2)
print(type(set2))
print(len(set2)) #5

#checking whether an element is or is not a member of a set
print(11 in set2)
print(10 not in set2)

# we have
print(set2)
set2.add(16)
print(set2)
set2.remove(11)
print(set2)
set2.add(16)
print(set2)

#python 3 sets - methods
set1 = {1,2,3,4}
set2 = {3,5,8}

#python defines some methodss for identifying the similarities or differences  between two sets of elements,but also other methods to better make use of this data type
#lets see them in action
#to do this we can use the intersection method
print(set1.intersection(set2)) #{3}

#and this is correct of course, because 3 is the only element which resides in both sets. This operation can be done the other way around, too
#Now let's see which elements are in set1 but not in set2
print(set1.difference(set2)) #{1, 2, 4}
#and vice versa
print(set2.difference(set1)) #{8, 5}

#to unify the two sets you can use the union method() method and the result ,also being a set,a collection of unique elements, will include elements 3 just once
print(set1.union(set2)) #{1, 2, 3, 4, 5, 8} 

#another thing you can do is remove a random element in the set using the pop() method
set1.pop()
print(set1)#removes the first element of the set
set1.pop()
print(set1)

#finally we can clear the entire set using the clear() method
set1.clear()
print(set1) #set()

#set() .. and you can see now that set1 is empty
print(type({})) #<class 'set'>

#challenge time: write a program that prompts the user for their name and scores of 5 units.the program should store the score the score a set and then output the average score in a nice format
name = input('Please enter your name: ')
math = int (input('Enter your math score: '))
english = int(input('Enter your english score: '))
science = int(input('Enter your science score: '))
history = int(input('Enter your history score: '))
art = int(input('Enter your art score: '))
#create an empty set
scores = set()
#add the scores to the set
scores.add(math)
scores.add(english)
scores.add(science)
scores.add(history)
scores.add(art)
#calculate the average score
average_score = sum(scores) / len(scores)
print(f'{name}, your average score is: {average_score:.2f}')


