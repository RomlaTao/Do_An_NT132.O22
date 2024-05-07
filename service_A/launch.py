# service_a.py
from flask import Flask

app_a = Flask(__name__)

@app_a.route('/')

def display():
    return "Hello World"

if __name__ == '__main__':
    app_a.run(host="0.0.0.0", port=int("5000"), debug=True)