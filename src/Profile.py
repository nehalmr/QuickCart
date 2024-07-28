from customtkinter import *
import customtkinter
from PIL import Image as PILImage
import Home as home
import tkinter as tk
from tkinter import *
import SigninMain as signin

def create_template(newFrame,name, email, phoneNo, age):
        upper_frame(newFrame)
        left_frame(newFrame,name, email, phoneNo, age)
        right_frame(newFrame)
        lower_frame(newFrame, email)

def upper_frame(newFrame):
        upper_frame = CTkFrame(master=newFrame, width=1280, height=50, fg_color='#e662fc')
        upper_frame.place(relx=0, rely=0)

        text_label = CTkLabel(master=upper_frame, text="QuickCart",anchor="w", justify="left",text_color="#601E88",  font=("Arial Bold", 24))
        text_label.place(relx=0.5, rely=0.5, anchor='center')

        about_us_button = CTkButton(master=upper_frame, text="About Us",
                                    command=lambda: print("About Us clicked"), fg_color='#b303d0', height=40, width=50, corner_radius=40)
        about_us_button.place(relx=0.06, rely=0.5, anchor='center')

def left_frame(newFrame,name, email, phoneNo, age):
        frame1 = CTkFrame(master=newFrame, width=600, height=550, fg_color="#f5c2fe")
        frame1.grid(row=1, column=0, pady=50, padx=0)
        side_img_data = PILImage.open("assets/pers.png")
        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(150, 180))
        CTkLabel(master=newFrame, text="", fg_color="#f5c2fe", bg_color="#f5c2fe", image=side_img).place(anchor='center', relx=0.25, rely=0.3)

        #name
        text_label = CTkLabel(frame1, text="Name: " + name, font=("Arial", 18, "bold"), fg_color="#f5c2fe")
        text_label.place(relx=0.5, rely=0.5, anchor='center')

        #email
        text_label = CTkLabel(frame1, text="Email: " + email, font=("Arial", 18, "bold"), fg_color="#f5c2fe")
        text_label.place(relx=0.5, rely=0.55, anchor='center')

        # phone no
        text_label = CTkLabel(frame1, text="Phone Number: " + str(phoneNo), font=("Arial", 18, "bold"), fg_color="#f5c2fe")
        text_label.place(relx=0.5, rely=0.6, anchor='center')

        #age
        text_label = CTkLabel(frame1, text="Age: " + str(age), font=("Arial", 18, "bold"), fg_color="#f5c2fe")
        text_label.place(relx=0.5, rely=0.65, anchor='center')
        

def right_frame(newFrame):
        frame2 = CTkFrame(master=newFrame, width=640, height=550, fg_color="#fae2fe")
        frame2.grid(row=1, column=1)

        history_button = CTkButton(master=frame2, text="History", fg_color='#b303d0',font=("Arial", 20, "bold"), height=50, width=200, corner_radius=40)
        history_button.place(relx=0.5, rely=0.15, anchor='center')

        # side_img_data = Image.open("assets/cart-.png")
        side_img_data = PILImage.open("assets/cart-.png")
        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(280, 280))
        CTkLabel(master=frame2, text="", fg_color="#fae2fe", bg_color="#f5c2fe", image=side_img).place(anchor='center', relx=0.5, rely=0.5)


def lower_frame(newFrame, email):
        lower_frame = CTkFrame(master=newFrame, width=1280, height=50, fg_color='#e662fc')
        lower_frame.place(relx=0, rely=1, anchor="sw")

        profile_button = CTkButton(master=lower_frame, fg_color="#b303d0", text="Profile", width=210, height=40, corner_radius=80)
        profile_button.place(relx=0, rely=0.1, anchor='nw')

        home_button = CTkButton(master=lower_frame, fg_color="#b303d0", text="Home", width=20, height=40, corner_radius=100, command=lambda : open_home_screen(lower_frame, newFrame, email))
        home_button.place(relx=0.5, rely=0.1, anchor='n')

        cart_button = CTkButton(master=lower_frame, fg_color="#b303d0", text="Log Out", width=210, height=40, corner_radius=80, command=lambda : goToSignIn(lower_frame, newFrame))
        cart_button.place(relx=1, rely=0.1, anchor='ne')

def open_home_screen(currentFrame, newFrame, email):

        currentFrame.destroy()  # Close the current sign-in window
        Frame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=600,
                    fg_color='#fae2fe')
        Frame.place(relx=0, rely=1, anchor="sw") 
        home.createHome(newFrame, email) # Open the CustomTkinterApp window
        
def goToSignIn(currentFrame, newFrame) :

        currentFrame.destroy()
        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0.5, rely=0.5, anchor="center") 
        signin.createSignIN(Frame)

