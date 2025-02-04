movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Task1
def score(movie_name):
    for movie in movies:
        if movie["name"] == movie_name:
            if movie["imdb"] > 5.5:
                return True
            return False
movie_name = input()
print(score(movie_name))

#Task2
def scores(movies):
    arr = []
    for movie in movies:
        if movie["imdb"]>5.5:
            arr.append(movie["name"])
    return arr
print(scores(movies))

#Task3
def categories(name_category):
    a = []
    for movie in movies:
        if movie["category"]==name_category:
            a.append(movie["name"])
    return a
name_category = input()
print(categories(name_category))

#Task4
arr2 = []
def imdb_score(arr1):
    for i in arr1:
        for movie in movies:
            if i==movie["name"]:
                arr2.append(movie["imdb"])
    return sum(arr2)/len(arr2)
arr1 = input().split("|")
print(imdb_score(arr1))

#Task5
def imdb_category(name1_category):
    arr3 = []
    for movie in movies:
        if movie["category"]==name1_category:
            arr3.append(movie["imdb"])
    return sum(arr3)/len(arr3)
name1_category = input()
print(imdb_category(name1_category))




    