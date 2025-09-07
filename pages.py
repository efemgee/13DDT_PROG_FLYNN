#database stuff
import sqlite3
import hashlib

import customtkinter as ctk
import functions as func

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("custom_theme.json")




def log_in_page():
    """Opens the log in page of the program.
    """
    root = ctk.CTk()

    #Defining the window's properties
    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 400)
    root.maxsize(400, 400)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")

    def submit_log_in_details():
        entered_username = username_input_field.get()
        entered_password = hashlib.sha256(password_input_field.get().encode()).hexdigest()
    
        print (entered_username, entered_password)
        func.check_log_in_details(root, entered_username, entered_password)

    def close_program():
        root.destroy()

    app_name_header = ctk.CTkFrame(master_frame)
    app_name_header.pack(side = "top", pady = "5")
    
    app_name_header_caps = ctk.CTkLabel(app_name_header, text = "Caps", font = ("Hammersmith One", 70), fg_color = "#100d80")
    app_name_header_caps.pack(side = "left")
    
    app_name_header_u = ctk.CTkLabel(app_name_header, text = "U", font = ("Hammersmith One", 70), text_color = "#DD3E3E", fg_color = "#100d80")
    app_name_header_u.pack(side = "left")

    medications_title = ctk.CTkLabel(master_frame, text = "Log In", font = ("Hammersmith One", 25), text_color = "#EFEFEF")
    medications_title.pack(side = "top", anchor = "n", pady = "10")
    
    input_box_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e")
    input_box_frame.pack(side = "top")
    input_box_title = ctk.CTkLabel(input_box_frame, text="Username", fg_color = "#0c0a6e")
    input_box_title.pack(side = "top")
    username_input_field = ctk.CTkEntry(input_box_frame, placeholder_text="Type here...", width=200, height=20)
    username_input_field.pack(side = "top")
    
    input_box_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e")
    input_box_frame.pack(side = "top")
    input_box_title = ctk.CTkLabel(input_box_frame, text="Password", fg_color = "#0c0a6e")
    input_box_title.pack(side = "top")
    password_input_field = ctk.CTkEntry(input_box_frame, show = "*", placeholder_text="Type here...", width=200, height=20)
    password_input_field.pack(side = "top")
    
    submit_button = ctk.CTkButton(master_frame, text = "Submit", width = 50, command = submit_log_in_details)
    submit_button.pack(side = "top", pady = "5", padx = "5")
    
    submit_button = ctk.CTkButton(root, text = "Exit Program", width = 50, command = close_program)
    submit_button.pack(side = "bottom", pady = "10", padx = "5")

    root.mainloop()

def home_page(current_user):
    """Opens the home page of the program.
    """
    homeroot = ctk.CTk()
    
    #Defining the window's properties
    homeroot.title("CapsU")
    homeroot.geometry("400x600")
    homeroot.minsize(400, 600)
    homeroot.maxsize(400, 600)

    master_frame = ctk.CTkFrame(homeroot)
    master_frame.pack(fill = "x", expand = "True")

    def log_out():
        homeroot.destroy()
        log_in_page()

    #The title header for the home page
    app_name_header = ctk.CTkFrame(master_frame)
    app_name_header.pack(side = "top", pady = "5")
    
    app_name_header_caps = ctk.CTkLabel(app_name_header, text = "Caps", font = ("Hammersmith One", 70), fg_color = "#100d80")
    app_name_header_caps.pack(side = "left")
    
    app_name_header_u = ctk.CTkLabel(app_name_header, text = "U", font = ("Hammersmith One", 70), text_color = "#DD3E3E", fg_color = "#100d80")
    app_name_header_u.pack(side = "left")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e", bg_color = "transparent")
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    homeroot.geometry("300")


    current_user_display = ctk.CTkLabel(home_page_toolbar_frame, text = current_user)
    current_user_display.pack(side = "left", padx = "10")

    log_out_button = ctk.CTkButton(home_page_toolbar_frame, text = "Log Out", width = 50, command = log_out)
    log_out_button.pack(side = "right", pady = "5", padx = "5")

    schedule_frame = ctk.CTkFrame(master_frame, fg_color = "#DD3E3E")
    schedule_frame.pack(side = "top", fill = "x", pady = "10", padx = "15")

    schedule_header = ctk.CTkFrame(schedule_frame)
    schedule_header.pack(side = "top", pady = "5")

    schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Hammersmith One", 25), bg_color = "#DD3E3E", text_color = "#EFEFEF")
    schedule_header_title.pack(side = "left", anchor = "w")

    schedule_body = ctk.CTkScrollableFrame(schedule_frame, width = 400, height = 350, fg_color = "#EFEFEF")
    schedule_body.pack(side = "top", pady = "5")



    func.daily_schedule(current_user, schedule_body)
    
    # func.info_box(schedule_body, "Waking Up", "- Take x 1 LEVOTHYROXINE.")
    
    # func.info_box(schedule_body, "Breakfast", "- Take x 1 IBUPROFEN.\n- Take x 2 LISINOPRIL.")

    # func.info_box(schedule_body, "Dinner", "- Take x 1 ATORVASTATIN.")
    
    # func.info_box(schedule_body, "Before Bed", "- Take x 2 ISOTRETINOIN.")



    func.footer_button(master_frame, lambda: medication_list_page(homeroot, current_user), "Medications")

    homeroot.mainloop()
    


    
