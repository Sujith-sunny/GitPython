from functools import wraps

def Bold(fn):
    @wraps(fn)

    def wrapping(*args):
        return 'Hello' + ' Good Morning, ' + fn(*args) 
    
    return wrapping

#This new decorator is made in the downloaded folder and we need to sync this back to the main git folder 

def Italic(fn):
    @wraps(fn)
    def wrapping(*args):
        return 'How are you' + ' Doing Mr. ' + fn(*args)
    return wrapping

@Bold
@Italic
def Greeting(myname):
    return myname

MorningGreet = Greeting('Sujith')
print(MorningGreet)