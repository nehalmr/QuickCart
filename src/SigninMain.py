from customtkinter import *
from tkinter import *
import customtkinter
from PIL import Image
import tkinter
from tkinter import messagebox
import tkinter.messagebox as messagebox
import SignUpMain as signUp
import Forgot as fg
import Home as home
from firebase import *

class SignInFormApp(CTk):
    def __init__(self):
        customtkinter.set_appearance_mode('light')
        super().__init__()
        self.geometry("1280x650")
        self.create_signin_ui()
        
    def create_signin_ui(self):

        #images 
        email_icon_data = Image.open("assets/2.jpeg")
        # email_icon_data = SVGImage.open("logo svg.svg")
        password_icon_data = Image.open("assets/1.jpeg")
        imageLogo = Image.open('assets/logo0_1.png')
        
        #set title
        # self.title("Login")

        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
        img_logo = CTkImage(dark_image=imageLogo, light_image=imageLogo, size=(60, 60))

        #created frame
        frame = CTkFrame(master=self, width=500, height=550, fg_color="#ffffff", corner_radius=20)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        CTkLabel(master=frame, text="QuickCart", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).place(relx=0.03, rely=0.03)
        
        CTkButton(master=frame,command=lambda : self.goToSignUp(frame), text="Create Account", fg_color="#601E88", hover_color="#E44982",anchor="center",font=("Arial Bold", 12), text_color="#ffffff", width=200, height=30).place(relx=0.56, rely=0.03)

        # logo 
        self.logo = CTkLabel(master=frame, text="", text_color="#ffffff", anchor="w", justify="center", image=img_logo, compound="left").place(relx=0.4, rely=0.2)

        CTkLabel(master=frame, text="Swift & Secure Shopping Experience!", text_color="#7E7E7E", anchor="center", justify="left", font=("Arial Bold", 12)).pack(anchor="center", padx=(25, 0), pady=(170,0))

        CTkLabel(master=frame, text="Sign in to your account", text_color="#601E88", anchor="center", justify="left", font=("Arial Bold", 16)).pack(anchor="center", padx=(20, 0),pady=(5,0))

        # Email Label
        self.email = CTkLabel(master=frame, text="  Email or Phone:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(20, 0), padx=(100, 0))

        self.email_entry=Entry(master=frame,font=("Arial", 20), width=30,relief="ridge", borderwidth=2)

        self.email_entry.pack(anchor="w", pady=(20, 0), padx=(150, 0))
        # Password Label
        self.password=CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(20, 0), padx=(100, 0))

        self.password_entry=Entry(master=frame,font=("Arial", 20), show='*',width=30,relief="ridge", borderwidth=2)
        self.password_entry.pack(anchor="w", pady=(20, 0), padx=(150, 0))
        
        CTkButton(master=frame,command=lambda : self.goToForgotPassowrd(frame), text="Forget Password?",fg_color="transparent", hover_color="#E44982", font=("Arial Bold", 12), text_color="#601E88", width=120, height=20).place(relx=0.6,rely=0.77)

        CTkButton(master=frame, text="Login", fg_color="#601E88", command=lambda :self.submit(frame), hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, height=40).pack(anchor="w", pady=(55, 0), padx=(150, 0))
    
    def goToSignUp(self, currentFrame) :
        currentFrame.destroy()
        signUp.create_signup_ui(self)

    def goToForgotPassowrd(self, currentFrame):
        currentFrame.destroy()
        fg.create_Forgot_ui(self)

    def submit(self, currentFrame):
        print("Button Pressed")
        email = self.email_entry.get()
        password = self.password_entry.get()

        success, data = login(email, password)
        
        if success:
            
            print("User authenticated successfully!")
            print("User ID:", data["localId"])
            print("ID Token:", data["idToken"])
            messagebox.showinfo('Successful','Successfully Logged in!')
            self.open_home_screen(currentFrame,email)            #currentframe --------

        else:
            
            print("Authentication failed:", data)
            messagebox.showerror('Error', 'Wrong Credentials!')


    # def open_home_screen(self, currentFrame):
    #     currentFrame.destroy()  # Close the current sign-in window
    #     home.createHome(self) # Open the CustomTkinterApp window
    
    def open_home_screen(self,currentFrame, email):
        currentFrame.destroy()
        home.createHome(self, email) 

def createSignIN(frame) :
     SignInFormApp.create_signin_ui(frame)

def open_home_screen(self, currentFrame):
        currentFrame.destroy()  # Close the current sign-in window
        home.createHome(self) # Open the CustomTkinterApp window

if __name__ == "__main__":
    app = SignInFormApp()
    app.configure(fg_color = "#fae2fe")
    app.mainloop()
    
