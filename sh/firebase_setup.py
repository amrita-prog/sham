import firebase_admin
from firebase_admin import credentials, firestore

# Load credentials from JSON
cred = credentials.Certificate("secrets/serviceAccountKey.json")

# Initialize the Firebase app
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()
