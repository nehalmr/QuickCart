# firebase_auth.py
# This Module implements the key functionalites of Firebase Authentication in Python

import firebase_admin
from firebase_admin import credentials, auth
import requests
import json
from google.cloud import firestore
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "quickcartdemo-da394-firebase-adminsdk-54svr-d721c9ac99.json" # Add Your Json Key
# Use a service account
cred = credentials.Certificate(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
firebase_admin.initialize_app(cred)
db = firestore.Client()


def signup(email, password):
    try:
        auth.create_user(
            email=email,
            password=password,
        )
        print('User created successfully')
        return True
    except Exception as e:
        print('Error creating user:', e)
        return False


def login(email, password):
    def sign_in_with_email_and_password(email, password):
        FIREBASE_WEB_API_KEY = ' ' # Add your API Key
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        payload = json.dumps({
            "email": email,
            "password": password,
            "returnSecureToken": True
        })
        r = requests.post(rest_api_url, params={
                          "key": FIREBASE_WEB_API_KEY}, data=payload)
        response_data = r.json()

        if "error" in response_data:
            return False, response_data["error"]["message"]
        else:
            return True, response_data

    success, data = sign_in_with_email_and_password(email, password)
    return success, data

    '''
        if success:
            print("User authenticated successfully!")
            print("User ID:", data["localId"])
            print("ID Token:", data["idToken"])
            
        else:
            print("Authentication failed:", data)
        
        '''


# def forgot_password(self, email):
#     try:
#         auth.send_password_reset_email(email)
#         print('Password reset email sent successfully')
#         return True
#     except Exception as e:
#         print('Error sending password reset email:', e)
#         return False


def get_all_users(self):
    try:
        users = auth.list_users()
        return users
    except Exception as e:
        print(e)
        return None


# # Example Usage
# if __name__ == "__main__":
#     # Replace 'path/to/your/credentials.json' with the path to your Firebase service account key JSON file


#     print(firebase_auth.signup('efbl@gmail.com','123456'))
#     print(firebase_auth.login('efbl@gmail.com','123456'))
#     print(firebase_auth.get_all_users())


def get_document(collection_name, doc_id):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None


def add_document(collection_name, doc_id, doc_data):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.set(doc_data)
    return doc_id


def update_document(collection_name, doc_id, doc_data):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.update(doc_data)


# Product Manipulation
data = get_document('Product', 'B1')
for key, value in data.items():
    if (key == 'name'):
        name = value
    if (key == 'price'):
        price = value
    if (key == 'description'):
        description = value
    if (key == 'img_path'):
        image = value

print(name)
print(price)
print(description)
print(image)
