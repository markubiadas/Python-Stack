from flask_app import app
from flask import render_template,redirect, request, session, flash
from flask_app.models.survey_model import Survey

@app.route('/')
def index():
    return render_template("index.html")



# /TABLE/ACTION
# ===== CREATE SURVEY ROUTE ======

@app.route('/surveys/create', methods=['POST'])
def create_survey():

    if not Survey.validate_dojo(request.form):
        return redirect('/')

    Survey.save(request.form)
    return redirect("/results")



#  ========= SHOW SURVEY RESULT =========
@app.route("/results")
def results():
    one_survey = Survey.get_last_survey()
    return render_template('show.html', one_survey = one_survey)
    # return render_template('show.html', survey = Survey.get_last_survey())