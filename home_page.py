from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func


root = ctk.CTk()

root.title("CapsU")
root.geometry("400x600")

master_frame = ctk.CTkFrame(root)
master_frame.pack(fill = "x", expand = "True")

app_name_header = ctk.CTkLabel(master_frame, text = "CapsU", font = ("Arial", "50"), pady = "15")
app_name_header.pack(side = "top")

home_page_toolbar = ctk.CTkFrame(master_frame)
home_page_toolbar.pack(side = "top", fill = "x", padx = "30")

clock = ctk.CTkLabel(home_page_toolbar, text = "9:30pm")
clock.pack(side = "left")

home_page_toolbar_buttons = ctk.CTkFrame(home_page_toolbar)
home_page_toolbar_buttons.pack(side = "right")

profile_switch_button = ctk.CTkButton(home_page_toolbar, text = "Profiles")
profile_switch_button.pack(side = "right")

settings_button = ctk.CTkButton(home_page_toolbar, text = "Settings")
settings_button.pack(side = "right")

schedule_frame = ctk.CTkFrame(master_frame)
schedule_frame.pack(side = "top")

schedule_header = ctk.CTkFrame(schedule_frame)
schedule_header.pack(side = "top")

schedule_header_title = ctk.CTkLabel(schedule_header, text = "Today", font = ("Arial", "20"))
schedule_header_title.pack(side = "left", anchor = "w")

schedule_header_calendar_button = ctk.CTkButton(schedule_header, text = "Today on the Calendar")
schedule_header_calendar_button.pack(side = "left", padx = ("150", "0"))

schedule_body = ctk.CTkFrame(schedule_frame)
schedule_body.pack(side = "top")

update_items = LabelFrame(schedule_body, text = "Updates")
update_items.pack(side = "top", fill = "x", padx = "5")

update1 = ctk.CTkFrame(update_items)
update1.pack(side = "top", fill = "x", pady = "30")

update1_title = ctk.CTkLabel(update1, text = "Prescription")
update1_title.pack(side = "top", anchor = "w")

update1_content = ctk.CTkLabel(update1, text = "- Your ISOTRETINOIN prescription can now be renewed.")
update1_content.pack(side = "top", anchor = "w")

update2 = ctk.CTkFrame(update_items)
update2.pack(side = "top", fill = "x", pady = "30")

update2_title = ctk.CTkLabel(update1, text = "Prescription")
update2_title.pack(side = "top", anchor = "w")

update2_content = ctk.CTkLabel(update1, text = "- Your ADDERALL prescription can now be renewed.")
update2_content.pack(side = "top", anchor = "w")

schedule_timeslots = LabelFrame(schedule_body, text = "Schedule")
schedule_timeslots.pack(side = "top", fill = "x", padx = "5")

timeslot1 = ctk.CTkFrame(schedule_timeslots)
timeslot1.pack(side = "top", fill = "x", pady = "30")

timeslot1_title = ctk.CTkLabel(timeslot1, text = "9:30am")
timeslot1_title.pack(side = "top", anchor = "w")

timeslot1_content = ctk.CTkLabel(timeslot1, text = "- 2 x ISOTRETINOIN. Take with food and water.")
timeslot1_content.pack(side = "top", anchor = "w")


footer_frame = ctk.CTkFrame(master_frame)
footer_frame.pack(side = "bottom", pady = ("20", "0"))

home_button = ctk.CTkButton(footer_frame, text = "Home")
home_button.pack(side = "left")

calendar_button = ctk.CTkButton(footer_frame, text = "Calendar")
calendar_button.pack(side = "left")

medications_button = ctk.CTkButton(footer_frame, text = "Medications")
medications_button.pack(side = "left")

notifications_button = ctk.CTkButton(footer_frame, text = "Notifications")
notifications_button.pack(side = "left")

root.mainloop()
