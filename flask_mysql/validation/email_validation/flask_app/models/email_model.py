from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# =========== GET ALL EMAIL ===========
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM emails;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails


# =========== CREATE EMAIL =============
    @classmethod
    def save(cls,data):
        query = """
            INSERT INTO emails (email)
            VALUES (%(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)


# =========== VALIDATE EMAIL ===========

    @staticmethod
    def validate_email(email):
        is_valid = True
        # the code below checks whether the email is already in the database.
        # If email is in the database, email register is invalid.
        # If email is not in database, email is good to register.
        query = """
            SELECT * FROM emails
            WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,email)
        if len(results) >= 1:
            is_valid = False
            flash("Email is already taken. Please type a new email.")
        if len(email['email']) < 5:
            is_valid = False
            flash("Please type a valid email in the form.")
        elif not EMAIL_REGEX.match(email['email']):
            is_valid = False
            flash("Please type a valid email format.")
        return is_valid