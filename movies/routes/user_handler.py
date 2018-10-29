from flask import request, abort
from flask.blueprints import Blueprint
from movies.log import get_logger
from movies.core.commons import jsonify
from movies.core.data_operations import *

logger = get_logger()
mod = Blueprint('user_handler', __name__)


@mod.route('/getMovies', methods=['GET'])
def get_all_movies():
    movies = get_movie_list()
    response = jsonify({"data": movies}, fields_to_exclude=["id"])
    return response


@mod.route('/findMovies', methods=['GET'])
def search_movie_info():
    if 'name' in request.args:
        movie_name = request.args.get('name')
        res = search_by_movie_name(movie_name)

    elif 'director' in request.args:
        director_name = request.args.get('director')
        res = search_by_movie_director(director_name)

    elif 'popularity' in request.args:
        try:
            popularity = int(request.args.get('popularity'))
        except ValueError:
            abort(422,"Value datatype mismatch")
        res = search_by_movie_popularity(popularity)

    elif 'imdb_score' in request.args:
        try:
            imdb_score = float(request.args.get('imdb_score'))
        except ValueError:
            abort(422,"Value datatype mismatch")
        res = search_by_movie_imdb_score(imdb_score)

    elif 'genre' in request.args:
        genre = request.args.get('genre')
        res = search_by_movie_genre(genre)
    
    else:
        return jsonify({"error":"missing arguments"})

    response = jsonify({"data": res})
    return response