def medication_list_page(main_root, current_user):
    """Opens the page showing the current user's list of current medications.
    """
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 500)
    root.maxsize(400, 500)

    master_frame = ctk.CTkFrame(root, height = 500)
    master_frame.pack(fill = "both", expand = "True")

    medications_frame = ctk.CTkFrame(master_frame, fg_color = "#DD3E3E")
    medications_frame.pack(side = "top", fill = "x", pady = "10", padx = "15")


    medications_title = ctk.CTkLabel(medications_frame, text = "Medications", font = ("Hammersmith One", 25), bg_color = "#DD3E3E", text_color = "#EFEFEF")
    medications_title.pack(side = "top", anchor = "n")

    medications_content_frame = ctk.CTkScrollableFrame(medications_frame, width = 400, height = 400, fg_color = "#EFEFEF")
    medications_content_frame.pack(side = "top", fill = "both", pady = "5")


    func.medication_list(current_user, medications_content_frame)
    
    
    func.footer_button(master_frame, lambda: add_medication_page(main_root, root, current_user), "Add a Medication")


    root.mainloop()

def add_medication_page(main_root, med_list_root, current_user):
    """Opens the page where the current user can add a medication to their list of medications.
    """
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 250)
    root.maxsize(400, 250)

    master_frame = ctk.CTkFrame(root, height = 300)
    master_frame.pack(fill = "both", expand = "True", pady = "20", padx = "20")

    def submit_new_medication_details():
        medication_name = medication_name_input_field.get().upper()
        medication_dose = medication_dose_combo_box.get()
        medication_time = medication_time_combo_box.get().upper()
        
        medication_name_input_field.delete(0,99)
        medication_dose_combo_box.set("Choose a number...")
        medication_time_combo_box.set("Choose a time...")
        
        print (medication_name, medication_dose, medication_time)
        print(current_user)
        func.medication_to_database(current_user, medication_name, medication_dose, medication_time)
        
        med_list_root.destroy()
        root.destroy()
        main_root.destroy()
        home_page(current_user)
        


    medications_title = ctk.CTkLabel(master_frame, text = "Add a Medication", font = ("Hammersmith One", 25), text_color = "#EFEFEF")
    medications_title.pack(side = "top", anchor = "n")


    input_box_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e")
    input_box_frame.pack(side = "top")
    input_box_title = ctk.CTkLabel(input_box_frame, text="Medication Name", fg_color = "#0c0a6e")
    input_box_title.pack(side = "top")
    medication_name_input_field = ctk.CTkEntry(input_box_frame, placeholder_text="Type here...", width=200, height=20)
    medication_name_input_field.pack(side = "top")
    
    input_box_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e")
    input_box_frame.pack(side = "top")
    input_box_title = ctk.label = ctk.CTkLabel(input_box_frame, text="Dose Size", fg_color = "#0c0a6e")
    input_box_title.pack(side = "top")
    medication_dose_combo_box = ctk.entry = ctk.CTkComboBox(input_box_frame, state = "readonly", values = ["1", "2", "3", "4", "5"], width=200, height=20)
    medication_dose_combo_box.set("Choose a number...")
    medication_dose_combo_box.pack(side = "top")
    
    input_box_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e")
    input_box_frame.pack(side = "top")
    input_box_title = ctk.label = ctk.CTkLabel(input_box_frame, text="Time of Day", fg_color = "#0c0a6e")
    input_box_title.pack(side = "top")
    medication_time_combo_box = ctk.entry = ctk.CTkComboBox(input_box_frame, state = "readonly", values = ["Waking Up", "Breakfast", "Lunch", "Dinner", "Before Bed"], width=200, height=20)
    medication_time_combo_box.set("Choose a time...")
    medication_time_combo_box.pack(side = "top")
    
    submit_button = ctk.CTkButton(master_frame, text = "Submit", width = 50, command = submit_new_medication_details)
    submit_button.pack(side = "top", pady = "5", padx = "5")


    root.mainloop()