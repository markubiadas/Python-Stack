from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model
from flask import flash


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.user_id = data['user_id']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

# GET ALL RECIPE:
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM recipes;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

# CREATE RECIPE:
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO recipes (name,under, user_id, description, instruction, date)
            VALUES (%(name)s, %(under)s,%(id)s, %(description)s, %(instruction)s, %(date)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)


# VIEW ONE RECIPE:
    @classmethod
    def get_one(cls,data):
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

# EDIT ONE RECIPE:
    @classmethod
    def update(cls,data):
        query = """
            UPDATE recipes
            SET name = %(name)s,
                description = %(description)s,
                instruction = %(instruction)s,
                date = %(date)s,
                under = %(under)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)


# DELETE RECIPE:
    @classmethod
    def delete(cls,data):
        query = """
            DELETE FROM recipes
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)





#==****** TESTING===== DASHBOARD TABLE ====****** TESTING==
# JOIN TABLE
    # @classmethod
    # def join(cls):
    #     query = """
    #         SELECT *
    #         FROM recipes
    #         LEFT JOIN users ON users.id = recipes.user_id
    #     """
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     if results:
    #         this_recipe = cls(results[0])
    #         these_users = []
    #         for row in results:
    #             user_data = {
    #                 "id":row['users.id'],
    #                 "first_name": row['first_name'],
    #                 "last_name": row['last_name'],
    #                 "email": row['email'],
    #                 "password": row['password'],
    #                 "created_at": row['users.created_at'],
    #                 "updated_at": row['users.updated_at']
    #             }
    #             this_user = user_model.User(user_data)
    #             these_users.append(this_user)
    #         this_recipe.users = these_users
    #         # print(this_recipe.users)
    #         print(results)
    #         return this_recipe
            

    #         # print(results)
    #     return False

# =======JOHN'S DASHBOARD TABLE=======
    @classmethod
    def get_user_recipes(cls):
        query = """
        SELECT * FROM recipes
        JOIN users ON users.id = recipes.user_id 
        """
        result = connectToMySQL(DATABASE).query_db(query)
        if not result:
            return False
        recipe = []
        # recipes = cls(result)
        # ^ this is how u normally do it
        for row in result:
            recipes = cls(row)
            # ^ this combines the id and user_id cls(row)
            data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            #     {
            #     'id': row['id'],
            #     'first_name': row['first_name'],
            #     'last_name': row['last_name'],
            #     'email': row['email'],
            #     'password': row['password'],
            #     'created_at': row['created_at'],
            #     'updated_at': row['updated_at']
            # }]
            this_user = user_model.User(data)
            recipes.user = this_user
            recipe.append(recipes)
            # recipes.user.append(User(data[1]))
            # user_recipe.append(recipe_model.Recipe(recipe_data))
            # user_recipe.append(User(user_data))
        return recipe

# VALIDATOR
    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must not be blank",'recipe')
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must not be blank", 'recipe')
            is_valid = False
        if len(data['instruction']) < 3:
            flash("Instruction must not be blank", 'recipe')
            is_valid = False
        if len(data['date']) < 1:
            flash("Date must not be blank", 'recipe')
            is_valid = False
        if len(data['under']) < 1:
            flash("Under 30 mins must not be blank", 'recipe')
            is_valid = False
        return is_valid