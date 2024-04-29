# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def root():
#     return "Hello other world!"

# if __name__=='__main__':
#     app.run(debug=True)



import requests
from datetime import date
import json


if __name__=='__main__':
    url = 'http://127.0.0.1:5000/todo_items'
    jsonObj = {'title': 'first task', 'category': 'cleaning', 'completed': False, 'due_date': '2024-05-01'}
    x = requests.post(url, json=jsonObj)
    print(x.headers)
    print(x.status_code)

    url2 = 'http://127.0.0.1:5000/todo_items/1'
    y = requests.get(url2)
    print(json.loads(y.content))
    print('\n\n')

    url3 = 'http://127.0.0.1:5000/todo_items'
    z = requests.get(url3)
    print(json.loads(z.content))
    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(200), nullable=False)
    # category = db.Column(db.String(100), nullable=False)
    # completed = db.Column(db.Boolean, default=False)
    # due_date = db.Column(db.DateTime, nullable=True)