from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

# ADD RECIPE FORM
@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("recipe_new.html")


# CREATE A RECIPE
@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    recipe_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.create(recipe_data)
    return redirect('/dashboard')


# SHOW ONE RECIPE
@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    logged_user = User.get_by_id({'id': session['user_id']})
    this_recipe = Recipe.get_by_id(data)
    return render_template("recipe_one.html", this_recipe = this_recipe, logged_user = logged_user)


# EDIT RECIPE FORM
@app.route('/recipes/<int:id>/edit')
def edit_user_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_recipe = Recipe.get_by_id(data)
    return render_template('recipe_edit.html', one_recipe = one_recipe)

# UPDATE RECIPE
@app.route('/recipes/<int:id>/update', methods = ['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect(f"/recipes/{id}/edit")
    data = {
        'id': id,
        **request.form
    }
    Recipe.update(data)
    return redirect('/dashboard')

# DELETE RECIPE
@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    Recipe.delete(data)
    return redirect('/dashboard')