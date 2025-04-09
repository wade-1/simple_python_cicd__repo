from flask import Flask
from app.utils import add_numbers

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins Pipeline!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"Result: {add_numbers(a, b)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)