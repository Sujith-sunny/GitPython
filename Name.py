

def palindrome():
    name = 'Sujith Sunny'
    if name[::-1] == name:
        print('The given name {} is palindrome'. format(name))
    else:
        print('The given name {} is not a palindrome'. format(name))


palindrome()