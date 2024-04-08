from flask import Flask,request,jsonify
import json
from bson import json_util
import requests
from heyoo import WhatsApp
from datetime import date
app = Flask(__name__)
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from deep_translator import GoogleTranslator
try:
    from pydub import AudioSegment
except():
    pass

from openai import OpenAI


load_dotenv()
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")
#gpt_key = os.getenv("GPT_API_KEY")

# Replace the connection string with your MongoDB cluster connection string
connection_string = f"mongodb+srv://{mongo_username}:{mongo_password}@meddy.mohd0er.mongodb.net/?retryWrites=true&w=majority&appName=meddy"

client = MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)
db = client["rajagiri"]  # Replace 'dbname' with your database name


@app.route("/api/python")
def hello_world():
    return "<p>hi, World!</p>"

@app.get("/api/prescription")
def prescription():
    collection = db["prescription"]
    data = collection.find() # Retrieve data from MongoDB collection
    return json.loads(json_util.dumps(data))

@app.get("/api/view-patients")
def view_patients():
    collection = db["patient"]
    data = collection.find() # Retrieve data from MongoDB collection
    return json.loads(json_util.dumps(data))


@app.get("/api/view-patients/<uhid>")
def view_patient(uhid):
    try:
    
        collection = db["patient"]
        
        # Find patient by UHID
        patient = collection.find_one({"uhid": int(uhid)})
        
        # Check if patient exists
        if uhid:
            return json.loads(json_util.dumps(patient))
        else:
            return jsonify({"error": "Patient not found"}), 404  # HTTP status code 404 indicates resource not found
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 indicates internal server error


'''   
@app.post("/api/speech-to-text")
def speech_to_text():
    try:
        client = OpenAI()

        audio_file= open("harvard.wav", "rb")
        transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )
        print(transcription.text)
        
    except Exception as e:
        # If an error occurs, respond with an error message
        print(e)
        return "An error occurred"  '''

@app.post("/api/prescription")
def add_prescription():
    try:
        collection = db["prescription"]
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
        collection = db["patient"]
        # Get data from the POST request
        data = request.json  # Assuming JSON data is sent in the request body

        # Insert the data into the MongoDB collection
        result = collection.insert_one(data)
        phone = data.get("phone")
        # Respond with a success message and the ID of the inserted document
        response = {
            "message": "Patient registered successfully",
            "inserted_id": str(result.inserted_id)
        }
        messenger = WhatsApp("EAAGL5dZCRyoEBOZBsZAf0R4d2rXwlddD76EykK8MifbFkDcvffrpNcBDHtAc6E7sP2mI2dwd2ESGdbSn0JJIhXu3uS39gRsnZCvZAGXdSTJVC2ZBKPTZCUDkMURmZBjWdLOdv1Ev2wiWuXOJO4d7Sms1cJZBZA1sQOjW7P207enDS0rVyRwXJSBzjQYc6XR5WC2HqQl0uykhl9ua1Rhv3j8kGX", phone_number_id="259164670622151")
        
        messenger.send_reply_button(
                        recipient_id="91"+str(phone),
                        button={
                            "type": "button",
                            "body": {
                                "text": "Thank you for opting rajagiri. Meddy will assist you for pre doc-consulting."
                            },
                            "action": {
                                "buttons": [
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "start",
                                            "title": "Let's Start"
                                        }
                                    }
                                ]
                            }
                        },
                    )
        return jsonify(response), 201  # HTTP status code 201 indicates resource created
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 indicates internal server error


@app.get("/api/get-appointments")
def get_appointments():
    collection = db["appointments"]
    data = collection.find()
    return json.loads(json_util.dumps(data))

@app.get("/api/get-appointments/<uhid>")
def get_specific_appointment_info(uhid):
    try:
    
        collection = db["appointments"]
        
        # Find patient by UHID
        patient = collection.find_one({"uhid": int(uhid)})
        
        # Check if patient exists
        if uhid:
            return json.loads(json_util.dumps(patient))
        else:
            return jsonify({"error": "Patient not found"}), 404  # HTTP status code 404 indicates resource not found
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 indicates internal server error



