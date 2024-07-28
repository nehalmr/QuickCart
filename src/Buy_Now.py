from customtkinter import *
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.messagebox as messagebox
import firebase
import Home as home
import About_Us as about


def create_template(newFrame,doc_id):
        print("BuyNow")
        upper_frame(newFrame) 
        lower_frame(newFrame)
        frame(newFrame,doc_id)  # Adjust the image path     
        

def upper_frame(self):
        #Upper Frame
        upper_frame = CTkFrame(master=self, width=1280, height=50, fg_color='#e662fc')
        upper_frame.place(relx=0, rely=0)
        
        about_us_button = CTkButton(upper_frame,text="About Us",
                                    command=lambda: goToAboutUs(self, ), fg_color='#b303d0', height=40, width=50, corner_radius=40)
        about_us_button.place(relx=0.06, rely=0.5, anchor='center')

        #Quickcart Label
        text_label = CTkLabel(master=upper_frame, text="QuickCart",anchor="w", justify="left",text_color="#601E88",  font=("Arial Bold", 24))
        text_label.place(relx=0.5, rely=0.5, anchor='center')
        

def _sub_function(count_label):
            global count  # Declare count as global
            if count == 0:
                return
            count -= 1
            count_label.config(text=str(count))

def _add_function(count_label):
            global count  # Declare count as global
            count += 1
            count_label.config(text=str(count))

count = 0 
def frame(self, doc_id):
        # count = 0
        print("In frame 1")
        Frame1 = CTkFrame(master=self, 
                    width=800,
                    height=500,
                    fg_color='#f5c2fe')
        Frame1.place(relx=0.5, rely=0.5, anchor='center')
        
        data = firebase.get_document('Product', doc_id)
        for key, value in data.items():
            if key == 'name':
                name = value
            elif key == 'price':
                price = value
            elif key == 'description':
                description = value
            elif key == 'img_path':
                image_path = value
                
        #photo of product
        inFrame = CTkFrame(master=Frame1,
                width=250,
                height=250,
                corner_radius=20,
                fg_color="white")

        inFrame.place(relx=0.5, rely=0.1, anchor='n')
        
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        product_image_label = CTkLabel(master=inFrame, image=photo, text="")
        product_image_label.image = photo
        product_image_label.configure(image=photo)
        product_image_label.pack()

        # ... (rest of your code)
        name_label = CTkLabel(master=Frame1, text=f"Name: {name}", font=("Arial", 16))
        name_label.place(relx=0.5, rely=0.4, anchor='center')

        price_label = CTkLabel(master=Frame1, text=f"Price: {price}", font=("Arial", 16))
        price_label.place(relx=0.5, rely=0.5, anchor='center')

        description_label = CTkLabel(master=Frame1, text=f"Description: {description}", font=("Arial", 16))
        description_label.place(relx=0.5, rely=0.6, anchor='center')

        #Frame is added for Quantity
        # frameadd = CTkFrame(Frame1, fg_color="#fae2fe",height=40, width=200, corner_radius=70)
        # frameadd.place(relx=0.387, rely=0.75, anchor='center')
    

        # Create a label to display the count of both addition and subtraction
        count_label = tk.Label(Frame1, text=str(count), height=3, width=5)
        count_label.place(relx=0.42, rely=0.78)
    
        # Create the subtraction button
        sub_button = tk.Button(Frame1, text='-',height=3, width=5,command=lambda : _sub_function(count_label))
        sub_button.place(relx=0.38, rely=0.78)

        # Create the addition button
        add_button = tk.Button(Frame1, text='+',height=3, width=5, command=lambda: _add_function(count_label))
        add_button.place(relx=0.46, rely=0.78)

        checkout_button = CTkButton(self, text="Checkout", command=lambda : _checkout_function(self), fg_color='#b303d0',bg_color='#f5c2fe', font=("Arial", 14), height=40, width=150, corner_radius=40)
        checkout_button.place(relx=0.6, rely=0.75, anchor='center')  
    
def _checkout_function(self):
        if(count == 0) :
            messagebox.showerror('Unsuccessful','Please add products to buy')
        else:
            messagebox.showinfo(f"Successful",f"Placed {count} products!")

def add_to_cart():
        print("Product added to cart")

def remove_from_cart():
        print("Product removed from cart")



def lower_frame(self):
        #Lower Frame
        lower_frame = CTkFrame(master=self, width=1280, height=50, fg_color='#e662fc')
        lower_frame.place(relx=0, rely=1, anchor="sw")
        
        #Home Button
        home_button = CTkButton(master=lower_frame, fg_color="#b303d0", text="Home", width=20, height=40, corner_radius=100, command=open_home_screen(self))
        home_button.place(relx=0.5, rely=0.1, anchor='n')

def open_home_screen(self):
        Frame = CTkFrame(master=self, 
                    width=1280,
                    height=600,
                    fg_color='#fae2fe')
        # Frame.place(relx=0, rely=1, anchor="sw") 
        email = 'email'
        home.createHome(Frame, email) # Open the CustomTkinterApp window
        # pass
        
def goToAboutUs(newFrame) :

        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0.5, rely=0.5, anchor="center") 
        email = 'dummy@gmail.com'
        about.create_aboutUs_template(Frame, email)
        # currentFrame.destroy()
        # Frame1.destroy()
