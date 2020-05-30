import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from models import setup_db, Ingredient, Dish

from auth import AuthError, requires_auth

ITEMS_PER_PAGE = 10


def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    item = [item.format() for item in selection]

    return item[start:end]


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
    selection = Dish.query.order_by(Dish.id).all()
    current_dishes = paginate(request, selection)
    if len(current_dishes) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'dishes': current_dishes,
        "total_dishes": len(selection)
    })


@APP.route('/dishes', methods=['POST'])
def add_new_dishes():
    data = request.get_json()
    dish = Dish(data['name'], data['image_link'],
                json.dumps(data['ingredients']))
    dish.insert()
    return jsonify({
        'success': True
    })


@APP.route('/ingredients', methods=['POST'])
def add_new_ingredient():
    data = request.get_json()
    ingredient = Ingredient(data['name'], data['image_link'], data['color'])
    ingredient.insert()
    return jsonify({
        'success': True
    })


@APP.route('/dishes/<int:dish_id>', methods=['PATCH'])
def update_dish(dish_id):
    dish = Dish.query.filter(Dish.id == dish_id).one_or_none()
    if not dish:
        abort(404)
    data = request.get_json()
    if 'name' in data:
        setattr(dish, 'name', data['name'])
    if 'image_link' in data:
        setattr(dish, 'image_link', data['image_link'])
    if 'ingredients' in data:
        setattr(dish, 'ingredients', json.dumps(data['ingredients']))

    dish.update()
    return jsonify({
        "success": True,
        "dish": Dish.query.filter(Dish.id == dish_id).one_or_none()
    })


@APP.route('/ingredients/<int:ingredient_id>', methods=['PATCH'])
def update_ingredient(ingredient_id):
    ingredient = Ingredient.query.filter(
        Ingredient.id == ingredient_id).one_or_none()
    if not ingredient:
        abort(404)
    data = request.get_json()
    if 'name' in data:
        setattr(ingredient, 'name', data['name'])
    if 'image_link' in data:
        setattr(ingredient, 'image_link', data['image_link'])
    if 'color' in data:
        setattr(ingredient, 'color', data['color'])

    ingredient.update()
    return jsonify({
        "success": True,
        "ingredient": Ingredient.query.filter(Ingredient.id == ingredient_id).one_or_none()
    })


@APP.route('/dishes/<int:dish_id>', methods=["DELETE"])
def delete_dishes(dish_id):
    dish = Dish.query.filter(Dish.id == dish_id).one_or_none()
    if not dish:
        abort(404)
    dish.delete()
    return jsonify({
        "success": True,
        "delete": dish_id
    })


@APP.route('/ingredients/<int:ingredient_id>', methods=["DELETE"])
def delete_ingredient(ingredient_id):
    ingredient = Ingredient.query.filter(
        Ingredient.id == ingredient_id).one_or_none()
    if not ingredient:
        abort(404)
    ingredient.delete()
    return jsonify({
        "success": True,
        "delete": ingredient_id
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
