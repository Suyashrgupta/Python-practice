## list, set, dict comprehensions

#1. list comprehensions

my_list = []
word = 'hello'
my_list = [char for char in word]
my_list2 = [num*2 for num in range(0,100)]
my_list3 = [num for num in range(0,100) if num%2==0]
print(my_list)
print(my_list2)
print(my_list3)


for char in 'hello':
    my_list.append(char)

print(my_list)

#2. set comprehensions

my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0,100)}
my_set3 = {num**2 for num in range(0,100)}
my_set4 = {num**2 for num in range(0,100) if num%2 == 0}

print(my_set)

#3. dict comprehensions

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items()
           if v%2 == 0}
my_dict2 = {k:k*2 for k in [1,2,3]}
print(my_dict)
print(my_dict2)

# example (find duplicate items using commprehension)

some_list = ['a','b','c','d','e','d','m','n','n']

duplicates = {item for item in some_list if some_list.count(item)>1}
print(list(duplicates))