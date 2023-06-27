from app_settings import *
from front_end import *


if __name__=='__main__':
    # Calling the ancestor
    root.geometry('500x500')
    root.resizable(0, 0)
    parent_frame()
    child_frame()
    root.mainloop()
