import os
from firebase_admin import credentials, firestore, initialize_app

base_dir = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(base_dir, '..', 'secrets', 'serviceAccountKey.json')

cred = credentials.Certificate(cred_path)
initialize_app(cred)
db = firestore.client()
