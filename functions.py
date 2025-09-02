from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import pages

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("custom_theme.json")

#Function to create an approximate Tkinter LabelFrame in CTkinter. Unsuccessful.

# def custom_label_frame(parent_frame, title = str):

#     #Frame containing everything
#     overall_frame = ctk.CTkFrame(parent_frame)
#     overall_frame.pack(side = "top", fill = "x", padx = "5")
#     #Title of the label frame
#     overall_frame_label = ctk.CTkLabel(overall_frame, text = title)
#     overall_frame_label.pack(side = "top", padx = "5", anchor = "w")
#     #The specific frame to contain the content that the label frame is containing
#     body_frame = ctk.CTkFrame(overall_frame)
#     body_frame.pack(side = "top", fill = "x", padx = "5")
    
#     #Space for any content to be placed in the label frame
#     info_box(body_frame, "time to", "get a watch")



def info_box(parent_frame, title = str, content = str):
    """Creates a box of information that can be used for items in a list.

    Args:
        parent_frame (parent): The frame that the box will be placed in.
        title (string, optional): The text that will be displayed as the title of the box. Defaults to str.
        content (string, optional): The text that is held within the box. Defaults to str.
    """
    #Creating the box
    box = ctk.CTkFrame(parent_frame, fg_color = "#DD3E3E")
    box.pack(side = "top", fill = "x", pady = "10", padx = "10")

    #Creating the box content
    box_title = ctk.CTkLabel(box, fg_color = "#DD3E3E", text_color = "#EFEFEF", text = title, font = ("Hammersmith One", 16))
    box_title.pack(side = "top", anchor = "w", padx = "15", pady = "5")
    box_title_content_division = ctk.CTkFrame(box)
    box_title_content_division.pack(side = "top", anchor = "w", padx = "5", pady = "5", fill = "x")
    box_content = ctk.CTkTextbox(box_title_content_division, height = 50, width = 400, wrap = "word")
    box_content.insert("0.0", content)
    box_content.pack(side = "top", anchor = "w")


def footer_button(parent_frame, command_function, title = str):
    """Creates the footer buttons in a consistent style.

    Args:
        parent_frame (parent): The frame that the button will be placed in.
        command_function (_type_): The function for the button to execute upon being pressed.
        title (string, optional): The text that will be displayed on the button. Defaults to str.
    """
    button = ctk.CTkButton(parent_frame, text = title, command = command_function, width = 50)
    button.pack(side = "left", padx = 3)


def footer(parent_frame):
    """The toolbar which holds the buttons that allow the user to open other pages of the application.

    Args:
        parent_frame (parent): The frame that the footer will be placed in.
    """
    footer_frame = ctk.CTkFrame(parent_frame)
    footer_frame.pack(side = "bottom", pady = (20, 0))

    footer_button(footer_frame, pages.med_list_page, "Medications")

    footer_button(footer_frame, pages.notification_page, "Notifications")
    
    
def input_box(parent_frame, title = str, placeholder = str):
    """Creates a titled box that the user can input information into.

    Args:
        parent_frame (parent): The frame that the box will be placed in.
        title (string): The text that will be displayed as the title of the box. Defaults to str.
        placeholder (string): The default text within the entry field. Defaults to str.
    """
    input_box_frame = ctk.CTkFrame(parent_frame)
    input_box_frame.pack(side = "top")
    input_box_title = ctk.label = ctk.CTkLabel(input_box_frame, text=title)
    input_box_title.pack(side = "top")
    input_field = ctk.entry = ctk.CTkEntry(input_box_frame, placeholder_text=placeholder, width=140, height=20)
    input_field.pack(side = "top")
    
