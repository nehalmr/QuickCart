    # # user.py
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth

# cred = credentials.Certificate('QC-NMR/config/c2w-demo-9b2c5-firebase-adminsdk-h73qd-bd4dd0e016.json')
# default_app = firebase_admin.initialize_app(cred) 

# class User:

#     def _init_(self, name, email, phoneNo, age, password):
#         self.name = name
#         self.email = email
#         self.phoneNo = phoneNo
#         self.age = age
#         self.password = password
#         self.cart = []

#     def login(self, email, password):
        
#         try:
#             # Authenticate with Firebase
#             user = auth.sign_in_with_email_and_password(email, password)
#             self.email = user.email
#             return True
        
#         except:
#             return False
            
#     def signup(self,name, email, phoneNo, age, password):

#         try:
#             # Create new user account
#             user = auth.create_user(email=email, password=password)
#             self.email = user.email
#             return True

#         except:
#             return False
        
# #implement the forgot password login in def forgotpassword():
#         def forgotpassword(self, email):
#             try:
#                 auth.send_password_reset_email(email)
#                 return True
#             except:
#                 return Falses

# user.py
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('config/quickcartdemo-da394-firebase-adminsdk-54svr-280371d1a3.json')
default_app = firebase_admin.initialize_app(cred) 

class User:

    def __init__(self, name, email, phoneNo, age, password):
        self.name = name
        self.email = email
        self.phoneNo = phoneNo
        self.age = age
        self.password = password
        self.cart = []

    def login(self, email, password):
        try:
            # Authenticate with Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            # You can access user data if needed, for example, user['email']
            self.email = email
            return True
        except:
            return False
            
    def signup(self, name, email, phoneNo, age, password):
        try:
            # Create new user account
            auth.create_user(email=email, password=password, display_name=name)
            self.email = email
            return True
        except:
            return False

    def forgotpassword(self, email):
        try:
            auth.send_password_reset_email(email)
            return True
        except:
            return False
