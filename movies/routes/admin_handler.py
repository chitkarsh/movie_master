from flask import request, abort
from flask.blueprints import Blueprint
from flask_jwt import jwt_required
from movies.log import get_logger
from movies.core.commons import jsonify
from movies.core.data_operations import insert_new_movie, update_movie, delete_movie
from movies.cust_exceptions import ApplicationException

logger = get_logger()
mod = Blueprint('admin_handler', __name__)

@mod.route('/insertMovie', methods=['POST'])
@jwt_required()
def insert_movie_info():
    movie_name = request.form.get('name')
    director_name = request.form.get('director')
    genres = request.form.getlist('genres[]')
    try:
        popularity = int(request.form.get('popularity'))
        imdb_score = float(request.form.get('imdb_score'))
    except ValueError:
        abort(422,"Value datatype mismatch")
    
    if movie_name and director_name:
        try:
            new_movie=insert_new_movie(movie_name,director_name,popularity,imdb_score,genres)
            if new_movie:
                response = jsonify({"message":"Movie entry inserted"})
            else:
                response = jsonify({"message":"Duplicate entry. Not inserted"})
        except ApplicationException as a:
            logger.exception(a)
            abort(422, "database error")
    else:
        response = jsonify({"error":"missing arguments"})
    return response


@mod.route('/updateMovie', methods=['POST'])
@jwt_required()
def update_movie_info():
    movie_name = request.form.get('name')
    director_name = request.form.get('director')
    genres = request.form.getlist('genres[]')
    try:
        popularity = int(request.form.get('popularity'))
        imdb_score = float(request.form.get('imdb_score'))
    except ValueError:
        abort(500,"Value datatype mismatch")
    
    if movie_name:
        try:
            updated_movie=update_movie(movie_name,director_name,popularity,imdb_score,genres)
            if updated_movie:
                response = jsonify({"message":"Movie entry updated"})
            else:
                response = jsonify({"message":"Movie does not exists"})
        except ApplicationException as a:
            logger.exception(a)
            abort(500, "database error")
    else:
        response = jsonify({"error":"missing arguments"})
    return response

@mod.route('/deleteMovie', methods=['POST'])
@jwt_required()
def delete_movie_info():
    try:
        movie_name = request.form.get('name')
        res= delete_movie(movie_name)
        if res:
            response=jsonify({'message':'Movie deleted'})
        else:
            response=jsonify({'message':'Movie could not be deleted'})
        return response
    except ApplicationException as a:
        logger.exception(a)
        abort(500, "database error")