from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("custom_theme.json")

def home_page():
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

    home_page_toolbar_buttons = ctk.CTkFrame(home_page_toolbar_frame, fg_color = "#0c0a6e")
    home_page_toolbar_buttons.pack(side = "right")

    profile_switch_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Switch Profile", width = 50, bg_color = "transparent")
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
    
    func.info_box(schedule_body, "Breakfast", "- Take x 1 IBUPROFEN.")

    func.info_box(schedule_body, "Lunch", "- Take x 2 LISINOPRIL.")

    func.info_box(schedule_body, "Dinner", "- Take x 1 ATORVASTATIN.")
    
    func.info_box(schedule_body, "Before Bed", "- Take x 2 ISOTRETINOIN.")



    func.footer_button(master_frame, medications_page, "Medications")

    root.mainloop()
    

def profiles_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")

    app_name_header = ctk.CTkLabel(master_frame, text = "CapsU", font = ("Hammersmith One", 50), pady = "5")
    app_name_header.pack(side = "top")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame)
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    root.geometry("300")


    


    root.mainloop()
    
def medications_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root, height = 500)
    master_frame.pack(fill = "both", expand = "True")

    medications_frame = ctk.CTkFrame(master_frame, fg_color = "#DD3E3E")
    medications_frame.pack(side = "top", fill = "x", pady = "10", padx = "15")


    medications_title = ctk.CTkLabel(medications_frame, text = "Medications", font = ("Hammersmith One", 20), bg_color = "#DD3E3E", text_color = "#EFEFEF")
    medications_title.pack(side = "top", anchor = "n")

    medications_content_frame = ctk.CTkScrollableFrame(medications_frame, fg_color = "#EFEFEF", width = 400)
    medications_content_frame.pack(side = "top", fill = "both", pady = "5")

    func.info_box(medications_content_frame, "Isotretinoin", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(medications_content_frame, "Adderall", "- Your ADDERALL prescription can now be renewed.")
    
    
    #func.footer_button(master_frame, add_prescription_page, "Add a Prescription")


    root.mainloop()
