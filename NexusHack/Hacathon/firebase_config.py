import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Your downloaded Firebase service account key
firebase_admin.initialize_app(cred)

# Initialize Firestore (optional)
db = firestore.client()
