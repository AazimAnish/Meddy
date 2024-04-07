from flask import Flask, request
from heyoo import WhatsApp
from deep_translator import GoogleTranslator
import requests



app = Flask(__name__)
messenger = WhatsApp("EAAGL5dZCRyoEBO5zEVXpckSwl7RMrjfMc4IYu3EWpVdGuj0CYDm08o5pkQD39mfmg6tikNOFsCpxgJjoNapnPZAcpivNZCZCr3gQMNaZCCSZCI0g6IHqnAYy7ZAVCR9jLJJKW2tQzCZB0cjkDigRXnXfgDoZC7oNxmrw3Qaz3ZCcV2icSGClvtOMNkZB6DAWzPg9DLMvHn0NkaUML6rDuUwopiB", phone_number_id="259164670622151")
state = "normal"
language = "english"


@app.route('/', methods=['POST'])
def extract_audio():
    global state, language
    data = request.get_json()
    
    changed_field = messenger.changed_field(data)
    if changed_field == "messages":
        new_message = messenger.is_message(data)
        if new_message:
            mobile = messenger.get_mobile(data)
            name = messenger.get_name(data)
            message_type = messenger.get_message_type(data)
            print(
                f"New Message; sender:{mobile} name:{name} type:{message_type}"
            )



            if message_type == "text":
                message = messenger.get_message(data)
                name = messenger.get_name(data)
                print("Message: %s", message)
                if message.lower() == "hi":
                    messenger.send_reply_button(
                        recipient_id=mobile,
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
                elif state=="ask symptoms":
                    print(state)
                    state="normal"
                    
                    symptoms = GoogleTranslator(source='auto', target='en').translate(message)           

                    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
                    headers = {"Authorization": "Bearer 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"}

                    def query(payload):
                        response = requests.post(API_URL, headers=headers, json=payload)
                        return response.json()

                    output = query({
                        "inputs": symptoms,
                        "parameters": {"candidate_labels": ["Psychiatrist", "Dentist", "Cardiologist", "Dermatologist", "Orthopedist", "ENT Specialist", "General Physician"],"multi_label":True},
                    })
                    required_doctor = output["labels"][0]
                    textk = f'''
                    It is recommended that you see a {required_doctor}.\nShall I book an appointment for the following doctor available at Rajagiri Hospital\nPhilip K Thomas\nConsultant {required_doctor}
                    '''
                    if language=="malayalam":
                        textk = GoogleTranslator(source='auto', target='ml').translate(message) 
                    
                    

                    messenger.send_reply_button(
                        recipient_id=mobile,
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



                    

            elif message_type == "interactive":
                message_response = messenger.get_interactive_response(data)
                interactive_type = message_response.get("type")
                message_id = message_response[interactive_type]["id"]
                message_text = message_response[interactive_type]["title"]
                print(f"Interactive Message; {message_id}: {message_text}")
                if message_id=="start":
                    messenger.send_reply_button(
                        recipient_id=mobile,
                        button={
                            "type": "button",
                            "body": {
                                "text": "Choose your preferred language"
                            },
                            "action": {
                                "buttons": [
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "english",
                                            "title": "English"
                                        }
                                    },
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "malayalam",
                                            "title": "മലയാളം"
                                        }
                                    }
                                ]
                            }
                        },
                    )
                elif message_id=="english":
                    language = "english"
                    messenger.send_reply_button(
                        recipient_id=mobile,
                        button={
                            "type": "button",
                            "body": {
                                "text": "Choose an option"
                            },
                            "action": {
                                "buttons": [
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "book",
                                            "title": "Book an appointment"
                                        }
                                    },
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "lab",
                                            "title": "Get Lab Records"
                                        }
                                    },
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "prescriptions",
                                            "title": "Get Prescriptions"
                                        }
                                    },
                                ]
                            }
                        },
                    )

                elif message_id=="malayalam":
                    language = "malayalam"
                    messenger.send_reply_button(
                        recipient_id=mobile,
                        button={
                            "type": "button",
                            "body": {
                                "text": "ഓപ്ഷൻ തിരഞ്ഞെടുക്കുക"
                            },
                            "action": {
                                "buttons": [
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "book",
                                            "title": "അപ്പോയിൻ്റ്മെൻ്റ്"
                                        }
                                    },
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "lab",
                                            "title": "ലാബ് റെക്കോർഡുകൾ"
                                        }
                                    },
                                    {
                                        "type": "reply",
                                        "reply": {
                                            "id": "prescriptions",
                                            "title": "കുറിപ്പടികൾ"
                                        }
                                    },
                                ]
                            }
                        },
                    )

 
            
                elif message_id=="book":
                    if language=="english": 
                        messenger.send_message('Give a brief description about your symptoms', mobile)
                    elif language=="malayalam":
                        messenger.send_message('നിങ്ങളുടെ ബുദ്ധിമുട്ടുകൾ വിശദീകരിക്കുക', mobile)
                    print(state)
                    state = "ask symptoms"
                    print(state)

                elif message_id=="prescriptions":
                    messenger.send_document(
        document="https://pdfobject.com/pdf/sample.pdf",
        recipient_id="918129953715",
        caption="Prescription"
    ) 
                elif message_id=="lab":
                    messenger.send_document(
        document="https://pdfobject.com/pdf/sample.pdf",
        recipient_id="918129953715",
        caption="Lab Report"
    )
                
                



            elif message_type == "location":
                message_location = messenger.get_location(data)
                message_latitude = message_location["latitude"]
                message_longitude = message_location["longitude"]
                print("Location: %s, %s", message_latitude, message_longitude)

            elif message_type == "image":
                image = messenger.get_image(data)
                image_id, mime_type = image["id"], image["mime_type"]
                image_url = messenger.query_media_url(image_id)
                image_filename = messenger.download_media(image_url, mime_type)
                print(f"{mobile} sent image {image_filename}")

            elif message_type == "video":
                video = messenger.get_video(data)
                video_id, mime_type = video["id"], video["mime_type"]
                video_url = messenger.query_media_url(video_id)
                video_filename = messenger.download_media(video_url, mime_type)
                print(f"{mobile} sent video {video_filename}")

            elif message_type == "audio":
                audio = messenger.get_audio(data)
                audio_id, mime_type = audio["id"], audio["mime_type"]
                audio_url = messenger.query_media_url(audio_id)
                audio["mobile"] = mobile
                audio["language"] = language
                response = requests.post("https://meddy-rho.vercel.app/api/audios", json=audio, headers={'Content-Type': 'application/json'})
                if response.status_code == 200:
                    print("Request successful:", response.content)
                else:
                    print("Request failed with status code:", response.status_code)
                    print("Response content:", response.content) 
                #audio_filename = messenger.download_media(audio_url, mime_type)
                #print(f"{mobile} sent audio {audio_filename}")

            elif message_type == "document":
                file = messenger.get_document(data)
                file_id, mime_type = file["id"], file["mime_type"]
                file_url = messenger.query_media_url(file_id)
                file_filename = messenger.download_media(file_url, mime_type)
                print(f"{mobile} sent file {file_filename}")
            else:
                print(f"{mobile} sent {message_type} ")
                print(data)
        else:
            delivery = messenger.get_delivery(data)
            if delivery:
                print(f"Message : {delivery}")
            else:
                print("No new message")
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
