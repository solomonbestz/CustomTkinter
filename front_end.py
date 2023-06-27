from app_settings import *
from back_end import *


def parent_frame():
    global mummy_frame
    daddy_frame = ctk.CTkFrame(master=root, fg_color='white', width=400, height=400)
    mummy_frame = ctk.CTkFrame(master=root, fg_color='orange', width=400, height=400)
    daddy_frame.pack(pady=10)
    mummy_frame.pack(pady=10)



def child_frame():
    butt = ctk.CTkButton(master=mummy_frame, command=click)
    butt.pack()