#ex1
"""
def imdb_more_than_5(movie):
    return movie.get("imdb", 0) > 5.5:
"""
"""
for movie in movies:
    if imdb_more_than_5(movie):
        print(True)
    else:
        print(False)
"""   
#ex2
"""
def imdb_more_than_5(movie):
    return movie.get("imdb", 0) > 5.5
"""
"""
imdb_movie = [movie for movie in movies if imdb_more_than_5(movie)]
for movie in imdb_movie:
    print(f"{movie['name']} {movie['imdb'] } {movie['category']}")
"""
#ex3
"""
def movie_category(category):
    return [movie for movie in movies if movie['category']==category]
"""
"""
movie_category_input = movie_category(input(""))
print(movie_category_input)
"""
#ex4
"""
def avg_imdb(movies):
    num_movies = 0
    total_score = 0
    for movie in movies:
        total_score = movie['imdb']
        num_movies += 1
    return total_score / num_movies
"""
"""
average = avg_imdb(movies)
print(average)
"""
#ex5
def movie_category(category):
    return [movie for movie in movies if movie['category']==category]
def avg_imdb(movies):
    num_movies = 0
    total_score = 0
    for movie in movies:
        total_score = movie['imdb']
        num_movies += 1
    return total_score / num_movies

def avg_by_category(category):
    movies = movie_category(category)
    return avg_imdb(movies)
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
average_score = avg_by_category(input(""))
print(average_score)