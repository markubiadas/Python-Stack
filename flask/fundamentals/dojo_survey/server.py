from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'markymark'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def form():
    # print("Got Post Info")
    print(request.form)
    session['user_name'] = request.form['name']
    session['user_dojo'] = request.form['dojo']
    session['user_language'] = request.form['language']
    session['user_comments'] = request.form['comments']
    return redirect("/show")

@app.route("/show")
def show_user():
    return render_template('show.html')


if __name__ == "__main__":
    app.run(debug=True)