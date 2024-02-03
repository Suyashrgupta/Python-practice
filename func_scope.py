##Scpe - what variables you have access to

# functional scope

def some_func():
    total = 100
    print(total)
# total variable is only accessible in the function
    
some_func()

# example

a = 1

def confusion():
    a = 5
    return a

print(a) #1
print(confusion()) #5

#1 - start with local
#2 - check parent local socpe
#3 - check global scope
#4 - check built in python fumctions

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent()) # parent local scope

def parent():
    def confusion():
        return sum
    return confusion()

print(parent()) # built in python scope function


## Global keyword

def confusion(b):
    print(b)  # local variable b

confusion(20)

total = 0

# define global variable in function 

def count():
    global total
    total += 1
    return total

# dependency injection

def count(total):
    total += 1
    return total


print(count(count(count(total))))

## non local keyword

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal' # the x in parent function gets changed
        print("inner:", x)

    inner()
    print("outer: ", x )

outer()