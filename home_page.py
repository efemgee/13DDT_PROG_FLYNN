from tkinter import *
from tkinter import ttk

from pyfonts import load_google_font

font = load_google_font("Hammersmith One")



root = Tk()

root.title("CapsU")
root.geometry("370x630")
root.configure(bg = "#17139C")

master_frame = Frame(root)
master_frame.pack(fill = "x", )

app_name_header = Label(master_frame, text = "CapsU", font = ("Hammersmith One", "50"), bg = "#17139C", fg = "#EFEFEF", pady = "20")
app_name_header.pack(side = "top")

home_page_toolbar = Label(master_frame)
home_page_toolbar.pack(side = "top")

schedule_frame = Frame(master_frame, background = "#DD3E3E")
schedule_frame.pack(side = "top")

#schedule_header = 


root.mainloop()
