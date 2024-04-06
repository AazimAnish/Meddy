from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_username=os.getenv("MONGO_USERNAME")
mongo_password=os.getenv("MONGO_PASSWORD")

# Replace the connection string with your MongoDB cluster connection string
connection_string = f"mongodb+srv://{mongo_username}:{mongo_password}@meddy.mohd0er.mongodb.net/?retryWrites=true&w=majority&appName=meddy"

client = MongoClient(connection_string)
db_name="sample_mflix"
db = client.dbname  # Replace 'dbname' with your database name
collection_name="users"
collection = db.collection_name  # Replace 'collectionname' with your collection name
