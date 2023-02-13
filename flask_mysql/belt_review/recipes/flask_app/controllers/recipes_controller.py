from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

# ====== NEW RECIPE ROUTE/FORM =======
@app.route('/recipes/<int:id>/new')
def new_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    return render_template('add_recipe.html', data = data)

#  =====CREATE NEW RECIPE=====
@app.route('/recipes/<int:id>/create', methods=['POST'])
def create_recipe(id):
    data = {
        **request.form,
        'id': id
    }
    if not Recipe.validator(request.form):
        # FOR SOME REASON REDIRECTING TO THE URL OF NEW RECIPE ROUTE DOES NOT WORK. THAT IS WHY I JUST PUT 'new' INSIDE THE REDIRECT???
        return redirect('new')
    Recipe.create(data)
    return redirect('/dashboard')

# =======GET ONE RECIPE ======
@app.route('/recipes/<int:id>/show')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data)
    this_recipe = Recipe.get_one({"id":id})
    return render_template('one_recipe.html', this_recipe = this_recipe, logged_user = logged_user)

# =======EDIT RECIPE PAGE======
@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    this_recipe = Recipe.get_one(data)
    return render_template("edit_recipe.html", this_recipe = this_recipe)


# =======EDIT(UPDATE) ONE RECIPE=====
@app.route('/recipes/<int:id>/edit', methods=["POST"])
def update_recipe(id):
    data = {
        **request.form,
        'id':id
    }
    if not Recipe.validator(request.form):
        return redirect('edit')
    Recipe.update(data)
    return redirect('/dashboard')


# =======DELETE RECIPE========
@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    data = {
        'id':id
    }
    Recipe.delete(data)
    return redirect('/dashboard')



# ========== ONLY TESTING****** TEST SHOWING RECIPES ***** ONLY TESTING =========
# @app.route('/recipes/show_all')
# def show_all():
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         'id': session['user_id']
#     }
#     logged_user = User.get_by_id(data)
#     recipes = Recipe.get_user_recipes()
#     return render_template("test.html", logged_user = logged_user, recipes = recipes)