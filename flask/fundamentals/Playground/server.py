from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template("home.html")

# ======= Level 1 ========

@app.route('/play')
def index():
    return render_template("index.html")


# ======= Level 2 =========

@app.route('/play/<int:num>')
def num(num):
    return render_template("index2.html", num = num)

# ======== Level 3 =========

@app.route('/play/<int:num>/<color_change>')
def color(num,color_change):
    color_change = color_change
    return render_template("index3.html",num = num, color_change = color_change)





if __name__ == "__main__":
    app.run(debug=True)