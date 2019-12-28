movies = {   
    "2018, Bohemian Rhapsody": ["Rami Malek","Ben Hardy","Mike Myers","Lucy Bynton"],
    "2017, Get Out": ["Daniel Kaluuya", "Allison Williams", "Catherine Keener"],
    "2017 Logan": ["Hugh Jackman", "Boyd Holbrook", "Patrick Stewart"], 
    "2018, Black Panther": ["Chadwick Boseman", "Michael B. Jordan", "Lupita Nyong'o"],
    "2016, Doctor Strange": ["Benedict Cumberbatch", "Rachel McAdams", "Ch. Ejiofor"], 
    "2016, La La Land": ["Emma Stone", "Ryan Gosling", "John Legend"] 
}


def printformat (movs):
    data=movies.keys()
    print(data)
    for x in movies:
        print(x, movies[x])

printformat(movies)
