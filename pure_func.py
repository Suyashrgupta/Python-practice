## Pure function rules
#1 they return the same output for the same input everytime
#2 they should not produce side effects in the program or interact with objects outside the function

# example

def mult_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    print(new_list) # this is impure (using outside print)
    return new_list

print(mult_2([1,2,3,4]))