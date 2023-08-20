import datetime

CurrentTime = datetime.datetime.now()
print(CurrentTime,'Version 1')

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