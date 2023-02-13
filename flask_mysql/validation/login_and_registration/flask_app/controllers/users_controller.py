from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

# ============ index route =============

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")


# ============ Create user + validation ==============

@app.route('/users/register', methods = ['POST'])
def user_reg():
    if not User.validator(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password':hashed_pass
    }
    user_id = User.create(data)
    session['user_id'] = user_id # .... user_id as a session
    return redirect('/dashboard')


# ============= Log In ===============

@app.route('/users/login', methods = ['POST'])
def log_in():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Email and Password does not match", 'log')
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Email and Password does not match", 'log')
        return redirect ('/')
    session['user_id'] = user_in_db.id
    return redirect ('/dashboard')




# =========== Logout ===============
@app.route('/users/logout')
def log_out():
    del session['user_id']
    return redirect('/')



# ============== Dashboard ===========
@app.route('/dashboard')
def dash():
    if 'user_id' not in session: # checking whether user_id is in session
        return redirect('/') # if not in session, then redirect to index
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data) # if logged in , we can access the whole data of that one id
    return render_template("welcome.html", logged_user = logged_user)

