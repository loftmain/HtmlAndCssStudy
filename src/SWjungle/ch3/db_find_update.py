from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

movie = db.movies.find_one({'title':'매트릭스'})
print(movie['star'])

same_star = list(db.movies.find({'star':movie['star']}))
smae_star_title = [movie['title'] for movie in same_star]
print(smae_star_title)

db.movies.update_one({'title':'매트릭스'}, {'$set':{'star':0}})

matrix = db.movies.find_one({'title':'매트릭스'})
print(matrix)