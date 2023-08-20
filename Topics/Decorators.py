from functools import wraps

def Bold(fn):
    @wraps(fn)

    def wrapping(*args):
        return 'Hello' + ' Good Morning ' + fn(*args) 
    
    return wrapping

@Bold
def Greeting(myname):
    return myname

MorningGreet = Greeting('Sujith')
print(MorningGreet)