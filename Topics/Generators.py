def lists(My_list):
    for i in My_list:
        yield i

Thing = lists(['Name', 'Subject', 'city', 'Firstname', 'Secondname'])
print(next(Thing), 'Version 2')
print(next(Thing), 'Version 2')
print(next(Thing), 'Version 2')
print(next(Thing), 'Version 2')
print(next(Thing), 'Version 2')