# *args and **kwargs

# 1]. *args takes in a tuple of arguments (any len)


def super_func(*args):
    # print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

# 2]. **kwargs takes in a dictionary of names arguments

def super_func(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total 

print(super_func(1,2,3,4,5, num1=5, num2=10))


## Important
# Order of parameters
#Rule: params, *args, default parameters, **kwargs
