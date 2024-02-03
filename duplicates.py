some_list = ['a','b', 'c', 'b','d','m','n','n']

new_list = list(set(some_list))

print(new_list)
# method 1
for i in new_list:
    if i in some_list:
        some_list.remove(i)
print(some_list)

some_list = ['a','b', 'c', 'b','d','m','n','n']

new_list = []
# method 2
for i in some_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

for i in new_list:
    if i in some_list:
        some_list.remove(i)
print(some_list)

some_list = ['a','b', 'c', 'b','d','m','n','n']

new_list = []
# method 3d
for i in some_list:
    if some_list.count(i) > 1 and i not in new_list:
        new_list.append(i)

print(new_list)