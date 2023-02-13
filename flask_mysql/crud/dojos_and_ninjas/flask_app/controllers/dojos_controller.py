from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

# @app.route("/dojos")
# def dojos():
#     dojos = Dojo.get_all()
#     return render_template('dojos.html', dojos=dojos)


# ======== Create New Dojo =======
@app.route("/dojos/create", methods = ['POST'])
def create_dojo():
    Dojo.create(request.form)
    # dojos = Dojo.get_all()
    return redirect('/')

# ===== View one Dojo ======
@app.route('/dojos/<int:id>/show')
def show_dojo(id):
    one_dojo = Dojo.get_one({"id":id})
    return render_template("dojo_show.html", one_dojo = one_dojo)

