import re

print('\tTab')
# raw strings print strings as is
print(r'\tTab')

text_to_search = 'abcdefghaindlifahsiehfoiabc'

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  # match object shows span - beginning and end index
                  # match object shows 
    
print(text_to_search[0:3]) # slicing in the given span gives abc

# 2. special characters: [must be escaped with \ in the regular expression]
## . ^ $ * + ? { } [ ] \ ( )


new = "https//this.com"
pattern = re.compile(r'this\.com')

matches = pattern.finditer(new)

for match in matches:
    print(match)

# word boundaries

text = " Ha HaHa"

pattern  = re.compile(r'\bHa')

matches = matches = pattern.finditer(text)

for match in matches:
    print(match)

# beginning and end of a string

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'^Start')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)

pattern = re.compile(r'end$')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)

## Phone no. examples

p1 = '321-994-3456'
p2 = '990.576.2378'

# match phone no.s separated by dashes or dots

sent = f'{p1} and the no. {p2}'

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # any special char is matched

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # dashes and dots only are detected here

matches = pattern.finditer(sent)

for match in matches:
    print(match)