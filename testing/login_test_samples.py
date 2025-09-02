#database stuff
import sqlite3
import hashlib

#gui stuff
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("/theme.json")



conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS logindata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")


def new_user(username = str, password = str):
    username_to_enter, password_to_enter = username, hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO logindata (username, password) VALUES (?, ?)", (username_to_enter, password_to_enter))

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {username} (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            dose INTEGER NOT NULL,
            time VARCHAR(255) NOT NULL
            )
            """)
    
# def submit_on_click():
#     username = username_input.get()
#     password = password_input.get()
    
#     if username and password:
#         #check_login_details
#     else:
        #message: 'please fill out all fields'
    
#checks the username and passcode against the database
#def check_login_details:
    #take the values input into the entryboxes once the submit button has been pressed, then encode them.
    #see if these encoded versions match the encoded versions already in the database.
    #if they do, run login_to_user().
    #if they don't, then message: 'incorrect login details, please try again or return to main menu'

#puts the program into a state of being logged into one profile
#def login_to_user():
    #if the passcode and username used to attempt a login have matched the database, then this function will be used to close the login page and open the home page in a state where the profile that was successfully logged into is the current user.

#opens the home page gui in a certain user's possesion
#def open_home():
    #opens the home page gui, with the current user's username in the top right corner. this corner or the opposite on will have a button that closes the home page and returns to the profile select/login screen.
    #runs med_box_organise() to fill the page with the current user's medication


#creates a medication box out of parts of a list that it is given, then packs that box into a certain part of a home page based on the final parameter in the list.
#def med_box_organise():
    #makes the gui of the med box
    #packs the second and third parts of the list into the phrase 'Take [3] [2] pills.'
    #once complete, the box is packed into the home page gui based on the fourth part of the list. it will be either 'waking up', 'breakfast', 'lunch', 'dinner', 'before bed'
    
#Retrieves prescription table of current user
def retrieve_prescriptions(current_user = str):
    current_prescriptions = cur.execute(f"""SELECT * FROM {current_user} WHERE id >= 0""")
    print(current_prescriptions)
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        #make a function that will take the specifications within this list and put it into a gui box. Format the home page so that there are separate boxes that this function can pack things into depending on what time of day the medication must be taken.
        

# username1, password1 = "frankinside", hashlib.sha256("bolts".encode()).hexdigest()
# username2, password2 = "orpo", hashlib.sha256("poor".encode()).hexdigest()
# username3, password3 = "plaktuk", hashlib.sha256("kultklap".encode()).hexdigest()
# username4, password4 = "pikpluk", hashlib.sha256("toothpik".encode()).hexdigest()
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

new_user("frankinside", "bolts")
new_user("orpo", "poor")
new_user("plaktuk", "kultklap")
new_user("pikpluk", "toothpik")

current_user = "frankinside"

retrieve_prescriptions(current_user)

conn.commit()