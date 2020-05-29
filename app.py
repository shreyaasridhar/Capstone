import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app


APP = create_app()


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


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
