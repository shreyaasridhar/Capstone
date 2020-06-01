# Le Bistro - Udacity Capstone project

This application was created as a Final Capstone project for Udacity's Full Stack Nano Degree. This application is Le Bistro, the great french restaurant in the neighbourhood that servers delicious dishes. 

## Pre-requisites and local development

**Frontend**

Development in Progress. 

**Backend**

Make sure to have Python 3.6 or 3.7 installed. This can be downloaded from the website or the through anaconda.

From the backend folder run `pip install requirements.txt` which includes all the required packages. 

**Key Dependencies**

[Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy and Flask-SQLAlchemy are libraries to handle the lightweight sqlite database. 

jose JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Environment Setup

Either execute `source .env` or `bash setup.sh` to load env variables in a local environment

### Database Setup
Make sure postgres server is running on the host machine and then create the database with `createdb capstone`. This repository has been initialized with the migrations folder that contains the basic schema for the database. 

To upgrade to the current schema, just run `python manage.py db upgrade`

To add changes the schema, `python manage.py db migrate`

Just for information, to initialize the repository for migrations, run `python manage.py db init`

The following is the general format for the path of the database. This repository has the one specific to the app deployed on heroku.
```
database_path = "postgres://{}:{}@{}/{}".format(<user-name>,'<password>','localhost:5432', <database_name>)"
```
**Run the application**

`FLASK_APP=app FLASK_ENV=development flask run`

This runs the application in develop and debug mode in app.py file of the root folder. 

## Authentication
This app has been designed to let users with certain permission to be able to work with the data. 

The following link can be used to register users:

`https://lebistro.auth0.com/authorize?audience=bestfood&response_type=token&client_id=joNomT31fdxcaR1720y9uKGC0zKaJQb3&redirect_uri=http://localhost:8080`

There are three primary roles,
1. Restaurant Manager
2. Head Chef
3. Sous Chef

Based on the roles specified they have specific permissions.

### Sous Chef

Active JWT token: 
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ad2pwaGdWSFdQVFduMEhXcU5qaCJ9.eyJpc3MiOiJodHRwczovL2xlYmlzdHJvLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQyZjhjOGJlYjY4NDBjOTM5NjY1MzEiLCJhdWQiOiJiZXN0Zm9vZCIsImlhdCI6MTU5MDkyOTY5NywiZXhwIjoxNTkxMDE2MDk3LCJhenAiOiJqb05vbVQzMWZkeGNhUjE3MjB5OXVLR0MwekthSlFiMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiR0VUOmRpc2hlcyIsIkdFVDppbmdyZWRpZW50cyJdfQ.KCV18PR5fUk8UzVT7MxxABghaoopICoiPbzFzOC-J0EtjR9mzuKZip7w0gcbNa4TWYI0BMlHVJoXmlFtWFx43yHXA36dJqlxkhCij2iRN1otGB0_qNOn0f8wovV7UkTIl4R02gp3Vp-L-5HxL13O5Ee7jsq7l1i0-HvUmsM1f7VuBldbsdEcFIgX_XmG5pcBQOOGYioMhm0UCTIXJpEhl0xjYw0h8hPtWwTV1DSFx2jpyfCPSn7DN5weS6bP6-PErJxHC8rxdvf9tD_iPQRBc9zU1r_TNN44xhmh-02u3e7Vg5bj9T0YQAWgudYu6fibqalh_r99aPKaf01MnV0KiQ
```

**Role** 

* Can view ingredients and dishes

### Head Chef

Active JWT token: 
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ad2pwaGdWSFdQVFduMEhXcU5qaCJ9.eyJpc3MiOiJodHRwczovL2xlYmlzdHJvLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQyZmZmOGYwYjhlNjBjOGU4NmZlODMiLCJhdWQiOiJiZXN0Zm9vZCIsImlhdCI6MTU5MDkyOTU5MywiZXhwIjoxNTkxMDE1OTkzLCJhenAiOiJqb05vbVQzMWZkeGNhUjE3MjB5OXVLR0MwekthSlFiMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiREVMRVRFOmluZ3JlZGllbnRzIiwiR0VUOmRpc2hlcyIsIkdFVDppbmdyZWRpZW50cyIsIlBBVENIOmRpc2hlcyIsIlBBVENIOmluZ3JlZGllbnRzIiwiUE9TVDppbmdyZWRpZW50cyJdfQ.FdQyOODbFc8vLRp6SdMLvgkEMUUJh7bsreoCE7zUFTO_kk13mlNfbjoKZGTE07ByMJmwqFN-IuWLC3wYjUjfFwpzd0_OEowlk5pYd1M0tofmqtbi9WaLIwRxuQnBGJO8ouuQU_qWIAAhrljInwU70E_6J2a4KNFaj2HYE6CPzRF35PkNiiuQ-imxWBa5Ce9CxikLot7xhvp2zjOkgvB5Fj-YtX3D7xVg4sHiTGbxrNDoYLs6mtyIPri5dfKGbeChgqgCCCu03w0wRMnJdY5Q2sfZq6XqCzjGbxliGUxfh1arXHJdrXJQ86YOCPcvUOGuntgl5e1qkySooTjgcL8KIQ
```
**Role** 

* All permissions a Sous Chef has and 

* Add or delete an ingredient from the database

* Modify ingredients or dishes

### Restaurant Manager

Active JWT token: 
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ad2pwaGdWSFdQVFduMEhXcU5qaCJ9.eyJpc3MiOiJodHRwczovL2xlYmlzdHJvLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQyZmZjZmJlYjY4NDBjOTM5NjcxZTMiLCJhdWQiOiJiZXN0Zm9vZCIsImlhdCI6MTU5MDkyOTc4NSwiZXhwIjoxNTkxMDE2MTg1LCJhenAiOiJqb05vbVQzMWZkeGNhUjE3MjB5OXVLR0MwekthSlFiMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiREVMRVRFOmRpc2hlcyIsIkRFTEVURTppbmdyZWRpZW50cyIsIkdFVDpkaXNoZXMiLCJHRVQ6aW5ncmVkaWVudHMiLCJQQVRDSDpkaXNoZXMiLCJQQVRDSDppbmdyZWRpZW50cyIsIlBPU1Q6ZGlzaGVzIiwiUE9TVDppbmdyZWRpZW50cyJdfQ.c-lDAU7Mv5beMZzyiwIgiBx19DzsQrajT6gHEDM9G7MSA419wqWwjxsTQJGC0TFNL0OWJrklyeXxooFh1WbKNYbXyWHolTWPV-ZmJrBJzeFRgG_GqEgy304hae3g2ItCjYKD0PpwCWBUUo121X4MkjfGpf9FYmiVbEbipGtUYyI4km5M-7-sRhb1CcDcoc5YeYFvYosBoHC8mV-BRe_GqRzkfEpggphucBDGeS5IVjZjUBJTOPwoKaOzLSRov-9xZ_ONW7YMcTrSRBAg-u7h6Qf249Nt__fGKAoZG2dj-bNbiPk1V4ocj_eKS9Orq9Vq6oQtwi9lbNfoEBdxDl49rQ
```

**Role** 

* All permissions a Head Chef has and…

* Add or delete a movie from the database

## Error Handling
Errors are returned a readable JSON format.
```
return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unproccessable'
        })
