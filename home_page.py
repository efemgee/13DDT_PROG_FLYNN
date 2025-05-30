from tkinter import *
from tkinter import ttk


root = Tk()

root.title("CapsU")
root.geometry("400x600")

master_frame = Frame(root)
master_frame.pack(fill = "x", expand = "True")

app_name_header = Label(master_frame, text = "CapsU", font = ("Arial", "50"), pady = "15")
app_name_header.pack(side = "top")

home_page_toolbar = Frame(master_frame)
home_page_toolbar.pack(side = "top", fill = "x", padx = "30")

clock = Label(home_page_toolbar, text = "12:30pm")
clock.pack(side = "left")

home_page_toolbar_buttons = Frame(home_page_toolbar)
home_page_toolbar_buttons.pack(side = "right")

profile_switch_button = Button(home_page_toolbar, text = "Profiles")
profile_switch_button.pack(side = "right")

settings_button = Button(home_page_toolbar, text = "Settings")
settings_button.pack(side = "right")

schedule_frame = Frame(master_frame)
schedule_frame.pack(side = "top")

schedule_header = Frame(schedule_frame)
schedule_header.pack(side = "top")

schedule_header_title = Label(schedule_header, text = "Today", font = ("Arial", "20"))
schedule_header_title.pack(side = "left", anchor = "w")

schedule_header_calendar_button = Button(schedule_header, text = "Today on the Calendar")
schedule_header_calendar_button.pack(side = "left", padx = ("150", "0"))

schedule_body = Frame(schedule_frame)
schedule_body.pack(side = "top")

update_items = LabelFrame(schedule_body, text = "Updates")
update_items.pack(side = "top", fill = "x", padx = "5")

update1 = Frame(update_items)
update1.pack(side = "top", fill = "x", pady = "30")

update1_title = Label(update1, text = "Prescription")
update1_title.pack(side = "top", anchor = "w")

update1_content = Label(update1, text = "- Your ISOTRETINOIN prescription can now be renewed.")
update1_content.pack(side = "top", anchor = "w")

update2 = Frame(update_items)
update2.pack(side = "top", fill = "x", pady = "30")

update2_title = Label(update1, text = "Prescription")
update2_title.pack(side = "top", anchor = "w")

update2_content = Label(update1, text = "- Your ADDERALL prescription can now be renewed.")
update2_content.pack(side = "top", anchor = "w")

schedule_timeslots = LabelFrame(schedule_body, text = "Schedule")
schedule_timeslots.pack(side = "top", fill = "x", padx = "5")

timeslot1 = Frame(schedule_timeslots)
timeslot1.pack(side = "top", fill = "x", pady = "30")

timeslot1_title = Label(timeslot1, text = "9:30am")
timeslot1_title.pack(side = "top", anchor = "w")

timeslot1_content = Label(timeslot1, text = "- 2 x ISOTRETINOIN. Take with food and water.")
timeslot1_content.pack(side = "top", anchor = "w")


footer_frame = Frame(master_frame)
footer_frame.pack(side = "bottom", pady = ("20", "0"))

home_button = Button(footer_frame, text = "Home")
home_button.pack(side = "left")

calendar_button = Button(footer_frame, text = "Calendar")
calendar_button.pack(side = "left")

medications_button = Button(footer_frame, text = "Medications")
medications_button.pack(side = "left")

notifications_button = Button(footer_frame, text = "Notifications")
notifications_button.pack(side = "left")

root.mainloop()
