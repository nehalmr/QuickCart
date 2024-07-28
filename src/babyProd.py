from customtkinter import *
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as messagebox
import Home as home
import tkinter
import Profile as fm
import About_Us as about
import Buy_Now as buynow

def createProductTemplate(currentFrame,newFrame, email) :
    
    upperframe(newFrame)
#     rightFrame(newFrame)
    leftFrame(newFrame)
    lowerframe(newFrame, email)
    dummy_rightframe(newFrame)


def upperframe(newFrame):
        upperFrame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=50,
                    fg_color='#e662fc')
        upperFrame.place(relx=0, rely=0)


        text_label = CTkLabel(master=upperFrame, text="QuickCart",anchor="w", justify="left",text_color="#601E88",  font=("Arial Bold", 24))
        text_label.place(relx=0.5, rely=0.5, anchor='center')

        search_icon_image = CTkImage(light_image=Image.open('assets/searchr.png'),
                                     dark_image=Image.open('assets/searchr.png'),
                                     size=(15, 15))

        search_icon_button = CTkButton(upperFrame, text="search", image=search_icon_image,
                                       command=lambda: print("Search clicked"), fg_color='#b303d0')
        search_icon_button.place(relx=0.7, rely=0.5, anchor='center')

        search_entry = CTkEntry(upperFrame, width=300)
        search_entry.place(relx=0.87, rely=0.5, anchor='center')

        about_us_image = CTkImage(light_image=Image.open('assets/aboutus.png'),
                                  dark_image=Image.open('assets/aboutus.png'),
                                  size=(35, 35))

        about_us_button = CTkButton(upperFrame,text="About Us",
                                    command=lambda: goToAboutUs(upperFrame), fg_color='#b303d0', height=40, width=50, corner_radius=40,)
        about_us_button.place(relx=0.06, rely=0.5, anchor='center')

