from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return json.dumps({"oi": "michelet"})


if __name__ == '__main__':
    app.run(host='0.0.0.0')