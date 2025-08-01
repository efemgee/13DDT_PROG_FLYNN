from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func



def home_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")

    app_name_header = ctk.CTkLabel(master_frame, text = "CapsU", font = ("Arial", 50), pady = "5")
    app_name_header.pack(side = "top")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame)
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    root.geometry("300")


    clock = ctk.CTkLabel(home_page_toolbar_frame, text = "9:30pm")
    clock.pack(side = "left")

    home_page_toolbar_buttons = ctk.CTkFrame(home_page_toolbar_frame)
    home_page_toolbar_buttons.pack(side = "right")

    profile_switch_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Profiles", width = 50)
    profile_switch_button.pack(side = "right")

    settings_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Settings", width = 50)
    settings_button.pack(side = "right")

    schedule_frame = ctk.CTkFrame(master_frame)
    schedule_frame.pack(side = "top", fill = "x", pady = "10")

    schedule_header = ctk.CTkFrame(schedule_frame)
    schedule_header.pack(side = "top", pady = "5")

    schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Arial", 20))
    schedule_header_title.pack(side = "left", anchor = "w")

    schedule_header_calendar_button = ctk.CTkButton(schedule_header, text = "Today on the Calendar")
    schedule_header_calendar_button.pack(side = "left", padx = "10", pady = "5")

    schedule_body = ctk.CTkScrollableFrame(schedule_frame, width = 400, height = 350)
    schedule_body.pack(side = "top", pady = "5")

    update_items_frame = ctk.CTkFrame(schedule_body)
    update_items_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    update_items_title = ctk.CTkLabel(update_items_frame, text = "Updates")
    update_items_title.pack(side = "top", padx = "5", anchor = "w")

    update_items_content_frame = ctk.CTkScrollableFrame(update_items_frame, width = 400, height = 20)
    update_items_content_frame.pack(side = "top")

    func.info_box(update_items_content_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(update_items_content_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


    #UPDATE THIS WITH MANUAL TITLE AND FRAME!!!!!!!!
    schedule_timeslots_frame = ctk.CTkFrame(schedule_body)
    schedule_timeslots_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    schedule_timeslots_title = ctk.CTkLabel(schedule_timeslots_frame, text = "Schedule")
    schedule_timeslots_title.pack(side = "top", padx = "5", anchor = "w")

    schedule_timeslots_content_frame = ctk.CTkScrollableFrame(schedule_timeslots_frame, width = 400, height = 50)
    schedule_timeslots_content_frame.pack(side = "top")

    func.info_box(schedule_timeslots_content_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")


    func.footer(master_frame)

    root.mainloop()
    

def profiles_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")

    app_name_header = ctk.CTkLabel(master_frame, text = "CapsU", font = ("Arial", 50), pady = "5")
    app_name_header.pack(side = "top")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame)
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    root.geometry("300")


    clock = ctk.CTkLabel(home_page_toolbar_frame, text = "9:30pm")
    clock.pack(side = "left")

    home_page_toolbar_buttons = ctk.CTkFrame(home_page_toolbar_frame)
    home_page_toolbar_buttons.pack(side = "right")

    profile_switch_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Profiles", width = 50)
    profile_switch_button.pack(side = "right")

    settings_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Settings", width = 50)
    settings_button.pack(side = "right")

    schedule_frame = ctk.CTkFrame(master_frame)
    schedule_frame.pack(side = "top", fill = "x", pady = "10")

    schedule_header = ctk.CTkFrame(schedule_frame)
    schedule_header.pack(side = "top", pady = "5")

    schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Arial", 20))
    schedule_header_title.pack(side = "left", anchor = "w")

    schedule_header_calendar_button = ctk.CTkButton(schedule_header, text = "Today on the Calendar")
    schedule_header_calendar_button.pack(side = "left", padx = "10", pady = "5")

    schedule_body = ctk.CTkFrame(schedule_frame)
    schedule_body.pack(side = "top", pady = "5")

    update_items_frame = ctk.CTkFrame(schedule_body)
    update_items_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    update_items_title = ctk.CTkLabel(update_items_frame, text = "Updates")
    update_items_title.pack(side = "top", padx = "5", anchor = "w")

    update_items_content_frame = ctk.CTkScrollableFrame(update_items_frame, width = 400)
    update_items_content_frame.pack(side = "top")

    func.info_box(update_items_content_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(update_items_content_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


    #UPDATE THIS WITH MANUAL TITLE AND FRAME!!!!!!!!
    schedule_timeslots_frame = ctk.CTkFrame(schedule_body)
    schedule_timeslots_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    schedule_timeslots_title = ctk.CTkLabel(schedule_timeslots_frame, text = "Schedule")
    schedule_timeslots_title.pack(side = "top", padx = "5", anchor = "w")

    schedule_timeslots_content_frame = ctk.CTkScrollableFrame(schedule_timeslots_frame, width = 400)
    schedule_timeslots_content_frame.pack(side = "top")

    func.info_box(schedule_timeslots_content_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")


    func.footer(master_frame)

    root.mainloop()

def new_profile_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")

    app_name_header = ctk.CTkLabel(master_frame, text = "CapsU", font = ("Arial", 50), pady = "5")
    app_name_header.pack(side = "top")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame)
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    root.geometry("300")


    clock = ctk.CTkLabel(home_page_toolbar_frame, text = "9:30pm")
    clock.pack(side = "left")

    home_page_toolbar_buttons = ctk.CTkFrame(home_page_toolbar_frame)
    home_page_toolbar_buttons.pack(side = "right")

    profile_switch_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Profiles", width = 50)
    profile_switch_button.pack(side = "right")

    settings_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Settings", width = 50)
    settings_button.pack(side = "right")

    schedule_frame = ctk.CTkFrame(master_frame)
    schedule_frame.pack(side = "top", fill = "x", pady = "10")

    schedule_header = ctk.CTkFrame(schedule_frame)
    schedule_header.pack(side = "top", pady = "5")

    schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Arial", 20))
    schedule_header_title.pack(side = "left", anchor = "w")

    schedule_header_calendar_button = ctk.CTkButton(schedule_header, text = "Today on the Calendar")
    schedule_header_calendar_button.pack(side = "left", padx = "10", pady = "5")

    schedule_body = ctk.CTkFrame(schedule_frame)
    schedule_body.pack(side = "top", pady = "5")

    update_items_frame = ctk.CTkFrame(schedule_body)
    update_items_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    update_items_title = ctk.CTkLabel(update_items_frame, text = "Updates")
    update_items_title.pack(side = "top", padx = "5", anchor = "w")

    update_items_content_frame = ctk.CTkScrollableFrame(update_items_frame, width = 400)
    update_items_content_frame.pack(side = "top")

    func.info_box(update_items_content_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(update_items_content_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


    #UPDATE THIS WITH MANUAL TITLE AND FRAME!!!!!!!!
    schedule_timeslots_frame = ctk.CTkFrame(schedule_body)
    schedule_timeslots_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    schedule_timeslots_title = ctk.CTkLabel(schedule_timeslots_frame, text = "Schedule")
    schedule_timeslots_title.pack(side = "top", padx = "5", anchor = "w")

    schedule_timeslots_content_frame = ctk.CTkScrollableFrame(schedule_timeslots_frame, width = 400)
    schedule_timeslots_content_frame.pack(side = "top")

    func.info_box(schedule_timeslots_content_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")


    func.footer(master_frame)

    root.mainloop()
    
def med_list_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root)
    master_frame.pack(fill = "x", expand = "True")

    app_name_header = ctk.CTkLabel(master_frame, text = "CapsU", font = ("Arial", 50), pady = "5")
    app_name_header.pack(side = "top")

    home_page_toolbar_frame = ctk.CTkFrame(master_frame)
    home_page_toolbar_frame.pack(side = "top", fill = "x", padx = "10")
    root.geometry("300")


    clock = ctk.CTkLabel(home_page_toolbar_frame, text = "9:30pm")
    clock.pack(side = "left")

    home_page_toolbar_buttons = ctk.CTkFrame(home_page_toolbar_frame)
    home_page_toolbar_buttons.pack(side = "right")

    profile_switch_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Profiles", width = 50)
    profile_switch_button.pack(side = "right")

    settings_button = ctk.CTkButton(home_page_toolbar_buttons, text = "Settings", width = 50)
    settings_button.pack(side = "right")

    schedule_frame = ctk.CTkFrame(master_frame)
    schedule_frame.pack(side = "top", fill = "x", pady = "10")

    schedule_header = ctk.CTkFrame(schedule_frame)
    schedule_header.pack(side = "top", pady = "5")

    schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Arial", 20))
    schedule_header_title.pack(side = "left", anchor = "w")

    schedule_header_calendar_button = ctk.CTkButton(schedule_header, text = "Today on the Calendar")
    schedule_header_calendar_button.pack(side = "left", padx = "10", pady = "5")

    schedule_body = ctk.CTkFrame(schedule_frame)
    schedule_body.pack(side = "top", pady = "5")

    update_items_frame = ctk.CTkFrame(schedule_body)
    update_items_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    update_items_title = ctk.CTkLabel(update_items_frame, text = "Updates")
    update_items_title.pack(side = "top", padx = "5", anchor = "w")

    update_items_content_frame = ctk.CTkScrollableFrame(update_items_frame, width = 400)
    update_items_content_frame.pack(side = "top")

    func.info_box(update_items_content_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(update_items_content_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


    #UPDATE THIS WITH MANUAL TITLE AND FRAME!!!!!!!!
    schedule_timeslots_frame = ctk.CTkFrame(schedule_body)
    schedule_timeslots_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

    schedule_timeslots_title = ctk.CTkLabel(schedule_timeslots_frame, text = "Schedule")
    schedule_timeslots_title.pack(side = "top", padx = "5", anchor = "w")

    schedule_timeslots_content_frame = ctk.CTkScrollableFrame(schedule_timeslots_frame, width = 400)
    schedule_timeslots_content_frame.pack(side = "top")

    func.info_box(schedule_timeslots_content_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")


    func.footer(master_frame)

    root.mainloop()
    
def calendar_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root, width = 400, height = 600)
    master_frame.pack(side = "top", fill = "both")


    #HEADER
    notif_frame = ctk.CTkFrame(master_frame, width = 400, height = 00)
    notif_frame.pack(side = "top", fill = "both")

    schedule_header = ctk.CTkFrame(notif_frame)
    schedule_header.pack(side = "top")


    #NOTIFICATIONS BODY
    notif_header_title = ctk.CTkLabel(schedule_header, text = "Notifications", font = ("Arial", 20))
    notif_header_title.pack(side = "left", anchor = "w", fill = "x", expand = "True", pady = "15")

    notif_body = ctk.CTkFrame(notif_frame)
    notif_body.pack(side = "top")

    #CURRENT MEDICATION TIMESLOT
    current_timeslot_frame = ctk.CTkFrame(notif_body)
    current_timeslot_frame.pack(side = "top", fill = "x", padx = "5")

    current_timeslot_title = ctk.CTkLabel(current_timeslot_frame, text = "Current Medication(s)")
    current_timeslot_title.pack(side = "top", padx = "5", anchor = "w")

    func.info_box(current_timeslot_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")

    #UPDATES
    update_items_frame = ctk.CTkFrame(notif_body)
    update_items_frame.pack(side = "top", fill = "x", padx = "5")

    update_items_title = ctk.CTkLabel(update_items_frame, text = "Updates")
    update_items_title.pack(side = "top", padx = "5", anchor = "w")

    func.info_box(update_items_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(update_items_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


    #FOOTER
    func.footer(master_frame)

    root.mainloop()

    
    
def notification_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x600")
    root.minsize(400, 600)
    root.maxsize(400, 600)

    master_frame = ctk.CTkFrame(root, width = 400, height = 600)
    master_frame.pack(side = "top", fill = "both")


    #HEADER
    notif_frame = ctk.CTkFrame(master_frame, width = 400, height = 00)
    notif_frame.pack(side = "top", fill = "both")

    schedule_header = ctk.CTkFrame(notif_frame)
    schedule_header.pack(side = "top")


    #NOTIFICATIONS BODY
    notif_header_title = ctk.CTkLabel(schedule_header, text = "Notifications", font = ("Arial", 20))
    notif_header_title.pack(side = "left", anchor = "w", fill = "x", expand = "True", pady = "15")

    notif_body = ctk.CTkFrame(notif_frame)
    notif_body.pack(side = "top")

    #CURRENT MEDICATION TIMESLOT
    current_timeslot_frame = ctk.CTkFrame(notif_body)
    current_timeslot_frame.pack(side = "top", fill = "x", padx = "5")

    current_timeslot_title = ctk.CTkLabel(current_timeslot_frame, text = "Current Medication(s)")
    current_timeslot_title.pack(side = "top", padx = "5", anchor = "w")

    func.info_box(current_timeslot_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")

    #UPDATES
    update_items_frame = ctk.CTkFrame(notif_body)
    update_items_frame.pack(side = "top", fill = "x", padx = "5")

    update_items_title = ctk.CTkLabel(update_items_frame, text = "Updates")
    update_items_title.pack(side = "top", padx = "5", anchor = "w")

    func.info_box(update_items_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

    func.info_box(update_items_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


    #FOOTER
    func.footer(master_frame)

    root.mainloop()
