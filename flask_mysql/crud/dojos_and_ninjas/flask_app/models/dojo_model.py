from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ======== Get All Dojo ==========
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dojos;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

# ======== Get One Dojo =========
    @classmethod
    def get_one(cls,data):
        query = """
            SELECT * FROM dojos
            LEFT JOIN ninjas
            ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            this_dojo = cls(results[0])
            these_ninjas = []
            for row in results:
                ninja_data = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "dojo_id": row['dojo_id'],
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at']
                }
                this_ninja = ninja_model.Ninja(ninja_data)
                these_ninjas.append(this_ninja)
            this_dojo.ninjas = these_ninjas
            return this_dojo
            print(results)

        return False

# ======== Create New Dojo =========
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)