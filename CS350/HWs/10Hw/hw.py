from random import randint

""""
function : NGramGen 
In: list of strings, n
Out: List of Strings in random order of length n
"""

'''
1. i = [n++]
2. i in w 
3.0. add to list 
3.1 generate new number
'''

def random(iter,n):
    return [ iter.pop(randint(0,len(iter)-1)) for i in range(n)]

listform = lambda x : (("{} ")*len(x)).format(*x)

def getwords(fileName):
    file = open(fileName, 'r')
    text = file.read()
    stopletters= [".", ",", ";", ":", "'s", '"', "!", "?", "(", ")", '“', '”']
    text = text.lower()
    for letter in stopletters:
        text = text.replace(letter, "")
        words = text.split()
        return words

def compute_bigrams(fileName):
    input_list= getwords(fileName)
    bigram_list= {}
    for i in range(len(input_list)-1):
        if input_list[i] in bigram_list:
            bigram_list[input_list[i]] = bigram_list[input_list[i]]+[input_list[i+1]]
        else:
            bigram_list[input_list[i]] = [input_list[i+1]]
    return bigram_list

x = getwords('text.txt')
z = compute_bigrams('text.txt')
#init = x.copy().pop(randint(0,len(x)))


test = lambda z: x[randint(0,len(z)-1)] 
add = lambda x,y : y.append(x)
copies = lambda x,y :  (x in y)



print(x)

# for i in range(1,10):
#     pass
#     qq.append(test(qq[i-1]))

g = [ i for i in  range(10)]

# print(list(map(lambda x: x*x, g)))

# # print(list(map(lambda x: x*x, [ i for i in  range(10)])))
    
# # '''
# p= test(z[init])
# print(p)

# print(test(z[p]))
# o = test(z[p])

# print(test(z[o]))
# u = test(z[o])

# print(test(z[u]))
# y = test(z[u])

# print(test(z[y]))
# t = test(z[y])

# print(test(z[t]))
# '''

# '''def tri (init, x):
#     if x !=0:
#         (z[init])
#         return tri(test(z[init]),x-1)  

# print(tri(test(z[init]),10))'''

q = (i*i for i in range(10))
'''print(next(q))
print(next(q))
print(next(q))'''

c = list('james')
f = ( c.append(i) for i in c )
'''
print(next(f))
print(c)
print(next(f))
print(c)
print(next(f))
print(c)
print(next(f))
'''

j = init.split()

h = (test(z.get(i)) for i in j)



def hw(n):
    lis = [test(i) for i in n]

def li(init,end):
    end




g= [i for i in range(10)]
x = lambda i: g.append(i*i) 




def att (init,n):
    iterable = list()
    iterable.append(init)
    ne = iterable.__iter__()
    
         

        
    

    return iterable
        
        


print(att(init,7))
        