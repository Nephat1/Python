#Are another type of sequence in Python, similar to lists.
#You can consider tuples being like immutable lists.
#Once a tuple is created, you cannot change its values, add new values, or remove values.
#They maybe used to prove to br useful in situations where you want to ensure that the data remains constant and unaltered.
#Tuples are defined by enclosing the values in parentheses ()  and their elements are separated by commas.

#creating a tuple
my_tuple = ()
print(type(my_tuple))
  # <class 'tuple'>....this is an empty tuple and python confrims this, too
#If you want to create a tuple with a single element, you need to include a comma after the element, otherwise Python will not recognize it as a tuple.
my_tuple = (9)
print(type(my_tuple)) #<class 'int'>....this is an integer, not a tuple
#using a comma to create a single-element tuple
my_tuple = (9,)
print(type(my_tuple)) 
#Accessing elements in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[-1])  # Output: 5
print(my_tuple[3])  # Output: 4

#my_tuple[1] = 10  # This will raise a TypeError because tuples are immutable
tuple1 = ('Cisco', '2000', '12.4')
(vendor, model, ios) = tuple1
print(vendor)  # Output: Cisco
print(model)   # Output: 2000
print(ios)     # Output: 12.4

#This is called tuple packing and unpacking and you can see it is a kind of maping between elemrents of two different tuples.
#Remember both tuples must have the same number of elements for this to work, otherwise you will get a ValueError.
tuple2 = (1, 2, 3, 4)
(x, y, z, y) = tuple2
#friday 24th October 2025
#challenge time
#1. Build sentence from words list
words = ['I', 'enjoy', 'Learning', 'Python']
sentence = ' '.join(words)
print(sentence)  # Output: I enjoy Learning Python

#add the word 'really' between I and enjoy
words.insert(1, 'really')
sentence = ' '.join(words)
print(sentence)  #I really enjoy Learning Python


#2. Get unique words from sentence
sentence = 'the cat and the dog and the house'
unique_words = set(sentence.split())
print(unique_words) #'the', 'cat', 'and', 'dog', 'house'

#3. get common words
sentence1 = 'I love python programming'
sentence2 = 'I love java programming'
set1 = set(sentence1.split())
set2 = set(sentence2.split())
common_words = set1.intersection(set2) #also '&' can be used as intersection operator
print(common_words)  #'i','love','programming'


#4. Count vowels and consonants
sentence = 'Hello World'
vowels = 'aeiouAEIOU'
vowel_count = 0
consonant_count = 0
for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f'Vowels: {vowel_count}, Consonants: {consonant_count}') 


#5. Text Statistics
text = 'The quick brown fox jumps over the lazy dog.'
#count words
words = text.split()
word_count = len(words)
#Count characters
char_count = len(text)
print(f'Words: {word_count}, Characters: {char_count}')
#characters without spaces
char_count_no_spaces = len(text.replace(' ', ''))
print(f'Characters (no spaces): {char_count_no_spaces}')
#count sentences
sentences = text.split('.')
sentence_count = len(sentences)
print(f'Sentences: {sentence_count}')
#Count average word length
total_word_length = sum(len(word) for word in words)
average_word_length = total_word_length / word_count
print(f'Average Word Length: {average_word_length:.2f}')

#extract email from the sentence below
text = 'Contact me at user@exmple.com for more information.'
import re
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
match = re.search(email_pattern, text)
if match:
    print(f'Email found: {match.group()}')


#extract number from the text below
sentence = 'I have 5 apples and 10 oranges.'
numbers = []
words = sentence.split()
print(words)
for word in words:
    if word.isdigit():
        numbers.append(int(word))
print(numbers) 

tuples2 = (1, 2, 3, 4)
print(tuples2[0:]) #1,2,3,4
print(tuples2[::-1]) # 4,3,2,1
print(tuples2[::2]) #1,3

print(3 in tuple2)# TRUE
print(3 not in tuple2)#FALSE
print(5 in tuple2)#FALSE

#del tuple2
print(tuple2)











