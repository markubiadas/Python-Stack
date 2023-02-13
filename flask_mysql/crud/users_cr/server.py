from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)


@app.route('/new')
def new():
    return render_template("create.html")


# Create User
@app.route('/create', methods=["POST"])
def create_user():
    new_id = User.create(request.form)
    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)