age = 18
if age<18:
    print('Minor')
elif age == 18:
    print('Just eligible')
else:
    print('Adult')
age = 20
if age<18:
    print('Minor')
elif age == 18:
    print('Just eligible')
else:
    print('Adult')
print('Hey there, my name is %s and i am %f years old' %('Nephat', 20))
#print('Hey Mrs %s, you have been hired as a %d in our %f department and your salary is 50000' %('Nephat', 'Engineer', 'IT', 50000))

import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed(0)
bgcolor("black")
color("red")
pensize(2)

for i in range(6000):
    x = hearta(i/100) * 20
    y = heartb(i/100) * 20
    goto(x, y)
    dot(3)

hideturtle()
done()

emails = ['alice@example.com','bob@test.org','carol@sample.com']
usernames =[email.split('@')[0]for email in emails]
print(usernames)