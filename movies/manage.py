from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import simplejson as json

from movies import application as app
from movies import db
from movies.models.movie_model import Genre, Director, Movie


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

def get_item(iterable_obj, item_name):
    for item in iterable_obj:
        if item is not None:
            if item.name == item_name:
                return item
    return None

@manager.command
def seed():
    movies = []
    movie_names_set = set()
    genre_set = set()
    director_set = set()
       
    with open('imdb.json') as imdb:
        datas = json.load(imdb)
        for data in datas:
            movie_name = data['name']
            if movie_name in movie_names_set:
                print(movie_name)
                continue
            movie_names_set.add(movie_name)
            
            director_name = data['director'].strip()
            director = get_item(director_set, director_name)
            if director is None:
                director = Director.query.filter(Director.name == director_name).first()
                if not director:
                    director = Director(director_name)
                director_set.add(director)
            
            genres = data['genre']
            genre_objs = []
            for genre in genres:
                genre_name = genre.strip()
                genre = get_item(genre_set, genre_name)
                if genre is None:
                    genre = Genre.query.filter(Genre.name == genre_name).first()
                    if not genre:
                        genre = Genre(genre_name)
                    genre_set.add(genre)
                genre_objs.append(genre)
            
            popularity = data['99popularity']
            imdb_score = data['imdb_score']
            genres = data['genre']
            movie = Movie.query.filter(Movie.name == movie_name).first()
            if movie is None:
                movie = Movie(movie_name, director, popularity, imdb_score, genre_objs)
            else:
                movie.director = director
            movies.append(movie)
    
    for movie in movies:
        db.session.add(movie)

    db.session.commit()

if __name__ == '__main__':
    manager.run()
#     update movies.user_roles set role_id=2 where user_id=1;