from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "markymark"


@app.route('/')
def index():
    if "counter" in session: # checking whether 'counter' exist in session[""].
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template("index.html", counter = session['counter'])

@app.route("/user")
def click_button():
    session['counter'] += 1
    return redirect("/")
    

@app.route("/destroy_session")
def clear_all():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5003)