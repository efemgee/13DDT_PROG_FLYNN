from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func


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
current_timeslot_frame = ctk.CTkFrame(notifications_body)
current_timeslot_frame.pack(side = "top", fill = "x", padx = "5")

current_timeslot_title = ctk.CTkLabel(current_timeslot_frame, text = "Current Medication(s)")
current_timeslot_title.pack(side = "top", fill = "x", padx = "5", anchor = "w")

current_timeslot = ctk.CTkFrame(current_timeslot_frame)
current_timeslot.pack(side = "top", fill = "x", pady = "30")

current_timeslot_time = ctk.CTkLabel(current_timeslot, text = "9:30am")
current_timeslot_time.pack(side = "top", anchor = "w")

current_timeslot_content = ctk.CTkLabel(current_timeslot, text = "- 2 x ISOTRETINOIN. Take with food and water.")
current_timeslot_content.pack(side = "top", anchor = "w")

#UPDATES
update_items = LabelFrame(notifications_body, text = "Updates")
update_items.pack(side = "top", fill = "x", padx = "5")

func.info_box(update_items, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

func.info_box(update_items, "Prescription", "- Your ADDERALL prescription can now be renewed.")


#FOOTER
func.footer(master_frame)

root.mainloop()
