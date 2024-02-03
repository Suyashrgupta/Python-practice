print(len('hellooo'))
print('this'[0:-1])

# String methods

quote = 'to be or not to be'

quote.upper()
quote.lower()
quote.swapcase() #swaps capital and lowercase letters
print(quote.capitalize()) # first letter capitalized
print(quote.title()) # each word is capitalized
print(quote.find('be'))
print(quote.replace('be', 'see'))
quote_2 = quote.replace('be', 'see')

print(quote) # the string is not mutated in the above function (immutable)
print(quote_2)

print(chr(65)) # chr function automatically converts ASCII values to characters.
print(ord('A')) # ord function gives ASCII value of given character
j = [3,4,5]
