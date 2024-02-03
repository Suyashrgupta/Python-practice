basket = ['a','d','e','f','h','y']

## len used commonly
print(len(basket))

## list slicing for reversed
basket.sort()
print(basket[::-1])

nw_list = list(range(1,100))
print(nw_list)

## add list items to string using join

sentence = ' '
new_sentence = sentence.join(['name', 'is', 'jojo'])
print(new_sentence)

## list unpacking

basket = [1,2,3]
a,b,c, *other, d  = [1,2,3,4,5,6,7,8,9]

print(a,b,c)
print(other)
# other becomes a list of items after 1,2,3, and before 9
# similar to *args and **kwargs