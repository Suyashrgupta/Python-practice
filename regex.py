import re

print('\tTab')
# raw strings print strings as is
print(r'\tTab')

text_to_search = 'abcdefghaindlifahsiehfoiabcde'

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
    print(match.span())

    
p3 = '800-567-4583'
p4 = '900.456.2343'

sent2 = f'{p1}, {p3}, {p4}, {p2}'

pattern  = re.compile(r'[8-9]00[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(sent2)

for match in matches:
    print(match)


test_words = 'cat, mat, rat, pat, bat'
# match all words except for bat

pattern = re.compile(r'[^b]at')

matches = pattern.finditer(test_words)

for match in matches:
    print(match)


# Quantifiers used to match more than one character
    
# same pattern for matching phone numbers
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{3}')

matches = pattern.finditer(sent2)

for match in matches:
    print(match)

# Names
    
names = ''' Mr. White
            Mr. Smith
            Mr. T
            Mrs. Robinson
            Ms. Davis
'''
#1. matching for Mr

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

matches = pattern.finditer(names)

for match in matches:
    print(match)

#2 Using a group to match several different patterns (using parenthesis)

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches = pattern.finditer(names)

for match in matches:
    print(match)

## Find emails

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[\w-]+@[\w-]+\.\w+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

## Find URLS
    
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?([a-zA-Z0-9_-]+)(\.\w+)')

matches = pattern.finditer(urls)

# can substitute sections of a regular expression

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# can search for groups separately to get domain name


for match in matches:
    print(match.group(3))

# findall method returns list of tuples for each group
# match method checks for just one instance of the pattern specified at the beginning
# search method checks for just one instance of a pattern (first match found anywhere)
    
# flags example
# ignore case
    
examp = 'Start a sentence and then bring it to and end'

pattern = re.compile(r'start', re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)
