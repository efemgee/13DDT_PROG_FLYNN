from tkinter import *
from tkinter import ttk
import customtkinter as ctk


#Function to create a box of information that can be used many times throughout the program for notifications, schedules, and medication lists
def info_box(parent_frame, title = str, content = str):
    box = ctk.CTkFrame(parent_frame)
    box.pack(side = "top", fill = "x", pady = "10", padx = "10")

    box_title = ctk.CTkLabel(box, text = title, font = ("Arial", 18))
    box_title.pack(side = "top", anchor = "w", padx = "15", pady = "5")
    box_title_content_division = ctk.CTkFrame(box)
    box_title_content_division.pack(side = "top", anchor = "w", padx = "5", pady = "5", fill = "x")
    box_content = ctk.CTkLabel(box_title_content_division, text = content)
    box_content.pack(side = "top", anchor = "w", padx = "10")

def footer_button(parent_frame, title = str):
    button = ctk.CTkButton(parent_frame, text = title, width = 50)
    button.pack(side = "left", padx = 3)

def footer(parent_frame):
    footer_frame = ctk.CTkFrame(parent_frame)
    footer_frame.pack(side = "bottom", pady = (20, 0))

    footer_button(footer_frame, "Home")

    footer_button(footer_frame, "Calendar")

    footer_button(footer_frame, "Medications")

    footer_button(footer_frame, "Notifications")