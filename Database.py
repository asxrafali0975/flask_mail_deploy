from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
load_dotenv()

uri  = os.environ.get("uri")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['new_testing_uri']
collections = db['users_data']