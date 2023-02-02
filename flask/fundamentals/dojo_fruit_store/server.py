from re import A
import datetime as dt
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

# date time
date_today = dt.datetime.now()

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    first_name = request.form['first_name']
    string_date = date_today.strftime("%B %d, %Y")
    count = int(strawberry) + int(raspberry) + int(apple)
    print(f"Charging {first_name} for {count} fruits.")
    return render_template("checkout.html", total = count, date = string_date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True,port=5002)    