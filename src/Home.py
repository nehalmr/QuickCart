from customtkinter import CTk, CTkImage, CTkButton, CTkFrame, CTkEntry, CTkLabel
from PIL import Image
import customtkinter
import babyProd as tm
import tkinter as tk
import tkinter
import Profile as fm
import babyProd as bp
import cosmetic as cs
import electronics as el
import sport as sp
import About_Us as about
import cart as Cart

def createHome(newFrame, email) :
    create_upper_frame(newFrame, email)
    createFrame(newFrame, email)
    lowerframe(newFrame, email)
#     lowerframe(newFrame)

    
# def open_home_screen(currentFrame, newFrame):
#     currentFrame.destroy()  # Close the current frame
#     createHome(newFrame) 

def open_home_screen(newFrame, email):
    
    createHome(newFrame, email)  

def create_upper_frame(newFrame, email):
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
                                    command=lambda: goToAboutUs(upperFrame,newFrame, email), fg_color='#b303d0', height=40, width=50, corner_radius=40)
        about_us_button.place(relx=0.06, rely=0.5, anchor='center')

Frame1 = None      
def createFrame(newFrame, email):
    Frame1 = CTkFrame(master=newFrame, 
                      width=800,
                      height=500,
                      fg_color='#f5c2fe')
    Frame1.place(relx=0.5, rely=0.5, anchor='center')

    image_paths = ['assets/beauty-product.png', 'assets/sports.png', 'assets/cosmetics.png', 'assets/electronic1.png']
    functions = [bp.createProductTemplate, sp.createSportTemplate, cs.createCosmeticTemplate, el.createElectronicTemplate]

    for i, path in enumerate(image_paths):
        image = CTkImage(light_image=Image.open(path),
                        dark_image=Image.open(path),
                        size=(300, 200))

        label = CTkLabel(Frame1, corner_radius=25, image=image, anchor='e', text="", fg_color="#f5c2fe")
        label.grid(row=i // 2, column=i % 2, padx=25, pady=20)

        # Set bg_color to be transparent or the same as the Frame1's background color
        image_button = CTkButton(label, corner_radius=25, text_color="#f5c2fe", image=image,
                                command=lambda i=i: functions[i](Frame1, newFrame, email), bg_color='#f5c2fe', fg_color="#f5c2fe")
        image_button.place(relx=0.6, rely=0.5, anchor='center')

def lowerframe(newFrame, email) :
        #lower frame (bar)
        lowerFrame = CTkFrame(master=newFrame, 
                    width=1280,
                    height=50,
                    fg_color='#e662fc')
        lowerFrame.place(relx=0, rely=1, anchor="sw") 

        #profile button
        profile = CTkButton(master=lowerFrame, fg_color="#b303d0",text="Profile", width=210, height=40, corner_radius=80, command=lambda : goToProfile(newFrame, email))
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        profile.place(relx=0, rely=0.1, anchor='nw')

        #profile button
        home = CTkButton(master=lowerFrame, fg_color="#b303d0", text="Home", width=20, height=40, corner_radius=100)
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        home.place(relx=0.5, rely=0.1, anchor='n')

        #Cart button
        cart2 = CTkButton(master=lowerFrame,  fg_color="#b303d0",text="Cart", width=210, height=40, corner_radius=80, command=lambda: goToCart(lowerFrame, newFrame))
        # profile.place(relx=0, rely=0 padx=5, pady=5)
        cart2.place(relx=1, rely=0.1, anchor='ne')

def goToTemplate(currentFrame, newFrame, email) :
        currentFrame.destroy()
        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0, rely=0, anchor="sw") 
        bp.createProductTemplate(Frame, email)

def goToProfile(newFrame, doc_id) :
      
        # currentFrame.destroy()
        import firebase
        data = firebase.get_document('User_data', doc_id)
        for key, value in data.items() :
                if(key == 'name') :
                        name = value
                if (key == 'email'):
                        email = value
                if (key == 'phoneNo'):
                        phoneNo = value
                if (key == 'age'):
                        age = value
                if (key == 'password'):
                        password = value
                              
        print(name)
        print(email)
        print(phoneNo)
        print(age)
        print(password)

        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0, rely=0, anchor="sw") 
        # fm.create_template(newFrame)
        fm.create_template(newFrame, name, email, phoneNo, age)

def goToAboutUs(currentFrame, newFrame, email) :

        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0.5, rely=0.5, anchor="center") 
        about.create_aboutUs_template(Frame, email)
        # currentFrame.destroy()
        # Frame1.destroy()

def goToCart(currentFrame, newFrame) :
        
        Frame = CTkFrame(master=newFrame, 
                        width=1280,
                        height=650,
                        fg_color='#fae2fe')
        Frame.place(relx=0, rely=0, anchor="sw") 
        Cart.createCart(newFrame)

        
