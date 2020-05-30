import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Ingredient, Dish

from auth import AuthError, requires_auth

ITEMS_PER_PAGE = 10


def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    questions = [question.format() for question in selection]

    return questions[start:end]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app


APP = create_app()


@APP.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@APP.route('/ingredients')
def view_ingredients():
    selection = Ingredient.query.order_by(Ingredient.id).all()
    current_ingredients = paginate(request, selection)
    if len(current_ingredients) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'ingredients': current_ingredients,
        "total_ingredients": len(selection)
    })


@APP.route('/dishes')
def view_dishes():
    selection = Dish.query.order_by(Dselection=Dish.id).all()
    current_dishes = paginate(request, selection)
    if len(current_dishes) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'dishes': current_dishes,
        "total_dishes": len(selection)
    })

# Error Handling
@APP.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@APP.errorhandler(404)
def Notfound(error):
    return jsonify({
        "success": True,
        "error": 404,
        "description": "Resource not found"
    }), 404


@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@APP.errorhandler(AuthError)
def autherror(error):
    return jsonify({
        "success": True,
        "error": error.status_code,
        "description": error.error["description"]
    }), error.status_code


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
