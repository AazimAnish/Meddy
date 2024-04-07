from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
gpt_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


audio_file= open("C:/Users/thepywizard/Documents/hackathena/Meddy/api/harvard.wav", "rb")
transcription = client.audio.transcriptions.create(
model="whisper-1", 
file=audio_file
)
print(transcription.text)