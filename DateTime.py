import datetime

CurrentTime = datetime.datetime.now()
print(CurrentTime,'Version 2')

#New Block of code added in a another device to out git and we are syncing it with our git repository in our device

CurrentDate = datetime.datetime.today()
print(CurrentDate)

import inspect
print(inspect.getsource(datetime))

import json

people = {
    'name' : ['sujith', 'Sunny', 'Suneetha'],
    'city' : 'Guntur',
    'State' : 'Andhra Pradesh',
    'Role' :  [{'Inter' : 'B.Sc', 'PG': 'Microbiology and Botany'}, {'Inter' : 'MPC', 'Degree': 'B.Tech'}]
}

Storing_JSON = json.dumps(people, indent=3)
with open('myjson.json', mode='w') as f:
    f.write(Storing_JSON)