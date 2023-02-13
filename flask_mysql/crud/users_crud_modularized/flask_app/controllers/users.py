from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

# ========== Home route ===========
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

# ============ Form route ===============
@app.route('/new')
def new():
    return render_template("create.html")

# ======== View one user route =========
@app.route("/users/<int:id>/show")
def show_user(id):
    one_user = User.get_one({"id":id})
    return render_template("user_show_one.html", one_user = one_user)

# ========= Create user route ===========
@app.route('/create', methods=["POST"])
def create_user():
    new_id = User.create(request.form)
    return redirect('/')

# ========= Delete user route ===========
@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/')

# ============ Edit user page==============
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id':id
    }
    this_user = User.get_one(data)
    return render_template("user_edit.html", this_user = this_user)

# ========= Update user ============
@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    data = {
        **request.form,
        'id':id
    }
    User.update(data)
    return redirect('/')