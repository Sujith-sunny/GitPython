

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

print('This is a change that is being made in Name.py')
print('Another New change being made')

print("This is a change is made on Aug 22nd 10:20pm")
print("This is a change is made on Aug 23rd 2.50am")
print("This is a change is made on Aug 23rd 3.40am")