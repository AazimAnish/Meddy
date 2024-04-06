from flask import Flask, jsonify
from db import collection

app = Flask(__name__)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/prescription")
def prescription():
    data = list(collection.find())  # Retrieve data from MongoDB collection
    return jsonify(data)

