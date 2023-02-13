from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# Create Survey
    @classmethod
    def save(cls,data):
        query = """
            INSERT INTO dojos (name, location, language, comment)
            VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)


# Show one
    @classmethod
    def get_last_survey(cls):
        query = """
            SELECT * FROM dojos
            ORDER BY dojos.id DESC LIMIT 1;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        return Survey(results[0])

# ========== This is for validating input fields ==========
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("Please select a Dojo location.")
            is_valid = False
        if len(dojo['language']) < 3:
            flash("Please select a language.")
            is_valid = False
        if len(dojo['comment']) < 5:
            flash("Comment must be at least 5 characters.")
            is_valid = False
        return is_valid
