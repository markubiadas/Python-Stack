from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

# ===== Form Route ======
@app.route('/ninjas')
def new():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojos)

# ======= Create Ninja Route =======
@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    new_id = Ninja.create(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}/show")