```
The API will return objects when requests fail due to a certain type of condition:
```
    * 400: Bad Request
    * 401: Unauthorized Request
    * 404: Resource not found
    * 405: Not allowed
    * 422: Unprocessable action
    * 500: Internal error  
```

## API Endpoints

Please view the attached [postman collection](Capstone-Restaurant.postman_collection.json) to view the sample requests and run them by changing the url to `https://lebistro.herokuapp.com` to access the heroku instance. 

A sample curl request is as follows. 
```
curl 'http://127.0.0.1:5000/ingredients' 
-H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ad2pwaGdWSFdQVFduMEhXcU5qaCJ9.eyJpc3MiOiJodHRwczovL2xlYmlzdHJvLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQyZjhjOGJlYjY4NDBjOTM5NjY1MzEiLCJhdWQiOiJiZXN0Zm9vZCIsImlhdCI6MTU5MDkyOTY5NywiZXhwIjoxNTkxMDE2MDk3LCJhenAiOiJqb05vbVQzMWZkeGNhUjE3MjB5OXVLR0MwekthSlFiMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiR0VUOmRpc2hlcyIsIkdFVDppbmdyZWRpZW50cyJdfQ.KCV18PR5fUk8UzVT7MxxABghaoopICoiPbzFzOC-J0EtjR9mzuKZip7w0gcbNa4TWYI0BMlHVJoXmlFtWFx43yHXA36dJqlxkhCij2iRN1otGB0_qNOn0f8wovV7UkTIl4R02gp3Vp-L-5HxL13O5Ee7jsq7l1i0-HvUmsM1f7VuBldbsdEcFIgX_XmG5pcBQOOGYioMhm0UCTIXJpEhl0xjYw0h8hPtWwTV1DSFx2jpyfCPSn7DN5weS6bP6-PErJxHC8rxdvf9tD_iPQRBc9zU1r_TNN44xhmh-02u3e7Vg5bj9T0YQAWgudYu6fibqalh_r99aPKaf01MnV0KiQ'
```

