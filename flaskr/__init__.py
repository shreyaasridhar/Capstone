import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from models import setup_db, Ingredient, Dish, drop_create_all

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

    # drop_create_all()

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/ingredients')
    @requires_auth("GET:ingredients")
    def view_ingredients(jwt):
        selection = Ingredient.query.order_by(Ingredient.id).all()
        # current_ingredients = paginate(request, selection)
        # if len(current_ingredients) == 0:
        #     abort(404)
        return jsonify({
            'success': True,
            'ingredients': [item.format() for item in selection],
            "total_ingredients": len(selection)
        })

    @app.route('/dishes')
    @requires_auth("GET:dishes")
    def view_dishes(jwt):
        selection = Dish.query.order_by(Dish.id).all()
        # current_dishes = paginate(request, selection)
        # if len(current_dishes) == 0:
        #     abort(404)
        return jsonify({
            'success': True,
            'dishes': [item.format() for item in selection],
            "total_dishes": len(selection)
        })

    @app.route('/dishes', methods=['POST'])
    @requires_auth("POST:dishes")
    def add_new_dishes(jwt):
        data = request.get_json()
        dish = Dish(data['name'], data['image_link'],
                    json.dumps(data['ingredients']))
        dish.insert()
        return jsonify({
            'success': True
        })

    @app.route('/ingredients', methods=['POST'])
    @requires_auth("POST:ingredients")
    def add_new_ingredient(jwt):
        data = request.get_json()
        ingredient = Ingredient(
            data['name'], data['image_link'], data['color'])
        ingredient.insert()
        return jsonify({
            'success': True
        })

    @app.route('/dishes/<int:dish_id>', methods=['PATCH'])
    @requires_auth("PATCH:dishes")
    def update_dish(jwt, dish_id):
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
            "dish": Dish.query.filter(Dish.id == dish_id).one_or_none().format()
        })

    @app.route('/ingredients/<int:ingredient_id>', methods=['PATCH'])
    @requires_auth("PATCH:ingredients")
    def update_ingredient(jwt, ingredient_id):
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
            "ingredient": Ingredient.query.filter(Ingredient.id == ingredient_id).one_or_none().format()
        })

    @app.route('/dishes/<int:dish_id>', methods=["DELETE"])
    @requires_auth("DELETE:dishes")
    def delete_dishes(jwt, dish_id):
        dish = Dish.query.filter(Dish.id == dish_id).one_or_none()
        if not dish:
            abort(404)
        dish.delete()
        return jsonify({
            "success": True,
            "delete": dish_id
        })

    @app.route('/ingredients/<int:ingredient_id>', methods=["DELETE"])
    @requires_auth("DELETE:ingredients")
    def delete_ingredient(jwt, ingredient_id):
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
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def Notfound(error):
        return jsonify({
            "success": True,
            "error": 404,
            "description": "Resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(AuthError)
    def autherror(error):
        return jsonify({
            "success": True,
            "error": error.status_code,
            "description": error.error["description"]
        }), error.status_code

    return app
