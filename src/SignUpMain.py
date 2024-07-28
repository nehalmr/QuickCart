from customtkinter import *
import customtkinter 
from tkinter import messagebox
from PIL import Image
import SigninMain as signin
import Home as home
from tkinter import messagebox
import tkinter.messagebox as messagebox
from firebase import *

def create_signup_ui(newFrame):
        name_icon_data = Image.open("assets/user.png")
        email_icon_data = Image.open("assets/email.png")
        phone_icon_data = Image.open("assets/call.png")
        age_icon_data = Image.open("assets/age.png")
        #gender_icon_data = Image.open("assets/gender.png")
        password_icon_data = Image.open("assets/1.jpeg")
        confirm_password_icon_data = Image.open("assets/confirm.png")

        name_icon = CTkImage(dark_image=name_icon_data, light_image=name_icon_data, size=(20, 20))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(17, 17))
        phone_icon = CTkImage(dark_image=phone_icon_data, light_image=phone_icon_data, size=(20, 20))
        age_icon = CTkImage(dark_image=age_icon_data, light_image=age_icon_data, size=(17, 17))
        #gender_icon = CTkImage(dark_image=gender_icon_data, light_image=gender_icon_data, size=(20, 20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
        confirm_password_icon = CTkImage(dark_image=confirm_password_icon_data, light_image=confirm_password_icon_data, size=(20, 20))

        frame = CTkFrame(master=newFrame, width=500, height=610, fg_color="#ffffff", corner_radius=20)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        #labels SignUp
        signUp_label = CTkLabel(master=frame, text="SignUp", text_color="#601E88", anchor="center", justify="center", font=("Arial Bold", 24))
        signUp_label.pack(anchor="center", pady=10)

        #label Slogan
        slogan_label = CTkLabel(master=frame, text="Swift & Secure Shopping Experience!", text_color="#7E7E7E", anchor="center", justify="center", font=("Arial Bold", 12))
        slogan_label.pack(anchor="center", padx=(25, 0))

        #label
        sign_label = CTkLabel(master=frame, text="SignUp in to your account", text_color="#601E88", anchor="center", justify="center", font=("Arial Bold", 16))
        sign_label.pack(anchor="center", padx=(25, 0), pady=(10,0))

        #label user_name
        user_name = CTkLabel(master=frame, text="  Name:", image=name_icon,text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),  compound="left")
        user_name.pack(anchor="w", pady=(10, 0), padx=(70, 0))

        #name entry
        user_name_entry = CTkEntry(master=frame, width=325, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        user_name_entry.pack(anchor="w", padx=(75, 0))

        #label user email
        user_email = CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left",image=email_icon, font=("Arial Bold", 14),compound="left")
        user_email.pack(anchor="w", pady=(10, 0), padx=(70, 0))
        #email entry
        user_email_entry = CTkEntry(master=frame, width=325, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        user_email_entry.pack(anchor="w", padx=(75, 0))

        #label phone no
        user_phone = CTkLabel(master=frame, text="  Phone Number:", text_color="#601E88", anchor="w", justify="left", image=phone_icon,font=("Arial Bold", 14),  compound="left")
        user_phone.pack(anchor="w", pady=(10, 0), padx=(70, 0))
        #phone no entry
        user_phone_entry = CTkEntry(master=frame, width=325, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        user_phone_entry.pack(anchor="w", padx=(75, 0))

        #Age label
        user_age = CTkLabel(master=frame, text="  Age:", image=age_icon,text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),compound="left")
        user_age.pack(anchor="w", pady=(10, 0), padx=(70, 0))
        #User age entry
        user_age_entry = CTkEntry(master=frame, width=325, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        user_age_entry.pack(anchor="w", padx=(75, 0))
        
        #user gender label
        user_gender =CTkLabel(master=frame, text="Gender:",text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),  compound="left")
        user_gender.pack(anchor="w", pady=(10,0), padx=(75, 0))
        newFrame.genderVar=StringVar(value="Prefer\not to say")

        user_male = CTkRadioButton(master=frame,text="Male",variable=newFrame.genderVar,value="True")
        user_male.place(relx=0.3, rely=0.64)
        user_female = CTkRadioButton(master=frame,text="Female",variable=newFrame.genderVar,value="False")
        user_female.place(relx=0.5, rely=0.64)
       
        #password label
        user_password=CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", image=password_icon,font=("Arial Bold", 14),compound="left")
        user_password.pack(anchor="w", pady=(10, 0), padx=(70, 0))
        

        # password entry
        user_password_entry = CTkEntry(master=frame, width=325, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        user_password_entry.pack(anchor="w", padx=(75, 0))

        #confirm password label
        confirm_password = CTkLabel(master=frame, text="  Confirm Password:", text_color="#601E88", anchor="w", justify="left", image=confirm_password_icon,font=("Arial Bold", 14),compound="left")
        confirm_password.pack(anchor="w", pady=(10, 0), padx=(70, 0))

        # confirm password entry
        confirm_password_entry = CTkEntry(master=frame, width=325, height=30, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        confirm_password_entry.pack(anchor="w", padx=(75, 0))

        #signUp button
        signUp_btn = CTkButton(master=frame,command=lambda :signUp(frame, newFrame), text="SignUp", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", anchor="center",width=150, height=30)
        signUp_btn.pack(anchor="center", pady=(10, 0), padx=(0, 0))

        def signUp(self, currentFrame):
                print("Button Pressed")
                name = user_name_entry.get()
                email = user_email_entry.get()
                phoneNo = user_phone_entry.get()
                age1 = user_age_entry.get()
                age = age1.strip()  # Strip any leading/trailing spaces
                password = user_password_entry.get()
                confirmPassword = confirm_password_entry.get()

                if not (name and email and phoneNo and age and password and confirmPassword):
                        messagebox.showerror("Unsuccessful", "Please fill in all fields.")
                        return

                try:
                        age = int(age)
                        if age <= 0:
                                raise ValueError
                except ValueError:
                        messagebox.showerror("Unsuccessful", "Please enter a valid age.")
                        return

                if len(phoneNo) != 10 or not phoneNo.isdigit():
                        messagebox.showerror("Unsuccessful", "Please enter a valid 10-digit phone number.")
                        return

                if password != confirmPassword:
                        messagebox.showerror("Unsuccessful", "Passwords do not match.")
                        return

                if not password:
                        messagebox.showerror("Unsuccessful", "Please enter a password.")
                        return

                val = signup(email, password)
                if val:
                        add_document('User_data', email, {'name': name, 'email': email, 'phoneNo': phoneNo, 'age': age, 'password': password})
                        messagebox.showinfo('Successful', 'Successfully Sign Up!')
                        goToSignIn(self, currentFrame)
                else:
                        messagebox.showerror("Unsuccessful", "Unable to sign up. Please try again.")

def goToSignIn(currentFrame, newFrame) :
        currentFrame.destroy()
        signin.createSignIN(newFrame)
