from sqlalchemy.exc import IntegrityError

from movies import db
from movies.log import get_logger
from movies.models.movie_model import Movie, Genre, Director
from movies.cust_exceptions import DatabaseException

def init_app(app):
    global logger
    logger = get_logger()


def get_movie_list():
    movie_list = Movie.query.all()
    return movie_list


def delete_movie(movie_name):
    try:
        movie_found = Movie.query.filter(Movie.name == movie_name).first()
        if movie_found:
            db.session.delete(movie_found)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        raise DatabaseException(e)

def insert_new_movie(movie_name, director_name, popularity, imdb_score, genres):
    try:
        genre_list = []
        for genre_name in genres:
            genre = Genre.query.filter(Genre.name == genre_name).first()
            if not genre:
                genre = Genre(genre_name)
            
            genre_list.append(genre)

        director = Director.query.filter(Director.name == director_name).first()
        if not director:
            director = Director(director_name)

        new_movie = Movie(movie_name, director, popularity, imdb_score, genre_list)
    
        db.session.add(new_movie)
        db.session.commit()
        return True
    except IntegrityError:
        return False
    except Exception as e:
        raise DatabaseException(e)

def update_movie(movie_name, director_name, popularity, imdb_score, genres):
    try:
        movie = Movie.query.filter(Movie.name == movie_name).first()
        if not movie:
            return False
        
        if director_name:
            director = Director.query.filter(
                Director.name == director_name).first()
            if not director:
                director = Director(director_name)
            movie.director = director

        if popularity:
            movie.popularity = popularity
        if imdb_score:
            movie.imdb_score = imdb_score
        if genres:
            genre_list = []
            for genre_name in genres:
                genre = Genre.query.filter(Genre.name == genre_name).first()
                if not genre:
                    genre = Genre(genre_name)

                genre_list.append(genre)
            movie.genres = genre_list
    
        db.session.commit()
        return True
    except Exception as e:
        raise DatabaseException(e)

def search_by_movie_name(movie_name):
    movies = Movie.query.filter(Movie.name.like('%'+movie_name+'%')).all()
    return movies


def search_by_movie_popularity(popularity):
    movies = Movie.query.filter(Movie.popularity >= popularity).all()
    return movies


def search_by_movie_imdb_score(imdb_score):
    movies = Movie.query.filter(Movie.imdb_score >= imdb_score).all()
    return movies


def search_by_movie_director(director):
    directors = Director.query.filter(
        Director.name.like('%'+director+'%')).all()
    movies = []
    for director in directors:
        movies.append(director.movies)
    return movies


def search_by_movie_genre(genre):
    genres = Genre.query.filter(Genre.name.like('%'+genre+'%')).all()
    movies = []
    for gen in genres:
        movies.append(gen.movies)
    return movies
