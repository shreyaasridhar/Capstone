import unittest
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from app import create_app
from models import setup_db, Ingredient, Dish, drop_create_all
unittest.TestLoader.sortTestMethodsUsing = None


class RestaurantTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()

        self.manager = {'Content-Type': 'application/json',
                        'Authorization': "Bearer {}".format(os.getenv("RESTAURANT_MANAGER"))}
        self.head_chef = {'Content-Type': 'application/json',
                          'Authorization': "Bearer {}".format(os.getenv("HEAD_CHEF"))}
        self.sous_chef = {'Content-Type': 'application/json',
                          'Authorization': "Bearer {}".format(os.getenv("SOUS_CHEF"))}

        self.database_name = "test_capstone"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        self.new_ingredient = {
            "name": "Peanut",
            "image_link": "https://images.unsplash.com/photo-1567892737950-30c4db37cd89",
            "color": "brown",
        }
        self.new_dish = {
            "name": "Pancake",
            "image_link": "https://images.unsplash.com/photo-1554520735-0a6b8b6ce8b7",
            "ingredients": [
                "Milk",
                "Baking powder",
                "Flour",
                "Maple Syrup"
            ]
        }
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # GET ingredients

    def test_get_ingredients(self):
        res = self.client.get('/ingredients', headers=self.sous_chef)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["ingredients"])
        self.assertTrue(data['total_ingredients'])

    def test_get_ingredients_unauthorized_user(self):
        res = self.client.get('/ingredients')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"], "Authorization header expected.")
        self.assertTrue(data["success"])

    # GET dishes

    def test_get_dishes(self):
        res = self.client.get('/dishes', headers=self.sous_chef)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["dishes"])
        self.assertTrue(data['total_dishes'])

    def test_get_dishes_unauthorized_user(self):
        res = self.client.get('/dishes')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"], "Authorization header expected.")
        self.assertTrue(data["success"])

    # POST /ingredients

    def test_insert_ingredients(self):
        res = self.client.post(
            '/ingredients', headers=self.head_chef, json=self.new_ingredient)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_insert_ingredients_unauthorized(self):
        res = self.client.post(
            '/ingredients', headers=self.sous_chef, json=self.new_ingredient)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["description"], "Permission not found.")
        self.assertTrue(data["success"])

    # POST /dishes

    def test_insert_dishes(self):
        res = self.client.post(
            '/dishes', headers=self.manager, json=self.new_dish)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_insert_dishes_unauthorized(self):
        res = self.client.post(
            '/dishes', headers=self.head_chef, json=self.new_dish)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["description"], "Permission not found.")
        self.assertTrue(data["success"])

    # PATCH /ingredients/<int:ingredient_id>

    def test_update_ingredient(self):
        updated_ingredient = {
            "name": "Tomato",
            "image_link": "https://images.unsplash.com/photo-1518977822534-7049a61ee0c2",
            "color": "red"
        }
        res = self.client.patch(
            '/ingredients/1', headers=self.head_chef, json=updated_ingredient)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["ingredient"])

    def test_update_ingredient_unauthorized(self):
        updated_ingredient = {
            "name": "Tomato",
            "image_link": "https://images.unsplash.com/photo-1518977822534-7049a61ee0c2",
            "color": "red"
        }
        res = self.client.patch(
            '/ingredients/1', headers=self.sous_chef, json=updated_ingredient)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["description"], "Permission not found.")
        self.assertTrue(data["success"])

    # PATCH /dishes/<int:dish_id>

    def test_update_dish(self):
        updated_dish = {
            "name": "Penne Pasta",
            "image_link": "https://images.unsplash.com/photo-1501934398334-266c81d54888",
            "ingredients": ["pasta", "tomato", "onion"]
        }
        res = self.client.patch(
            '/dishes/1', headers=self.head_chef, json=updated_dish)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["dish"])

    def test_update_dish_unauthorized(self):
        updated_dish = {
            "name": "Penne Pasta",
            "image_link": "https://images.unsplash.com/photo-1501934398334-266c81d54888",
            "ingredients": ["pasta", "tomato", "onion"]
        }
        res = self.client.patch(
            '/dishes/1', headers=self.sous_chef, json=updated_dish)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["description"], "Permission not found.")
        self.assertTrue(data["success"])

    # DELETE / ingredients/<int: ingredient_id >

    def test_z_delete_ingredient(self):
        res = self.client.delete('/ingredients/1', headers=self.manager)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["delete"], 1)

    def test_z_delete_ingredient_unauthorized(self):
        res = self.client.delete('/ingredients/1', headers=self.sous_chef)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["description"], "Permission not found.")
        self.assertTrue(data["success"])

    # DELETE /dishes/<int:dish_id>

    def test_z_delete_dish(self):
        res = self.client.delete('/dishes/1', headers=self.manager)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["delete"], 1)

    def test_z_delete_dish_unauthorized(self):
        res = self.client.delete('/dishes/1', headers=self.sous_chef)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["description"], "Permission not found.")
        self.assertTrue(data["success"])


if __name__ == "__main__":
    unittest.main()
