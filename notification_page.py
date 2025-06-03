from tkinter import *
from tkinter import ttk
import customtkinter as ctk


root = ctk.CTk()

root.title("CapsU")
root.geometry("400x600")

master_frame = ctk.CTkFrame(root)
master_frame.pack(fill = "both")


#HEADER
notifications_frame = ctk.CTkFrame(master_frame)
notifications_frame.pack(side = "top")

schedule_header = ctk.CTkFrame(notifications_frame)
schedule_header.pack(side = "top")


#NOTIFICATIONS BODY
notifications_header_title = ctk.CTkLabel(schedule_header, text = "Notifications", font = ("Arial", 20))
notifications_header_title.pack(side = "left", anchor = "w", fill = "x", expand = "True", pady = "15")

notifications_body = ctk.CTkFrame(notifications_frame)
notifications_body.pack(side = "top")

#CURRENT MEDICATION TIMESLOT
current_timeslot_frame = LabelFrame(notifications_body, text = "Current Medication(s)")
current_timeslot_frame.pack(side = "top", fill = "x", padx = "5")

current_timeslot = ctk.CTkFrame(current_timeslot_frame)
current_timeslot.pack(side = "top", fill = "x", pady = "30")

current_timeslot_time = ctk.CTkLabel(current_timeslot, text = "9:30am")
current_timeslot_time.pack(side = "top", anchor = "w")

current_timeslot_content = ctk.CTkLabel(current_timeslot, text = "- 2 x ISOTRETINOIN. Take with food and water.")
current_timeslot_content.pack(side = "top", anchor = "w")

#UPDATES
update_items = LabelFrame(notifications_body, text = "Updates")
update_items.pack(side = "top", fill = "x", padx = "5")

update1 = ctk.CTkFrame(update_items)
update1.pack(side = "top", fill = "x", pady = "15")

update1_title = ctk.CTkLabel(update1, text = "Prescription")
update1_title.pack(side = "top", anchor = "w")

update1_content = ctk.CTkLabel(update1, text = "- Your ISOTRETINOIN prescription can now be renewed.")
update1_content.pack(side = "top", anchor = "w")

update2 = ctk.CTkFrame(update_items)
update2.pack(side = "top", fill = "x", pady = "15")

update2_title = ctk.CTkLabel(update1, text = "Prescription")
update2_title.pack(side = "top", anchor = "w")

update2_content = ctk.CTkLabel(update1, text = "- Your ADDERALL prescription can now be renewed.")
update2_content.pack(side = "top", anchor = "w")


#FOOTER
footer_frame = ctk.CTkFrame(master_frame)
footer_frame.pack(side = "bottom", pady = (20, 0))

home_button = ctk.CTkButton(footer_frame, text = "Home")
home_button.pack(side = "left")

calendar_button = ctk.CTkButton(footer_frame, text = "Calendar")
calendar_button.pack(side = "left")

medications_button = ctk.CTkButton(footer_frame, text = "Medications")
medications_button.pack(side = "left")

notifications_button = ctk.CTkButton(footer_frame, text = "Notifications")
notifications_button.pack(side = "left")

root.mainloop()
