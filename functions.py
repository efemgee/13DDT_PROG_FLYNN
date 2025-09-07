#database stuff
import sqlite3
import hashlib

import customtkinter as ctk
import pages

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("custom_theme.json")

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()


#LISTING STUFF -----------------------------------------------------------------

def daily_schedule(user, parent_frame):
    
    current_prescriptions = cur.execute(f"""SELECT * FROM {user} WHERE id >= 0""")
    print(current_prescriptions)
    rows = cur.fetchall()
    
    waking_up_meds = []
    breakfast_meds = []
    lunch_meds = []
    dinner_meds = []
    before_bed_meds = []
        
    for row in rows:
        if "WAKING UP" in row:
            waking_up_meds.append(row)
        elif "BREAKFAST" in row:
            breakfast_meds.append(row)
        elif "LUNCH" in row:
            lunch_meds.append(row)
        elif "DINNER" in row:
            dinner_meds.append(row)
        elif "BEFORE BED" in row:
            before_bed_meds.append(row)
    print(waking_up_meds)
    print(breakfast_meds)
    print(lunch_meds)
    print(dinner_meds)
    print(before_bed_meds)
    
    if waking_up_meds:
        med_content = ""
        for med in waking_up_meds:
            med_name = med[1]
            med_dose = med[2]
            med_time = med[3]
            
            med_content += f"- Take x {med_dose} {med_name}.\n"
        
        info_box(parent_frame, med_time.title(), med_content)
        
    if breakfast_meds:
        med_content = ""
        for med in breakfast_meds:
            med_name = med[1]
            med_dose = med[2]
            med_time = med[3]
            
            med_content += f"- Take x {med_dose} {med_name}.\n"
        
        info_box(parent_frame, med_time.title(), med_content)
    
    if lunch_meds:
        med_content = ""
        for med in lunch_meds:
            med_name = med[1]
            med_dose = med[2]
            med_time = med[3]
            
            med_content += f"- Take x {med_dose} {med_name}.\n"
        
        info_box(parent_frame, med_time.title(), med_content)
        
    if dinner_meds:
        med_content = ""
        for med in dinner_meds:
            med_name = med[1]
            med_dose = med[2]
            med_time = med[3]
            
            med_content += f"- Take x {med_dose} {med_name}.\n"
        
        info_box(parent_frame, med_time.title(), med_content)
        
    if before_bed_meds:
        med_content = ""
        for med in before_bed_meds:
            med_name = med[1]
            med_dose = med[2]
            med_time = med[3]
            
            med_content += f"- Take x {med_dose} {med_name}.\n"
        
        info_box(parent_frame, med_time.title(), med_content)
            
            
    

def medication_list(user, parent_frame):
    
    current_prescriptions = cur.execute(f"""SELECT * FROM {user} WHERE id >= 0""")
    print(current_prescriptions)
    rows = cur.fetchall()
    
    for row in rows:
        med_name = row[1]
        med_dose = row[2]
        med_time = row[3]
        
        if med_time == "BEFORE BED":  
            med_content = f"- Take x {med_dose} before bed."
        else:
            med_content = f"- Take x {med_dose} after {med_time.lower()}."
        
        info_box(parent_frame, med_name, med_content)
        
        
    


#DATABASE STUFF ----------------------------------------------------------------

def check_log_in_details(root, entered_username, entered_password):
    
    cur.execute("SELECT username FROM logindata WHERE username = ?", (entered_username,))
    correct_username = cur.fetchone()
    print(correct_username)
    
    if correct_username:
        cur.execute("SELECT password FROM logindata WHERE password = ?", (entered_password,))
        correct_password = cur.fetchone()
        
        print(correct_password)
        if correct_password:
            root.destroy()
            pages.home_page(entered_username)
            
        else:
            print("ERROR 2!")
    else:
        print("ERROR 1!")


def medication_to_database(user, medication_name, medication_dose, medication_time):
    
    print(user, medication_name, medication_dose, medication_time)
    
    cur.execute(f"""INSERT INTO {user} (name, dose, time)
                VALUES (?, ?, ?)""", (medication_name, medication_dose, medication_time))
    conn.commit()


