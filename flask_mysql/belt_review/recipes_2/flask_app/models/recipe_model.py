# JUST COPY IMPORTS FROM USER MODEL FIRST
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
# ADD THIS LINE
from flask_app.models import user_model

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction= data['instruction']
        self.date = data['date']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


# CREATE RECIPE
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO recipes (name, description, instruction, date, under, user_id)
            VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(under)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)


# GET ALL RECIPE
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM recipes
            JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        if results:
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                # this_recipe.chef is a variable. YOU CAN NAME IT WHATEVER YOU WANT
                this_recipe.chef = this_user
                all_recipes.append(this_recipe)
        return all_recipes


# GET ONE RECIPE
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM recipes
            JOIN users ON recipes.user_id = users.id
            WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            this_recipe = cls(results[0])
            row = results[0]
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_recipe.chef = this_user
            return this_recipe
        return False


# UPDATE RECIPE
    @classmethod
    def update(cls,data):
        query = """
            UPDATE recipes SET
            name = %(name)s,
            description = %(description)s,
            instruction = %(instruction)s,
            date = %(date)s,
            under = %(under)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)


# DELETE RECIPE
    @classmethod
    def delete(cls,data):
        query = """
            DELETE FROM recipes
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)



# VALIDATOR RECIPE
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data ['name']) < 3:
            flash("Name is required", 'recipe')
            is_valid = False
        if len(form_data ['description']) < 3:
            flash("Description is required", 'recipe')
            is_valid = False
        if len(form_data ['instruction']) < 3:
            flash("Instruction is required", 'recipe')
            is_valid = False
        if len(form_data ['date']) < 1:
            flash("Date is required", 'recipe')
            is_valid = False
        if "under" not in form_data:
            flash("Please select one in Under 30 Minutes section", 'recipe')
            is_valid = False
        return is_valid