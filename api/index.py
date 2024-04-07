from flask import Flask,request,jsonify
import json
from bson import json_util

app = Flask(__name__)
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")

# Replace the connection string with your MongoDB cluster connection string
connection_string = f"mongodb+srv://{mongo_username}:{mongo_password}@meddy.mohd0er.mongodb.net/?retryWrites=true&w=majority&appName=meddy"

client = MongoClient(connection_string)
db = client["rajagiri"]  # Replace 'dbname' with your database name
collection = db["patient"]  # Replace 'collectionname' with your collection name

@app.route("/api/python")
def hello_world():
    return "<p>hi, World!</p>"

@app.get("/api/prescription")
def prescription():
    data = collection.find() # Retrieve data from MongoDB collection
    return json.loads(json_util.dumps(data))

@app.get("/api/view-patients")
def view_patients():
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


@app.post("/api/patient-reg")
def add_patient():
    try:
        # Get data from the POST request
        data = request.json  # Assuming JSON data is sent in the request body

        # Insert the data into the MongoDB collection
        result = collection.insert_one(data)

        # Respond with a success message and the ID of the inserted document
        response = {
            "message": "Patient registered successfully",
            "inserted_id": str(result.inserted_id)
        }
        return jsonify(response), 201  # HTTP status code 201 indicates resource created
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 indicates internal server error


