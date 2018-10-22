from flask.blueprints import Blueprint
from sqlalchemy.orm import joinedload

from movies import db
from movies.log import get_logger
from movies.models.dbfunctions import Movie, Genre, Director
from movies.core.commons import jsonify

logger = get_logger()
mod = Blueprint('api_handler', __name__)

@mod.route('/getMovies' , methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    response = jsonify({"data":movies})
    return response


@mod.route('/insertMovie', methods=['GET'])
def insert_movie_info():
    genre_name = 'history'
    genre= Genre.query.filter(Genre.name==genre_name).one()
    genre_list = []
    if not genre:
        genre = Genre(genre_name)
        genre_list.append(genre)
    
    director_name = 'Adriyan Lyne'
    director = Director.query.filter(Director.name == director_name).first()
    if not director:
        director = Director(director_name)
    new_movie = Movie('movie2',director,55,4.5,genre_list)
    tx_session = db.session
    tx_session.add(new_movie)
    tx_session.commit()
    return 'movie inserted'