from flask_app import app
from flask import render_template,redirect, request, session, flash
from flask_app.models.email_model import Email

@app.route('/')
def index():
    return render_template("index.html")

# Create email

@app.route('/emails/create', methods = ['POST'])
def create_email():

    if not Email.validate_email(request.form):
        return redirect('/')

    Email.save(request.form)
    return redirect("/success")

# Show All Emails

@app.route('/success')
def show_email():
    emails = Email.get_all()
    return render_template('show_all.html', emails = emails)