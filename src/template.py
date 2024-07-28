from customtkinter import *
from tkinter import *
import customtkinter as ctk
from PIL import Image
import tkinter as tk
import tkinter
from tkinter import messagebox
import tkinter.messagebox as messagebox
import Home as home

def createTemplate(newFrame) :
    upperframe(newFrame)
    leftFrame(newFrame)
    rightFrame(newFrame)
    lowerframe(newFrame)


# def upperframe(newFrame) :
#         # creating upper bar
#         upperFrame = ctk.CTkFrame(master=newFrame, 
#                     width=1280,
#                     height=50,
#                     fg_color='#1560BD')
#         upperFrame.place(relx=0, rely=0)
    
def upperframe(newFrame):
        upperFrame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=50,
                    fg_color='#e662fc')
        upperFrame.place(relx=0, rely=0)


        text_label = CTkLabel(upperFrame, text="QUICKCART", font=("Arial", 16, "bold"), fg_color="#e662fc")
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
                                    command=lambda: print("About Us clicked"), fg_color='#b303d0', height=40, width=50, corner_radius=40)
        about_us_button.place(relx=0.06, rely=0.5, anchor='center')

def leftFrame(newFrame) :
        #first frame - list of product
        frame1 = ctk.CTkFrame(master=newFrame,
                 width = 600,
                 height = 550,
                #  corner_radius = 20,
                 fg_color = "#f5c2fe")

        frame1.grid(row=1, column=0, pady=50)
            
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

        # #load image cricket kit
        # image_path = "src\Template\cricket_kit.jpg"
        # image = tk.PhotoImage(file = image_path)

        # crik_button = ctk.CTkButton(master=innerFrame,image=image, width = 150, height = 150, corner_radius=5)
        # crik_button.grid(row=0, column=0, padx=20, pady=20)

        pf2 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf2.grid(row=0, column=1,padx=20, pady=10)
        pf3 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf3.grid(row=1, column=0,padx=20, pady=10)

        pf4 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf4.grid(row=1, column=1,padx=20, pady=10)
        pf5 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf5.grid(row=2, column=0,padx=20, pady=10)

        pf6 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf6.grid(row=2, column=1,padx=20, pady=10)

        pf7 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf7.grid(row=3, column=0,padx=20, pady=10)

        pf8 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf8.grid(row=3, column=1,padx=20, pady=10)

        pf9 = ctk.CTkFrame(master=innerFrame,
                 width = 150,
                 height = 150,
                 corner_radius = 5,
                 fg_color = "lightgray")

        pf9.grid(row=4, column=0,padx=20, pady=10)

        pf10 = ctk.CTkFrame(master=innerFrame,
                        width = 150,
                        height = 150,
                        corner_radius = 5,
                        fg_color = "lightgray")

        pf10.grid(row=4, column=1,padx=20, pady=10)

def rightFrame(newFrame) :
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

        #create button add to cart
        cart = ctk.CTkButton(master=frame2, text="Add to Cart", fg_color="#b303d0", width=210, height=40)
        cart.place(relx=0.3, rely=0.9, anchor='s')

        buy = ctk.CTkButton(master=frame2, text="Buy Now", fg_color="#b303d0", width=210, height=40)
        buy.place(relx=0.7, rely=0.9, anchor='s')

# def lowerframe(newFrame) :
#         #lower frame (bar)
#         lowerFrame = ctk.CTkFrame(master=newFrame, 
#                     width=1280,
#                     height=50,
#                     fg_color='#000080')
#         lowerFrame.place(relx=0, rely=1, anchor="sw") 

#         #profile button
#         profile = ctk.CTkButton(master=lowerFrame, text="Profile", width=210, height=40, corner_radius=80)
#         # profile.place(relx=0, rely=0 padx=5, pady=5)
#         profile.place(relx=0, rely=0.1, anchor='nw')

#         #profile button
#         home = ctk.CTkButton(master=lowerFrame, text="Adaptix", width=20, height=40, corner_radius=100, command=lambda: open_home_screen(lowerframe, newFrame))
#         # profile.place(relx=0, rely=0 padx=5, pady=5)
#         home.place(relx=0.5, rely=0.1, anchor='n')

#         #Cart button
#         cart2 = ctk.CTkButton(master=lowerFrame, text="Cart", width=210, height=40, corner_radius=80)
#         # profile.place(relx=0, rely=0 padx=5, pady=5)
#         cart2.place(relx=1, rely=0.1, anchor='ne')
        
def lowerframe(newFrame) :
        #lower frame (bar)
        lowerFrame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=50,
                    fg_color='#e662fc')
        lowerFrame.place(relx=0, rely=1, anchor="sw") 

        #profile button
        profile = CTkButton(master=lowerFrame, fg_color="#b303d0",text="Profile", width=210, height=40, corner_radius=80)
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        profile.place(relx=0, rely=0.1, anchor='nw')

        #profile button
        home = CTkButton(master=lowerFrame, fg_color="#b303d0", text="Adaptix", width=20, height=40, corner_radius=100, command=lambda: open_home_screen(lowerFrame, newFrame))
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        home.place(relx=0.5, rely=0.1, anchor='n')

        #Cart button
        cart2 = CTkButton(master=lowerFrame,  fg_color="#b303d0",text="Cart", width=210, height=40, corner_radius=80)
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        cart2.place(relx=1, rely=0.1, anchor='ne')

def open_home_screen(currentFrame, newFrame):

        # currentFrame.destroy()  # Close the current sign-in window
        Frame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=600,
                    fg_color='#fae2fe')
        Frame.place(relx=0, rely=1, anchor="sw") 
        home.createHome(newFrame) # Open the CustomTkinterApp window

# def goToTemplate(currentFrame, newFrame) :
#         currentFrame.destroy()
#         tm.createTemplate(newFrame)