### GET /ingredients
* Gets the list of all the ingredients in the database. Can be paginated if quite large. 
* Also returns the total number of ingredients
```
{
    "ingredients": [
        {
            "color": "red",
            "id": 1,
            "image_link": "https://images.unsplash.com/photo-1518977822534-7049a61ee0c2",
            "name": "tomato"
        }
    ],
    "success": true,
    "total_ingredients": 1
}
```
### GET /dishes
### POST /ingredients
* Adds a new ingredient in the following format in the json addribute of the request.
```
{
    "name": "Peanut",
    "image_link": "https://images.unsplash.com/photo-1567892737950-30c4db37cd89",
    "color": "brown",
}
```
* Returns a success value.
```
{
    "success": true
}
```
### POST /dishes
* Adds a new dish in the following format in the json addribute of the request.
```
{
     "name": "Pancake",
     "image_link": "https://images.unsplash.com/photo-1554520735-0a6b8b6ce8b7",
     "ingredients": ["Milk","Baking powder","Flour","Maple Syrup"]
}
```
* Returns a success value.
```
{
    "success": true
}
```
### PATCH /ingredients/{ingredient_id}
* Modifies the specified id and returns the list of ingredients and success value.

* Sample
```
{
    "ingredient": {
        "color": "red",
        "id": 1,
        "image_link": "https://images.unsplash.com/photo-1518977822534-7049a61ee0c2",
        "name": "Tomato"
    },
    "success": true
}
```
### PATCH /dishes/{dish_id}
* Modifies the specified id and returns the list of dishes and success value.

* Sample
```
{
  "dish": {
    "id": 2,
    "image_link": "https://images.unsplash.com/photo-1501934398334-266c81d54888",
    "ingredients": [
      "pasta",
      "tomato",
      "onion"
    ],
    "name": "Penne Pasta"
  },
  "success": true
}
```
### DELETE /ingredients/{ingredient_id}
* Deletes the specified id and returns the id and success value.

* Sample
```
{
  "delete": 1,
  "success": true
}
```
### DELETE /dishes/{dish_id}
* Deletes the specified id and returns the id and success value.

* Sample
```
{
  "delete": 1,
  "success": true
}
```

## Tests

To run the test file [test_flaskr.py](test_flaskr.py), please make sure to run the following commands, also remember to set env variables.

`dropdb test_capstone && createdb test_capstone`

`psql test_capstone < test_capstone.sql`

`python3 test_flaskr.py`

## Deployment

Heroku deployed: `https://lebistro.herokuapp.com`

Here are the basic instruction on how to deploy on Heroku.
Make sure your git repository has all the required changes in the master branch.
```
heroku create APP_NAME
git remote add heroku GIT_URL_FROM_PREVIOUS_COMMAND
heroku addons:create heroku-postgresql:hobby-dev --app APP_NAME
heroku config --app APP_NAME
!! Before running the next command make sure to update the postgres DATABASE_URL!!
git push heroku master
heroku run python manage.py db upgrade --app APP_NAME
```
Add env variables to the heroku dashboard.

To run commands on the deployment environment use `heroku run` followed by the unix command.

To view Heroku logs to debug, use `heroku logs`




### Authors

[Shreyaa Sridhar](https://github.com/shreyaasridhar)

### Acknowledgements

Udacity Nanodegree!

Great amounts of Patience with deployment! :p




