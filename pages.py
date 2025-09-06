from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("custom_theme.json")


def profiles_page():
    """Opens the profiles/login page of the program.
    """
    root = ctk.CTk()

    #Defining the window's properties
    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")



    app_name_header = ctk.CTkFrame(master_frame)
    app_name_header.pack(side = "top", pady = "5")
    
    app_name_header_caps = ctk.CTkLabel(app_name_header, text = "Caps", font = ("Hammersmith One", 70), fg_color = "#100d80")
    app_name_header_caps.pack(side = "left")
    
    app_name_header_u = ctk.CTkLabel(app_name_header, text = "U", font = ("Hammersmith One", 70), text_color = "#DD3E3E", fg_color = "#100d80")
    app_name_header_u.pack(side = "left")

    

    root.mainloop()

def home_page():
    """Opens the home page of the program.
    """
    root = ctk.CTk()

    #Defining the window's properties
    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")



    #The title header for the home page
    app_name_header = ctk.CTkFrame(master_frame)
    app_name_header.pack(side = "top", pady = "5")
    
    app_name_header_caps = ctk.CTkLabel(app_name_header, text = "Caps", font = ("Hammersmith One", 70), fg_color = "#100d80")
    app_name_header_caps.pack(side = "left")
    
    app_name_header_u = ctk.CTkLabel(app_name_header, text = "U", font = ("Hammersmith One", 70), text_color = "#DD3E3E", fg_color = "#100d80")
    app_name_header_u.pack(side = "left")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame, fg_color = "#0c0a6e", bg_color = "transparent")
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    root.geometry("300")


    current_user_display = ctk.CTkLabel(home_page_toolbar_frame, text = "CurrentUser")
    current_user_display.pack(side = "left", padx = "10")

    profile_switch_button = ctk.CTkButton(home_page_toolbar_frame, text = "Switch Profile", width = 50, command = profiles_page)
    profile_switch_button.pack(side = "right", pady = "5", padx = "5")

    schedule_frame = ctk.CTkFrame(master_frame, fg_color = "#DD3E3E")
    schedule_frame.pack(side = "top", fill = "x", pady = "10", padx = "15")

    schedule_header = ctk.CTkFrame(schedule_frame)
    schedule_header.pack(side = "top", pady = "5")

    schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Hammersmith One", 25), bg_color = "#DD3E3E", text_color = "#EFEFEF")
    schedule_header_title.pack(side = "left", anchor = "w")

    schedule_body = ctk.CTkScrollableFrame(schedule_frame, width = 400, height = 350, fg_color = "#EFEFEF")
    schedule_body.pack(side = "top", pady = "5")

    func.info_box(schedule_body, "Waking Up", "- Take x 1 LEVOTHYROXINE.")
    
    func.info_box(schedule_body, "Breakfast", "- Take x 1 IBUPROFEN.\n- Take x 2 LISINOPRIL.")

    func.info_box(schedule_body, "Dinner", "- Take x 1 ATORVASTATIN.")
    
    func.info_box(schedule_body, "Before Bed", "- Take x 2 ISOTRETINOIN.")



    func.footer_button(master_frame, medication_list_page, "Medications")

    root.mainloop()
    


    
def medication_list_page():
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

    func.info_box(medications_content_frame, "LEVOTHYROXINE", "- Take x 1 after waking up.")
    
    func.info_box(medications_content_frame, "IBUPROFEN", "- Take x 1 after breakfast.")
    
    func.info_box(medications_content_frame, "LISINOPRIL", "- Take x 2 after breakfast.")
    
    func.info_box(medications_content_frame, "ATORVASTATIN", "- Take x 1 after dinner.")
    
    func.info_box(medications_content_frame, "ISOTRETINOIN", "- Take x 2 before bed.")
    
    
    func.footer_button(master_frame, add_medication_page, "Add a Medication")


    root.mainloop()

def add_medication_page():
    """Opens the page where the current user can add a medication to their list of medications.
    """
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 300)
    root.maxsize(400, 300)

    master_frame = ctk.CTkFrame(root, height = 300)
    master_frame.pack(fill = "both", expand = "True", pady = "20", padx = "20")

    medications_title = ctk.CTkLabel(master_frame, text = "Add a Medication", font = ("Hammersmith One", 25), text_color = "#EFEFEF")
    medications_title.pack(side = "top", anchor = "n")
    
    func.input_box(master_frame, "Medication Name")

    


    root.mainloop()