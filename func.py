def hello():
    print('hello')

hello()

print(hello) #gives memory location of function pointer

## Function arguments and parameters


def call(name, title): #parameters
    print(f"Your name is {name} and you are a/an {title}")

call('Joe','mama') #positional arguments

# default parameters

def call(name = 'Joe', title = 'nuts'):
    print(f"Your name is {name} and your title is {title}")

call()

# positional arguments

call(title="deez", name="nuts")

## Return values

def sum(n1,n2):
    return n1+n2

print(sum(92,34))

# ** A good function should focus on doing just one thing very well
# ** A function should return something

total = sum(10,2)

print(sum(10,total))


def test(num1, num2):
    def another_func(num1,num2):
        return num1 +num2
    return another_func(num1,num2)

# return keyword automatically ends the function

print(test(4,6))


### Methods vs Functions
# methods belong to a class while functions are global in scope

# Docstrings are like descriptions for functions

def test(a):
    '''
    this functions tests and prints param a
    '''
    print(a)

test('this')
# help(test) # prints out the docstring
print(test.__doc__)

# clean code example

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def is_even(num):
    return num % 2 == 0 

def is_even(num):
    return not num %2

print(is_even(50))

