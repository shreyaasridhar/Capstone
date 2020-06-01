# Le Bistro - Udacity Capstone project

This application was created as a Final Capstone project for Udacity's Full Stack Nano Degree. This application is Le Bistro, the great french restaurant in the neighbourhood that servers delicious dishes. 

### Pre-requisites and local development

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

### API Endpoints


`curl 'http://127.0.0.1:5000/ingredients' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ad2pwaGdWSFdQVFduMEhXcU5qaCJ9.eyJpc3MiOiJodHRwczovL2xlYmlzdHJvLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWQyZjhjOGJlYjY4NDBjOTM5NjY1MzEiLCJhdWQiOiJiZXN0Zm9vZCIsImlhdCI6MTU5MDkyOTY5NywiZXhwIjoxNTkxMDE2MDk3LCJhenAiOiJqb05vbVQzMWZkeGNhUjE3MjB5OXVLR0MwekthSlFiMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiR0VUOmRpc2hlcyIsIkdFVDppbmdyZWRpZW50cyJdfQ.KCV18PR5fUk8UzVT7MxxABghaoopICoiPbzFzOC-J0EtjR9mzuKZip7w0gcbNa4TWYI0BMlHVJoXmlFtWFx43yHXA36dJqlxkhCij2iRN1otGB0_qNOn0f8wovV7UkTIl4R02gp3Vp-L-5HxL13O5Ee7jsq7l1i0-HvUmsM1f7VuBldbsdEcFIgX_XmG5pcBQOOGYioMhm0UCTIXJpEhl0xjYw0h8hPtWwTV1DSFx2jpyfCPSn7DN5weS6bP6-PErJxHC8rxdvf9tD_iPQRBc9zU1r_TNN44xhmh-02u3e7Vg5bj9T0YQAWgudYu6fibqalh_r99aPKaf01MnV0KiQ'`

## Tests
To run the test file [test_flaskr.py](test_flaskr.py), please make sure to run the following commands.

`dropdb test_capstone && createdb test_capstone`
`psql test_capstone < test_capstone.sql`




