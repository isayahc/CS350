import sys 
from random import randint as Randit

#n = int(sys.argv[1])
def tri(n):
    for c in range(1,n):
        for b in range(1,c):
            for a in range(1,b):
                if(a*a +b == c*c):
                    print('{}, {}, {}'.format(a,c,b))
                    

def product(a=1,b=1,c=1,d=1,e=1,f=1,g=1,h=1,i=1,j=1):
    x= [a,b,c,d,e,f,g,h,i,j]
    sum = 0
    for i in x:
        i*=sum
    return sum


def game():
    atributes = ['person','exclaimation', 'verb', 'place','noun']
    gen = [i for i in range(len(atributes))]

    d = dict ({0:"person", 1:"exclaimation",2:"verb", 3:"place", 4:"noun"})
    storylist = [0,1,2,2,3,3,4,2,4,1]
    newlist = list()

    for i in storylist:
        newlist.append(input("please input a {}: ".format(d[i]) ))

    x = "We live on a like. Today {} tested the ice. {} it's frozen! Now i am off to {} my skates. I {} in the {}, not there. I {} in the {}, not there. I look in the {}, nope not there. I search high and low for my ice {}. ok so the one place i haven't looked, {} my {}. {} they are there! ".format(*newlist)
    return x
    
    
    


def loterry():
    answer =set (Randit(1,44) for i in range(5))
    user = set([input("please pick for number {} : ".format(i+1)) for i in range(5)])
    print("Nice try, human. The winning numbers are {} {} {} {} {}".format(*answer))
    
    if(answer == user):
        print("CONGRATULATIONS! YOU WON THE LOTTERY!")


 
        



        






