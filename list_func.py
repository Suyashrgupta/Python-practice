# length function (general methods)
basket = [3,4,'r','this']
print(len(basket))

## list specific methods

# 1]. append -> it is an inplace function
print(basket.append(100))
print(basket)

# 2]. insert -> add to list in specified index, and is also inplace
basket.insert(2,100)
print(basket)

# 3]. extend -> add another iterable to end of list (also in place)
basket.extend([2,4,'t'])
print(basket)

# 4]. pop() -> removes the element at specified index (deletes from end by default) - also returns the removed element
print(basket.pop())
print(basket)

# 5]. remove -> inplace function to delete a certain element (first instance found)
basket.remove(4)
print(basket)

# 6]. clear -> clears the list
basket.clear()
print(basket)

basket = [3,4,'r','this']
# 7]. index -> returns the first index of given element
print('r' in basket)
print(basket.index('r', 1, 3))

# 8]. count -> returns no. of occurences of a value in list
print(basket.count('r'))

# 9]. sort -> sorts list in place
basket = [3,6,7,5,8,9]
basket.sort()
print(basket)

# sorted general method

print(sorted(basket)) #returns a new array (not in place)

## copy vs reference to same list =>

# 10]. copy -> make a copy of list
list_new = basket.copy() # different list
list_new = basket[:] # also produces different list (slicing)
list_new = basket # produces a reference to the same damn list

# 11]. reverse() -> reverses the list
basket.reverse()
print(basket)
basket = basket[::-1]
print(basket)
print(reversed(basket))
 
# does the same reverse() and [::-1]