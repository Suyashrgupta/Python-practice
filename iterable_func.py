from functools import reduce

## map, filter, zip, and reduce

#1. map

def mult_2(item):
    return item*2

map(mult_2, [1,2,3])

print(list(map(mult_2, [1,2,3])))

print(list(map(lambda x: x*2, [1,4,6])))
# original list not modified

#2. filter - filter items based on a bool returning function

def check_odd(item):
    return item%2

print(list(filter(check_odd, [1,3,4,5,6,7])))
print(list(filter(lambda x:x%2, [1,2,3,4,5,6,7])))

#3. zip two iterables together to form a new one

my_list = [1,2,3]
your_list = [10,20,30]
that_list = [2,5,7]

print(list(zip(my_list, your_list)))
print(my_list)
print(dict(zip(my_list, your_list)))

print(list(zip(my_list, your_list, that_list)))
print(dict(zip(my_list,list(zip(your_list,that_list)))))

#4. reduce - collapses iterable into some value

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))
print(my_list)