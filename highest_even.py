def highest_even(li):
    max = -10000
    for i in li:
        if(i%2==0 and i>max):
            max = i
    return max

l = [1,3,5,7,12,47,56,88,120,33,34]

print(highest_even(l))