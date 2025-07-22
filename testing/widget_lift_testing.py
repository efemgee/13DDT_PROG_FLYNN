from tkinter import *
from tkinter import ttk
import customtkinter as ctk

def notif1_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x200")

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

   
    
    notif2_btn = ctk.CTkButton(root, text="Notif 2", command = notif2_page)
    notif2_btn.pack()
    close_btn = ctk.CTkButton(root, text="Close", command = root.destroy)
    close_btn.pack()
   

    root.mainloop()

def notif2_page():
    root = ctk.CTk()

    root.title("CapsU")
    root.geometry("400x200")

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



    notif1_btn = ctk.CTkButton(root, text="Notif 1", command = notif1_page)
    notif1_btn.pack()
    close_btn = ctk.CTkButton(root, text="Close", command = root.destroy)
    close_btn.pack()
   

    root.mainloop()
    

notif1_page()