from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functions as func





def info_box(parent_frame, title = str, content = str):
    """Creates a box of information that can be used for items in a list.

    Args:
        parent_frame (parent): The frame that the box will be placed in.
        title (string, optional): The text that will be displayed as the title of the box. Defaults to str.
        content (string, optional): The text that is held within the box. Defaults to str.
    """
    box = ctk.CTkFrame(parent_frame)
    box.pack(side = "top", fill = "x", pady = "10", padx = "10")

    box_title = ctk.CTkLabel(box, text = title, font = ("Arial", 16))
    box_title.pack(side = "top", anchor = "w", padx = "15", pady = "5")
    box_title_content_division = ctk.CTkFrame(box)
    box_title_content_division.pack(side = "top", anchor = "w", padx = "5", pady = "5", fill = "x")
    box_content = ctk.CTkTextbox(box_title_content_division, height = 50, width = 400, wrap = "word")
    box_content.insert("0.0", content)
    box_content.pack(side = "top", anchor = "w")




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

info_box(update_items_content_frame, "Prescription", "- Your ISOTRETINOIN prescription can now be renewed.")

info_box(update_items_content_frame, "Prescription", "- Your ADDERALL prescription can now be renewed.")


#UPDATE THIS WITH MANUAL TITLE AND FRAME!!!!!!!!
schedule_timeslots_frame = ctk.CTkFrame(schedule_body)
schedule_timeslots_frame.pack(side = "top", fill = "x", padx = "10", pady = "10")

schedule_timeslots_title = ctk.CTkLabel(schedule_timeslots_frame, text = "Schedule")
schedule_timeslots_title.pack(side = "top", padx = "5", anchor = "w")

schedule_timeslots_content_frame = ctk.CTkScrollableFrame(schedule_timeslots_frame, width = 400)
schedule_timeslots_content_frame.pack(side = "top")

info_box(schedule_timeslots_content_frame, "9:30 am", "- 2 x ISOTRETINOIN. Take with food and water.")


root.mainloop()