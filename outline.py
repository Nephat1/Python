print("Hello python!")



a = "Cisco Switch"
print(a.index('i')) 
print(a.count('c'))
print(a.find('sco'))
print(a.lower())
print(a.upper())
print(a.startswith('C'))
print(a.endswith('h'))

b = '   Cisco Switch   '
print(b.strip())

c = '$$$Cisco Switch$$$' 
print(c)   
print(c.strip('$'))

b.replace(' ', '')
print(b.replace(' ', ''))

d = 'Cisco,Juniper,HP,Avaya,Nortel'
print(d.split(','))
aa= 'Cisco Juniper HP Avaya Nortel'
print(aa)
print(aa.split(' '))
print('_'.join('Cisco Switch'))

x = 'Cisco'
y = ' Switch'
print(x + y)
print(x * 5)
print('Your product goes here....')
print('======' * 20)

print('o' in x)
print('o' not in y)
print('a' in x)

'Cisco model: 2600XM, 2 WAN slots, IOS 12.4'
print('Cisco model: %s, %d WAN slots, IOS %f' % ('2600XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %f' % ('2691XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %f' % ('7200XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %f' % ('1841XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %.1f' % ('2600XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %.2f' % ('2691XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %.3f' % ('7200XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %.4f' % ('1841XM',2, 12.4))
print('Cisco model: %s, %d WAN slots, IOS %.0f' % ('1841XM',2, 12.4))

num1 = 10
num2 = 2.5

print(type(num1))
print(type(num2))
#addition
print(1 + 2)
#subtraction
print(2-1)
#division
print( 5/2)
#multiplication
print(2 * 3)
#raising to power
print(4 ** 2)

print("Hey Nephat, you have lived for 1 decade and 5916892892seconds which means you are 19years old.") 

name = input('Nephat:')
age = int(input('20:'))
#compute decade(s) lived 1 decade =  10 19yrs = 1 decade
decade_lived = age // 10
#seconds decade lived
seconds_lived = age * 31557600
#display output
print(f'Hey {name}, you have lived for {decade_lived} decade(s) and {seconds_lived} seconds which means you are {age}years old.' )
print("Hey %s, you have lived for %f decade(s) and %g seconds which means you are %i years old." % (name, decade_lived, seconds_lived, age))

triplets = (function(find_pythagorean_triplets(50)))
print("Pythagorean triplets with values less than 50:")
for t in triplets:
    print('triplets',t)
#not equal (!=)
#greater than or equal (>=)
#less than or equal (<=)

#user credentials
name = 'Nephat'
password = 'pas$$w0rd'
#user login credentials
user_name = 'nephat'
user_password = 'pas$$w0rd'
#login the user
if((username == user_name) and (password == user_password))
    print('Login successful. Welcome %s' % user_name)
else:
    print('Login failed. Please try again.')
