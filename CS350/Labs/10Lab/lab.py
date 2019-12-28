'''def filmyear (year):
    movies = {   "2018, Bohemian Rhapsody": ["Rami Malek","Ben Hardy","Mike Myers","Lucy Bynton"],   "2017, Get Out": ["Daniel Kaluuya", "Allison Williams", "Catherine Keener"],   "2017 Logan": ["Hugh Jackman", "Boyd Holbrook", "Patrick Stewart"],   "2018, Black Panther": ["Chadwick Boseman", "Michael B. Jordan", "Lupita Nyong'o"],   "2016, Doctor Strange": ["Benedict Cumberbatch", "Rachel McAdams", "Ch. Ejiofor"],   "2016, La La Land": ["Emma Stone", "Ryan Gosling", "John Legend"] }
    newlist = list()
    for x in movies:
        form = x.split()[0][:-1]
    if int(form) == year:
        newlist.append(movies[x])
        '''

#[m for m in movies if m[0:4]]
# [(k, movies[k]) for k in movies if k[0:4]=="2016"]
def number2 (year):
    movies = {"2018, Bohemian Rhapsody": ["Rami Malek","Ben Hardy","Mike Myers","Lucy Bynton"],"2017, Get Out": ["Daniel Kaluuya", "Allison Williams", "Catherine Keener"],"2017 Logan": ["Hugh Jackman", "Boyd Holbrook", "Patrick Stewart"],"2018, Black Panther": ["Chadwick Boseman", "Michael B. Jordan", "Lupita Nyong'o"],"2016, Doctor Strange": ["Benedict Cumberbatch", "Rachel McAdams", "Ch.Ejiofor"],"2016, La La Land": ["Emma Stone", "Ryan Gosling", "John Legend"]}
    return [(m, movies[m]) for m in movies if int(m[0:4]) == year]

def squares():
    squares = [x**2 for x in range(12) if x%2 == 0 ]
    return squares 

def multisofTen():
    return [x for x in range(20) if x%2==0 and x%5==0]

def removebyyear(year):
    movies = ["2018, Black Panter", "2018: Bohemian Rhapsody", "2017: Get Out", "2017: Logan", "2016: La La Land", "2016: Doctor Strange"]
    return ['REMOVED FROM LIBRARY - {}'.format(x)  if x[0:4] == str(year)else x for x in movies ]

def number6():
    movies = ["2018, Black Panter", "2018: Bohemian Rhapsody", "2017: Get Out", "2017: Logan", "2016: La La Land", "2016: Doctor Strange"]
    new_list = []
    for m in movies:
        if m[0:4]=="2016":
            new_list.append('REMOVED FROM LIBRARY - ' + m)
        else:
            new_list.append(m)
    print(new_list)

    
def perfect_square(limit):
    value = 1
    while value < limit:
        yield value*value
        value += 1
foo = perfect_square(1000)

def com_perfect_square(limit):
    return (x*x for x in range(limit))

q = com_perfect_square(4)



def getDigits(n):
    return [i for i in n if i.isdigit()]

print(number2(2016))