frame2 = None
def leftFrame(newFrame) :
        #first frame - list of product
        frame1 = ctk.CTkFrame(master=newFrame,
                 width = 600,
                 height = 550,
                #  corner_radius = 20,
                 fg_color = "#f5c2fe")

        frame1.grid(row=1, column=0, pady=50, padx=0)

        # Add a label "Baby Product" above innerFrame
        label_baby_product = ctk.CTkLabel(master=frame1, text="Baby Product", fg_color="#f5c2fe", text_color="#601E88",  font=("Arial Bold", 24))
        label_baby_product.place(relx=0.04, rely=0.03)
            
        #list - contains products
        innerFrame = ctk.CTkScrollableFrame(master=frame1,
                 width = 400,
                 height = 400,
                 corner_radius = 20,
                 fg_color = "white")

        # list - contains product
        # Set relx and rely to place frame3 in the center
        innerFrame.place(relx=0.5, rely=0.5, anchor='center')

        pf1 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf1.grid(row=0, column=0, padx=20, pady=10)
        #Added Image
        image_path = "assets/B1.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        # B1 = ctk.CTkButton(master=pf1, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B1'))
        B1 = ctk.CTkButton(master=pf1, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B1', newFrame))
        B1.image = Image
        B1.pack()

        pf2 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf2.grid(row=0, column=1,padx=20, pady=10)
        #Added Image
        image_path = "assets/B2.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B2 = ctk.CTkButton(master=pf2, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B2', newFrame))
        B2.image = Image
        B2.pack()

        pf3 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf3.grid(row=1, column=0,padx=20, pady=10)
        #Added Image
        image_path = "assets/B3.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B3 = ctk.CTkButton(master=pf3, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B3', newFrame))
        B3.image = Image
        B3.pack()

        pf4 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf4.grid(row=1, column=1,padx=20, pady=10)
        #Added Image
        image_path = "assets/B4.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B4 = ctk.CTkButton(master=pf4, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B4', newFrame))
        B4.image = Image
        B4.pack()

        pf5 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf5.grid(row=2, column=0,padx=20, pady=10)
        #Added Image
        image_path = "assets/B5.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B5 = ctk.CTkButton(master=pf5, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B5', newFrame))
        B5.image = Image
        B5.pack()

        pf6 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf6.grid(row=2, column=1,padx=20, pady=10)
        #Added Image
        image_path = "assets/B6.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B6 = ctk.CTkButton(master=pf6, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B6', newFrame))
        B6.image = Image
        B6.pack()

        pf7 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf7.grid(row=3, column=0,padx=20, pady=10)
        #Added Image
        image_path = "assets/B7.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B7 = ctk.CTkButton(master=pf7, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B7', newFrame))
        B7.image = Image
        B7.pack()

        pf8 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf8.grid(row=3, column=1,padx=20, pady=10)
        #Added Image
        image_path = "assets/B8.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B8 = ctk.CTkButton(master=pf8, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B8', newFrame))
        B8.image = Image
        B8.pack()

        pf9 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")
        pf9.grid(row=4, column=0,padx=20, pady=10)
        #Added Image
        image_path = "assets/B9.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B9 = ctk.CTkButton(master=pf9, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B9', newFrame))
        B9.image = Image
        B9.pack()

        pf10 = ctk.CTkFrame(master=innerFrame,
                        width = 150,
                        height = 150,
                        corner_radius = 5,
                        fg_color = "lightgray")
        pf10.grid(row=4, column=1,padx=20, pady=10)
        #Added Image
        image_path = "assets/B10.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        B10 = ctk.CTkButton(master=pf10, image=photo, text="", height=5, width=5, corner_radius=5, command=lambda: showData('B10', newFrame))
        B10.image = Image
        B10.pack()
        
def dummy_rightframe(newFrame) :

        #second frame - description of product
        frame2 = ctk.CTkFrame(master=newFrame,
                 width = 680,
                 height = 550,
                #  corner_radius = 20,
                 fg_color = "#fae2fe",
                )

        # frame2.pack(padx=20, pady=20)
        frame2.grid(row=1, column=1)

def rightFrame(newFrame, name, price, description, image_path, doc_id) :

        #second frame - description of product
        frame2 = ctk.CTkFrame(master=newFrame,
                 width = 680,
                 height = 550,
                #  corner_radius = 20,
                 fg_color = "#fae2fe",
                )

        # frame2.pack(padx=20, pady=20)
        frame2.grid(row=1, column=1)

        #photo pf product
        inFrame = ctk.CTkFrame(master=frame2,
                 width = 250,
                 height = 250,
                 corner_radius = 20,
                 fg_color = "white")

        inFrame.place(relx=0.5, rely=0.1, anchor='n')
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        product_image_label = ctk.CTkLabel(master=inFrame, image=photo, text="")
        product_image_label.image = photo
        product_image_label.pack()

        name_label = ctk.CTkLabel(master=frame2, text=f"Name: {name}", font=("Arial", 16))
        name_label.place(relx=0.5, rely=0.4, anchor='center')

        price_label = ctk.CTkLabel(master=frame2, text=f"Price: {price}", font=("Arial", 16))
        price_label.place(relx=0.5, rely=0.5, anchor='center')

        description_label = ctk.CTkLabel(master=frame2, text=f"Description: {description}", font=("Arial", 16))
        description_label.place(relx=0.5, rely=0.6, anchor='center')

        #create button add to cart
        cart = ctk.CTkButton(master=frame2, text="Add to Cart", fg_color="#b303d0", width=210, height=40)
        cart.place(relx=0.3, rely=0.9, anchor='s')

        buy = ctk.CTkButton(master=frame2, text="Buy Now", fg_color="#b303d0", width=210, height=40, command=lambda: goToBuyNow(newFrame,doc_id))
        buy.place(relx=0.7, rely=0.9, anchor='s')
                
def lowerframe(newFrame, email) :
        #lower frame (bar)
        lowerFrame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=50,
                    fg_color='#e662fc')
        lowerFrame.place(relx=0, rely=1, anchor="sw") 

        #profile button
        profile = CTkButton(master=lowerFrame, fg_color="#b303d0",text="Profile", width=210, height=40, corner_radius=80,command=lambda : goToProfile(lowerFrame,newFrame))
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        profile.place(relx=0, rely=0.1, anchor='nw')

        #home button
        home = CTkButton(master=lowerFrame, fg_color="#b303d0", text="Home", width=20, height=40, corner_radius=100, command=lambda: open_home_screen(lowerFrame, newFrame, email))
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        home.place(relx=0.5, rely=0.1, anchor='n')

        #Cart button
        cart2 = CTkButton(master=lowerFrame,  fg_color="#b303d0",text="Cart", width=210, height=40, corner_radius=80)
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        cart2.place(relx=1, rely=0.1, anchor='ne')

def open_home_screen(currentFrame, newFrame, email):

        # currentFrame.destroy()  # Close the current sign-in window
        Frame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=600,
                    fg_color='#fae2fe')
        Frame.place(relx=0, rely=1, anchor="sw") 
        home.createHome(newFrame, email) # Open the CustomTkinterApp window
        
def goToProfile(currentFrame, newFrame) :
      
        currentFrame.destroy()
#       Frame = CTkFrame(master=newFrame, 
#                     width=1280,
#                     height=650,
#                     fg_color='#fae2fe')
#       Frame.place(relx=0, rely=1, anchor="sw") 
        fm.create_template(newFrame)

def goToAboutUs(currentFrame, newFrame) :
        
        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0.5, rely=0.5, anchor="center") 
        about.create_aboutUs_template(Frame)

def showData(doc_id, right_frame):
    import firebase
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

    # Assuming you have a label in the right frame to display the extracted data
    rightFrame(right_frame, name, price, description, image_path, doc_id)


def goToBuyNow(newFrame,doc_id) :
        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0.5, rely=0.5, anchor="center") 
        buynow.create_template(Frame,doc_id)