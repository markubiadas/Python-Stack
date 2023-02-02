from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route('/')
def index():
    return render_template("index.html", row=8, col=8, color_one='red', color_two='black')

# Rows and Columns

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color_one='red', color_two='black')


@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html", row=x, col=y, color_one='red', color_two='black')

# COLORS

@app.route('/<int:x>/<int:y>/<color_one>')
def row_col_color_one(x,y,color_one):
    return render_template("index.html", row=x, col=y, color_one=color_one, color_two='black')

@app.route('/<int:x>/<int:y>/<color_one>/<color_two>')
def row_col_color_two(x,y,color_one,color_two):
    return render_template("index.html", row=x, col=y, color_one=color_one, color_two=color_two)


# ============================

if __name__ == "__main__":
    app.run(debug=True)