

def palindrome():
    name = 'Sujith Sunny'
    if name[::-1] == name:
        print('The given name {} is palindrome'. format(name))
    else:
        print('The given name {} is not a palindrome'. format(name))


palindrome()


company = "Lucid Motors"

First = company[:5]
Second = company[6:]

print(First,'\n',Second)

for i in Second:
    if i == ' ':
        Second.strip()

print(Second)

import math
Given_Number = 5

print(math.factorial(Given_Number))