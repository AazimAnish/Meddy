from flask import Flask
import json
from bson import json_util
from db import collection

app = Flask(__name__)


@app.route("/api/python")
def hello_world():
    return "<p>hi, World!</p>"

@app.route("/api/prescription")
def prescription():
    data = collection.find() # Retrieve data from MongoDB collection
    return json.loads(json_util.dumps(data))

