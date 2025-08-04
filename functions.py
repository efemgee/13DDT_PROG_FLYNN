from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import pages


#Function to create an approximate Tkinter LabelFrame in CTkinter.

#MAKE FUNCTIONALITY SO THAT THIS FRAME CAN READ FROM A DATABASE THE LIST OF INFOBOXES THAT IT NEEDS TO DISPLAY WITHIN ITSELF. CURRENTLY IDK HOW TO PACK OTHER THINGS INTO THE FRAME WITHIN THIS FUNCTION.
def custom_label_frame(parent_frame, title = str):
    #Frame containing everything
    overall_frame = ctk.CTkFrame(parent_frame)
    overall_frame.pack(side = "top", fill = "x", padx = "5")
    #Title of the label frame
    overall_frame_label = ctk.CTkLabel(overall_frame, text = title)
    overall_frame_label.pack(side = "top", padx = "5", anchor = "w")
    #The specific frame to contain the content that the label frame is containing
    body_frame = ctk.CTkFrame(overall_frame)
    body_frame.pack(side = "top", fill = "x", padx = "5")
    
    #Space for any content to be placed in the label frame
    info_box(body_frame, "time to", "get a watch")


#Function to create a box of information that can be used many times throughout the program for notifications, schedules, and medication lists
def info_box(parent_frame, title = str, content = str):
    box = ctk.CTkFrame(parent_frame)
    box.pack(side = "top", fill = "x", pady = "10", padx = "10")

    box_title = ctk.CTkLabel(box, text = title, font = ("Arial", 16))
    box_title.pack(side = "top", anchor = "w", padx = "15", pady = "5")
    box_title_content_division = ctk.CTkFrame(box)
    box_title_content_division.pack(side = "top", anchor = "w", padx = "5", pady = "5", fill = "x")
    box_content = ctk.CTkTextbox(box_title_content_division, height = 50, width = 400, wrap = "word")
    box_content.insert("0.0", content)
    box_content.pack(side = "top", anchor = "w")

def footer_button(parent_frame, command_function, title = str):
    button = ctk.CTkButton(parent_frame, text = title, command = command_function, width = 50)
    button.pack(side = "left", padx = 3)

def footer(parent_frame):
    footer_frame = ctk.CTkFrame(parent_frame)
    footer_frame.pack(side = "bottom", pady = (20, 0))

    #footer_button(footer_frame, "Home")

    #footer_button(footer_frame, "Calendar")

    footer_button(footer_frame, pages.med_list_page, "Medications")

    footer_button(footer_frame, pages.notification_page, "Notifications")
    
    
def input_box(parent, title, placeholder):
    input_box_frame = ctk.CTkFrame(parent)
    input_box_frame.pack(side = "top")
    input_box_title = ctk.label = ctk.CTkLabel(input_box_frame, text=title)
    input_box_title.pack(side = "top")
    input_field = ctk.entry = ctk.CTkEntry(input_box_frame, placeholder_text=placeholder, width=140, height=20)
    input_field.pack(side = "top")

