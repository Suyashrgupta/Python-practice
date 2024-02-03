li = [1,2,3,4,5]
# collection of values of any data type
lis2 = ['a', 'b', 'c']
lis3 = [1,2,'a', True]

# Data Structure - container with different pros and cons

## 1]. list slicing:-


amazon_cart = ['headset', 'controller','keyboard','kari-kari']
print(amazon_cart)
print(amazon_cart[0:2])
# prints first and second element

print(amazon_cart[0::2])
# prints starting from first element, every other element

## unlike strings, lists are mutable

amazon_cart[0] = 'laptop'
print(amazon_cart)

print(amazon_cart[:3])
print(amazon_cart[0:3])
# these two are the same

## using = to assign a list makes it share the same memory location

amazon_cart[0] = 'laptop'
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# to make a new list using list slicing

new_cart = amazon_cart[:]
new_cart[0] = 'zour bomb'
print(new_cart)
print(amazon_cart)

