from tkinter import *
from tkinter import ttk
import customtkinter as ctk


#Function to create a box of information that can be used many times throughout the program for notifications, schedules, and medication lists
def info_box(parent_frame, title = str, content = str):
    box = ctk.CTkFrame(parent_frame)
    box.pack(side = "top", fill = "x", pady = "30", padx = "10")

    box_title = ctk.CTkLabel(box, text = title, font = ("Arial", 18))
    box_title.pack(side = "top", anchor = "w", padx = "15", pady = "5")
    box_title_content_division = ctk.CTkFrame(box)
    box_title_content_division.pack(side = "top", anchor = "w", padx = "5", pady = "5", fill = "x")
    box_content = ctk.CTkLabel(box_title_content_division, text = content)
    box_content.pack(side = "top", anchor = "w", padx = "10")



root = ctk.CTk()

root.title("CapsU")
root.geometry("400x600")

master_frame = ctk.CTkFrame(root)
master_frame.pack(fill = "x", expand = "True")

info_box(master_frame, "Prescription", "- Your ISORETINOIN prescription is ready to be renewed.")

root.mainloop()
