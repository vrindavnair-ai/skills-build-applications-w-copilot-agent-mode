from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["octofit_db"]

# List collections
collections = db.list_collection_names()
print("Collections in octofit_db:", collections)
