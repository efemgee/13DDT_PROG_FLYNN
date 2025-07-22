from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func


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
