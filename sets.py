# set -> unordered collection with only unique elements

my_set = {1,2,3,4,5}

print(my_set)

set2 = {1,2,3,3}
print(set2)
set2.add(100)
set2.add(2)
print(my_set)

lis = [1,2,3,4,5,5,6,6]
print(set(lis))

new_set = my_set.copy()
new_set.clear()
print(my_set)
print(new_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# 1]. difference() gives the elements in myset but not in yourset

print(my_set.difference(your_set))

# 2]. discard() inplace function to remove an element from set

my_set.discard(5)
print(my_set)

# 3]. difference_update -> inplace function to remove the differences between sets

#my_set.difference_update(your_set)
print(my_set)

# 4]. intersection -> gives common elements between sets

print(my_set.intersection(your_set))
print(my_set & your_set)

# 5]. isdisjoint() -> checks if sets have no intersection

print(my_set.isdisjoint(your_set))

# 6]. issubset()

print(my_set.issubset(your_set))

# 7]. issuperset()

print(my_set.issuperset(your_set))

# 8]. .union() joins the two sets

print(my_set.union(your_set))
print(my_set | your_set)