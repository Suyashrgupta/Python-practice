name = 'Suyash'
age = 22
gym_status = 'recovery'

gym_status = 'gainz'

birth_year = input('what year were you born?: ')
print(f'your age is {2023-int(birth_year)}')

# password checker

username = input('Username: ')
password = input('password: ')
pass_hidden = '*'*len(password)
print(f'{username}, your password {pass_hidden} is {len(password)} characters long')