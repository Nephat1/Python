
fruits = ['Apple','banana','cherries']
for fruit in fruits:
    print(fruit)

#iterate through a string
word = 'Python'
for letter in word:
    print(letter)

coordinates = (10,20,30)
for value in coordinates:
    print(f'value is:{value}')

values = range(0, 6)
for value in values:
    print(value)
#write a program using for loop that stores odd numbers between 1-30
numbers =range(1, 30,2)
for number in numbers:
    print(number)
#or
odd_number=[]
for number in range(1,31):
    if number % 2 != 0:
        odd_number.append(number)
print(odd_number)
#or
odd_number=[number for number in range(1,31)
            if number % 2 == 1]
print(odd_number)

#The while loop - a while loop is repeadily executes a block of code as long as a specific condition remains True.
#syntax
#while condition
    #code to execute while condition is True
    #statement1
    #statement2
#the condition is checked before each iteration
#if the condition is initially false the loop will not execute

count = 0

while count < 5:
    print(f'count: {count}')
    count  += 1 #same as count = count +1
    print('Loop finished')

#0 2 4 6 8 10
count = 0
while count <= 10:
    print(count, end=' ')
    count +=2
   # print(f'count:{count}'

#10,9,8,7,6,5,4,3,2,1
count = 10
while count >= 1:
    print(count) 
    count -= 1
    print(f'count:{count}')
#-30,15,0,15,30
n = -30
result = []
while n <= 30:
    result.append(str(n))
    n += 15
print(' '.join(result))  

num =-30
while num<=30:
    print(num)
    num+=15

#creating password
#password = '' 
#password =input('Enter password:')
#while password != 'Secret':
    #if password !='Secret':
       # print('Incorrect password,please try again!')
#print('Acces granted!')
#Bad count
#count = 0
#while count< 5:
   ## print(count)
    #forget to implement counter

#Bad-condition that never changes#
#While True: 
    # print ('This runs forever')
#to stop an infinite  loop  in terminal ,press ctrl+c

#Loop control statements
#The break statement
#Definition: break statement immeditely terminates the loop and transfers control to the statement after the loop

#Find the first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print('First even number',num)
        break
    print(f'checking:{num}')

list1 = [4,5,6]
list2 = [10,20,30]
for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i*j)
print('outside the nested loop')

#now lets have a look at the continue statement
#When python stumbles upon a continue statement inside a for or while loop, it ignores the rest of the code below, for the current iteration, goes up to the top of the next loop and immediately starts the next iteration
 
for number in range(10):
    if number == 5:
        continue
    print(number)

#create a time table of your number of choice
num = int(input(f'Enter a number to generate a timestable: '))
for i in range (1, 13):
    product=num*i
    print(f'{num} x {i} = {product}')

#complete timestable
for x in  range(1, 13):
    for y in range(1, 13):
        print(f'{x}X{y}={x*y}')
    print('==' * 10)

#Exceptions
#you may encounter two main types of errors: syntax errors and exceptions
#Syntax happens when you don't follow python's syntax and maybe you forget to add a colon,or the indentation is not proper

for i in range(5):
    try:
        print(i/0)
    except ZeroDivisionError as e:
        print(e,'--> Division by 0 is not allowed,soory!')
        for i in range(5):
            try:
                print(i/1)
            except ZeroDivisionError:
                print('Division by 0 is just wrong!')
            except NameError:
                print('Name error detected!')
            except ValueError:
                print('Wrong Value')






