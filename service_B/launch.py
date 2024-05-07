import os
from flask import Flask

app_b = Flask(__name__)

@app_b.route('/')
def display():
    # Lấy giá trị của biến môi trường SERVICE_A_NAME
    service_a_name = os.environ.get('SERVICE_A_NAME', 'default_value_if_not_found')
    return "link with " + service_a_name

if __name__ == '__main__':
    app_b.run(host="0.0.0.0", port=int("5100"), debug=True)
