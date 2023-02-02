from flask import Flask

app = Flask(__name__)

# 1. localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    print("Hello World!")
    return "Hello World!"


# 2. localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    print("Dojo!")
    return "Dojo!"

# 3. Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<name>')
def say_name(name):
    print(f"{name.capitalize()}")
    return f"Hi {name.capitalize()}!"


# 4. Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num,word):
    return f"{word * num}"






if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True) 