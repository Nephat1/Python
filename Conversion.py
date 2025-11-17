num = 2
f = 2.5

str1 ='5'
int1 = int(str1)
print(int1)  # Output: 5
print(type(int1))  # Output: <class 'int'>

#integers to float
f = float(num)
print(type(f))
print(f)  # Output: 2.0
#the other way round*(float to integer)
int1 = int(f)
print(int1)
print(type(int1))  # Output: <class 'int'>

#tuple to list
tup1 = (1, 2, 3)
list1 = list(tup1)
print(list1)  # Output: [1, 2, 3]
print(type(list1))  # Output: <class 'list'>

#list to tuple
list2 = [1, 2, 3]
tup = tuple(list2)
print(tup)
print(type(tup)) #<class 'tuple'>

#list to set (create set1 from list1)
set1 = set(list1)
print(set1)  # Output: {1, 2, 3}
print(type(set1))  # Output: <class 'set'>

#The last thing i'll show you here is how to convert between different numerical representations of numbers and i am reffering to decimal, binary, hexa notation and octal systems so base-10
#bin(),hex() and oct() functions are used to convert decimal numbers to binary, hexadecimal and octal representations respectively
#binary representation
num = 10
num_bin = bin(num)
print(num_bin)  # Output: 0b1010
print(type(num_bin))  # Output: <class 'str'>
#hexadecimal representation
num_hex = hex(num)
print(num_hex)  # Output: 0xa
print(type(num_hex))  # Output: <class 'str'>

#Convert from binary, hexadecimal back to decimal
bin_str = '0b1010'
dec_from_bin = int(bin_str,2)
print(dec_from_bin)  
print(type(dec_from_bin))
#Convert from  hexadecimal back to decimal
hex_str = '0xa'
dec_from_hex = int(hex_str,16)
print(dec_from_hex)
print(type(dec_from_hex))  # Output: 10

