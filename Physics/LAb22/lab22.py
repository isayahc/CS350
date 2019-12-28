import json

data = 10
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

def Rows(*args):
    """returns a dictionary using args for coluns
    +make a list of keys
    +loop setting each value of an item
    +return dictionary
    + format should be (argn : n) for x amount of times
    + args of n items
    """
    dataformat = "'{}':'{}',"*(len(*args))
    return dataformat[:-1]

def makedict (n, iter):
    """makes a diction of n items from a list of values"""
    d = dict()
    for _ in range(n):
        x = Rows(iter).format(*iter,)
    

def f(n,iter):
    x = 'hell0 # {}'.format(*iter)
    print(x*n)

def listform(l):
    """prints a list""" 
    x = len(l)
    form = ("this is {}. "*x).format(*l)
    print(form)

def values(iter):
    """returns a list of inputs"""
    #for _ in range(len(iter)):

   


l = ['h','b','c']
ll = len(l)
x = Rows(l).format(*list(range(ll)),*l)


print(f(2,["a",'b','c']))
print(x)