@app.post("/api/book-appointment")
def book():
    try:
        # Access appointments collection
        collection = db["patient"]
        collection2=db["appointments"]
        
        # Get data from the POST request
        data = request.json  # Assuming JSON data is sent in the request body
        
        # Find if the phone number exists in appointments collection
        existing_patient = collection.find_one({"phone": data.get("phone")})
        
        if existing_patient:
            # Extract patient details
            first_name = existing_patient.get("firstName")
            last_name = existing_patient.get("lastName")
            uhid = existing_patient.get("uhid")
            
            # Create new appointment data
            new_appointment = {
                "firstName": first_name,
                "lastName": last_name,
                "uhid": uhid,
                "doctor": data.get("doctor"),
                "speciality": data.get("speciality"),
                "time": date.today().strftime('%d-%m-%Y')
            }
            
            # Insert the new appointment data into the MongoDB collection
            result = collection2.insert_one(new_appointment)
            
            # Respond with a success message and the ID of the inserted document
            response = {
                "message": "Appointment booked successfully",
                "inserted_id": str(result.inserted_id),
                "name": first_name + " " + last_name
            }
            return jsonify(response), 201  # HTTP status code 201 indicates resource created
        else:
            # If the phone number doesn't exist in appointments collection, return error
            return jsonify({"error": "Patient not found. Please register first."}), 404
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500  # HTTP status code 500 indicates internal server error


@app.post("/api/audios_add")
def audio():
    try:
        collection = db["audios"]
        # Get data from the POST request
        data = request.json  # Assuming JSON data is sent in the request body

        # Insert the data into the MongoDB collection
        collection.delete_many({})
        result = collection.insert_one(data)
        
        # Respond with a success message and the ID of the inserted document
        response = {
            "message": "Audio added successfully",
            "inserted_id": str(result.inserted_id)
        }
        return jsonify(response), 201  # HTTP status code 201 indicates resource created
    except Exception as e:
        # If an error occurs, respond with an error message
        return jsonify({"error": str(e)}), 500
    
@app.get("/api/audios") 
def process_audio():
    collection = db["audios"]
    messenger = WhatsApp("EAAGL5dZCRyoEBO5zEVXpckSwl7RMrjfMc4IYu3EWpVdGuj0CYDm08o5pkQD39mfmg6tikNOFsCpxgJjoNapnPZAcpivNZCZCr3gQMNaZCCSZCI0g6IHqnAYy7ZAVCR9jLJJKW2tQzCZB0cjkDigRXnXfgDoZC7oNxmrw3Qaz3ZCcV2icSGClvtOMNkZB6DAWzPg9DLMvHn0NkaUML6rDuUwopiB", phone_number_id="259164670622151")
    audio=list(collection.find({}))[0]
    print(audio)
    mime_type = audio["mime_type"]
    audio_id = audio["id"]
    audio_url = messenger.query_media_url(audio_id)
    audio_filename = messenger.download_media(audio_url, mime_type)

    audiok = AudioSegment.from_file(audio_filename, format="ogg")
    mp3_filename = "converted_audio.mp3"
    audiok.export(mp3_filename, format="mp3")
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.getenv("OPENAI_API_KEY"),
    )


    audio_file= open(r"converted_audio.mp3", "rb")
    translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file
    )
    print(translation.text)

    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": translation.text,
        "parameters": {"candidate_labels": ["Psychiatrist", "Dentist", "Cardiologist", "Dermatologist", "Orthopedist", "ENT Specialist", "General Physician", "Ophthalmologist"],"multi_label":True},
    })
    required_doctor = output["labels"][0]
    textk = f'''
    It is recommended that you see a {required_doctor}.\nShall I book an appointment for the following doctor available at Rajagiri Hospital\nPhilip K Thomas\nConsultant {required_doctor}
    '''
    if audio["language"] == "malayalam":
        textk = GoogleTranslator(source='auto', target='ml').translate(textk)
    



    messenger.send_reply_button(
        recipient_id=audio["mobile"],
        button={
            "type": "button",
            "body": {
                "text": textk
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "yes",
                            "title": "Yes"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "no",
                            "title": "No"
                        }
                    }
                ]
            }
        },
    )
    
    
    return json.loads(json_util.dumps(audio))


@app.get("/api/sendreminder") 
def new():
    messenger = WhatsApp("EAAGL5dZCRyoEBO5zEVXpckSwl7RMrjfMc4IYu3EWpVdGuj0CYDm08o5pkQD39mfmg6tikNOFsCpxgJjoNapnPZAcpivNZCZCr3gQMNaZCCSZCI0g6IHqnAYy7ZAVCR9jLJJKW2tQzCZB0cjkDigRXnXfgDoZC7oNxmrw3Qaz3ZCcV2icSGClvtOMNkZB6DAWzPg9DLMvHn0NkaUML6rDuUwopiB", phone_number_id="259164670622151")
    messenger.send_message("നിങ്ങളുടെ മരുന്ന് കഴിക്കാൻ മറക്കരുത്","918129953715")
    
    return json.loads(json_util.dumps({"message":"sent"}))
