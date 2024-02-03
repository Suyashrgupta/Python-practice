# tuple => immutable lists

tup = (1,2,3,4,5)

# tup[1] = 'z' throws error

# can use tuple as a key for dict

new_tup = tup[1:2]
print(new_tup)

# tuple with single item must have comma at end

x,y,z, *other = (1,2,3,4,5)

print(other)

# 1]. count returns count of a value

print(tup.count(5))

# 2]. index returns the first index of given value

print(tup.index(4))