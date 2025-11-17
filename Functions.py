#A function is a reusable block of code that performs a specific task.it's like a mini-programing within you program that you can call whenever needed .Function help in organization code, avoiding repetition, and making programs more maintainable
#1. Function Basics 
#Function Definition
def greet(name):
    '''Takes a name and returns a greeting message
    
    Args
        name(str): The nameof the person to greet
        '''
    return f'Hello, {name}'
print(greet('Nephat'))
def greeting():
    print('Hello,Everyone!')
greeting()
greeting()
greeting()
greeting()

#2. Parameters and Arguments
#Parameter: Avariable that is listed in the function definition
#Arguments: The actual value passed to the function when called

#Types of parameters
#Required parameters(Positional Arguments)

def add(x, y): # x and y are required parameters
    '''Adds two numbers together'''
    return x + y

result = add(5, 3) #5 and 3are arguments
print(result)

#Default parameter
def greet_user(name = 'User'):
    '''Greet a user, using 'User' if no name provided'''
    return f'Greeting,{name}'

#Default parameter
def greet_user(name = 'User'):
    '''Greet a user, using 'User' if no name provided'''
    return f'Greeting,{name}'


#variable length arguments
#'args;collects all positional arguments into a tuple
def sum_all(numbers):
    """ sum any number of values"""
    return sum(numbers)

print(sum_all([1,2,3,4,5,6,7,8]))

#'kwargs';collects all keyword arguments into a dictionary
def print_info(**info):
    """Prints all provided keyword arguments."""
    for key, value in info.items():
        print_info(name="John Doe",age=30,city="Nairobi")


#3. Return statement
#Definiton
#The return statement is used to send a value back from a function to the caller. A function can return multiple values using tuples.

def greetings(name):
    print (f'Hello,{name}')

print(greetings('Maina'))

print(greetings('Maina'))
#single return
def square(num):
    '''returns the square of a number'''
    return num ** 2

    print(square(10))

def get_user_info():
    '''Returns multiple values about a user'''
    return 'John', 30, 'Nairobi' #returns a tuple

#unpack returned values    
name, age, city = get_user_info()
print(name, age, city)



#create a python program that uses function to display the user info in an nice format. The program should prompt the user for their name and age, and then display the name, decades, seconds lived and their age.

def get_user_input():
    name = input("Enter your name: ").strip() or "Anonymous"
    while True:
        age_str = input("Enter your age in years: ").strip()
        try:
            age = int(age_str)
            if age < 0:
                print("Age must be non-negative. Try again.")
                continue
            return name, age
        except ValueError:
            print("Please enter a valid integer for age.")

def format_user_info(name: str, age: int) -> str:
    decades = age // 10
    seconds_per_year = 365.25 * 24 * 3600  # accounts for leap years on average
    seconds_lived = int(age * seconds_per_year)
    return (
        f"Name: {name}\n"
        f"Age: {age} years\n"
        f"Decades: {decades}\n"
        f"Approx. seconds lived: {seconds_lived:,}"
    )

if __name__ == "__main__":
    name, age = get_user_input()
    print(format_user_info(name, age))

#create a function that checks if a password meets security requirements, common in user registration systems

    
import re

def validate_password(password):
    """
    Check if a password meets security requirements:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    
    return "Password is valid."
print(validate_password("Hello@123"))  
#ORR
def validate_password(password):
    '''Check if a passord meets security rewquirements:
    -Aleast 8 characters
    -Contain upper and lowercase
    -contain atleast one digit
    -contain atleast on special character'''
    import re
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
#Example usage
password = input("Enter a password to validate: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password does not meet security requirements.")

