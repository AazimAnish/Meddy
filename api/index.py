from flask import Flask,request,jsonify
import json
from bson import json_util
from db import collection

app = Flask(__name__)


@app.route("/api/python")
def hello_world():
    return "<p>hi, World!</p>"

@app.get("/api/prescription")
def prescription():
    data = collection.find() # Retrieve data from MongoDB collection
    return json.loads(json_util.dumps(data))

@app.post("/api/prescription")
def add_prescription():
    try:
        # Get data from the POST request
        data = request.json  # Assuming JSON data is sent in the request body

        # Insert the data into the MongoDB collection
        result = collection.insert_one(data)

        # Respond with a success message and the ID of the inserted document
        response = {
            "message": "Prescription added successfully",
            "inserted_id": str(result.inserted_id)
        }
        return jsonify(response), 201  # HTTP status code 201 indicates resource created
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 indicates internal server error