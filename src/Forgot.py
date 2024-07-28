from customtkinter import *
import customtkinter
from PIL import Image
import SigninMain as signin
from tkinter import messagebox
import tkinter.messagebox as messagebox

def create_Forgot_ui(newFrame):
        #images 
        email_icon_data = Image.open("assets/2.jpeg")
        password_icon_data = Image.open("assets/1.jpeg")

        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

        #created frame
        frame = CTkFrame(master=newFrame, width=500, height=550, fg_color="#ffffff", corner_radius=10)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        #label - forgot password 
        forgot_password_label = CTkLabel(master=frame, text="Forgot Password", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 24)).pack(anchor="center", pady=(50, 5), padx=(25, 0))

        label1 = CTkLabel(master=frame, text="Swift & Secure Shopping Experience!", text_color="#7E7E7E", anchor="center", justify="left", font=("Arial Bold", 12)).pack(anchor="center", padx=(25, 0),pady=(5,0))

        label2 = CTkLabel(master=frame, text="Forgot Password of your account", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 16)).pack(anchor="center", padx=(25, 0),pady=(5,0))

        #Email label
        email_label = CTkLabel(master=frame, text="  Email or Phone:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left")
        email_label.pack(anchor="w", pady=(38, 0), padx=(75, 0))
        #email entry
        email_entry = CTkEntry(master=frame, width=350, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        email_entry.pack(anchor="w", padx=(70, 0))

        #label - new password
        password_label = CTkLabel(master=frame, text="  New Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left")
        password_label.pack(anchor="w", pady=(21, 0), padx=(75, 0))

        #password entry
        password_entry = CTkEntry(master=frame, width=350, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        password_entry.pack(anchor="w", padx=(70, 0))

        #confirm password
        confirm_passord = CTkLabel(master=frame, text="  Confirm Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left")
        confirm_passord.pack(anchor="w", pady=(21, 0), padx=(75, 0))

        #confirm password entry
        confirm_password_entry = CTkEntry(master=frame, width=350, height=40, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        confirm_password_entry.pack(anchor="w", padx=(70, 0))

        def forgotPassword(self, currentFrame):

                print("Button Pressed")
                password = password_entry.get()
                confirmPassword = confirm_password_entry.get()
                if(password==confirmPassword and password!=""):
                        messagebox.showinfo('Successful','Password updated successfully')
                        goToSignIn(self, currentFrame)
                else:
                        messagebox.showerror("Unsuccessful","Password doesn't match")

        #Submit button
        submit_button = CTkButton(master=frame,command=lambda :forgotPassword(frame, newFrame),  text="Submit", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, height=50)
        submit_button.pack(anchor="w", pady=(40, 0), padx=(130, 0))

def goToSignIn(currentFrame, newFrame) :
        currentFrame.destroy()
        signin.createSignIN(newFrame)

        