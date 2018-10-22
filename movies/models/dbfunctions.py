from sqlalchemy import Column, ForeignKey, Float, Integer, String
from sqlalchemy.orm import relationship, backref

from movies import db
from movies.log import get_logger


def init_app(app):
    global logger
    logger = get_logger()
    logger.info('dbfunctions initialized')

genre_movies = db.Table('genre_movies',
    Column('movie_id', Integer, ForeignKey('movie.id')),
    Column('genre_id', Integer, ForeignKey('genre.id'))
)

class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
     
    popularity = Column(Float)
    imdb_score = Column(Float)
    director_id = Column(Integer, ForeignKey('director.id'),
        nullable=True)
    director = relationship('Director', backref=backref('movies', lazy=True), lazy=False)
    genres = relationship('Genre', secondary=genre_movies,
                             backref=backref('movies', lazy=True), lazy=False)
    
    def __init__(self, name, director, popularity, imdb_score, genres):
        self.name = name
        self.director = director
        self.popularity = popularity
        self.genres = genres
        self.imdb_score = imdb_score

class Genre(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    
    def __init__(self , name):
        self.name = name

class Director(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    
    def __init__(self , name):
        self.name = name