# def retrieve_prescriptions(current_user = str):
#     current_prescriptions = cur.execute(f"""SELECT * FROM {current_user} WHERE id >= 0""")
#     print(current_prescriptions)
#     rows = cur.fetchall()
    
#     for row in rows:
#         print(row)


def new_user(username, password):
    username_to_enter, password_to_enter = username, hashlib.sha256(password.encode()).hexdigest()
    cur.execute("""INSERT OR IGNORE INTO logindata (username, password)
                VALUES (?, ?)""", (username_to_enter, password_to_enter))
    conn.commit()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {username} (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            dose INTEGER NOT NULL,
            time VARCHAR(255) NOT NULL
            )
            """)
    conn.commit()



#GUI ELEMENTS ------------------------------------------------------------------

def info_box(parent_frame, title = str, content = str):
    """Creates a box of information that can be used for items in a list.

    Args:
        parent_frame (parent): The frame that the box will be placed in.
        title (string, optional): The text that will be displayed as the title of the box. Defaults to str.
        content (string, optional): The text that is held within the box. Defaults to str.
    """
    #Creating the box
    box = ctk.CTkFrame(parent_frame, fg_color = "#DD3E3E")
    box.pack(side = "top", fill = "x", pady = "10", padx = "10")

    #Creating the box content
    box_title = ctk.CTkLabel(box, fg_color = "#DD3E3E", text_color = "#EFEFEF", text = title, font = ("Hammersmith One", 16))
    box_title.pack(side = "top", anchor = "w", padx = "15", pady = "2")
    box_title_content_division = ctk.CTkFrame(box)
    box_title_content_division.pack(side = "top", anchor = "w", padx = "5", pady = "5", fill = "x")
    box_content = ctk.CTkTextbox(box_title_content_division, height = 50, width = 400, wrap = "word", bg_color = "#DD3E3E", fg_color = "#EFEFEF", text_color = "#17139C")
    box_content.insert("0.0", content)
    box_content.pack(side = "top", anchor = "w")


def footer_button(parent_frame, command_function, title = str):
    """Creates the footer buttons in a consistent style.

    Args:
        parent_frame (parent): The frame that the button will be placed in.
        command_function (_type_): The function for the button to execute upon being pressed.
        title (string, optional): The text that will be displayed on the button. Defaults to str.
    """
    button = ctk.CTkButton(parent_frame, text = title, command = command_function, width = 50)
    button.pack(side = "top", padx = 3)    
    
    
def input_box(parent_frame, title = str):
    """Creates a titled box that the user can input information into.

    Args:
        parent_frame (parent): The frame that the box will be placed in.
        title (string): The text that will be displayed as the title of the box. Defaults to str.
    """
    input_box_frame = ctk.CTkFrame(parent_frame, fg_color = "#0c0a6e")
    input_box_frame.pack(side = "top")
    input_box_title = ctk.CTkLabel(input_box_frame, text=title, fg_color = "#0c0a6e")
    input_box_title.pack(side = "top")
    input_field = ctk.CTkEntry(input_box_frame, placeholder_text="Type here...", width=200, height=20)
    input_field.pack(side = "top")
    
    
def selection_box(parent_frame, title = str):
    """Creates a titled selection box that the user can choose an option from.

    Args:
        parent_frame (parent): The frame that the box will be placed in.
        title (string): The text that will be displayed as the title of the box. Defaults to str.
    """
    input_box_frame = ctk.CTkFrame(parent_frame)
    input_box_frame.pack(side = "top")
    input_box_title = ctk.label = ctk.CTkLabel(input_box_frame, text=title)
    input_box_title.pack(side = "top")
    combo_box = ctk.entry = ctk.CTkComboBox(input_box_frame, state = "readonly", values = ["Choose a number of pills...", 1, 2, 3, 4, 5], width=200, height=20)
    combo_box.pack(side = "top")
