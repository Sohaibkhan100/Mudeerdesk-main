
# from tkinter import messagebox, ttk
# import tkinter

# import requests
# from logger import stop_logging_thread

# from timer_screen import Timer


# class LoginApp:
#     def __init__(self, root):
#         self.root = root
#         self.setup_ui()

#     def setup_ui(self):
#         self.root.title("Mudeer")
        

#         # Calculate the center position
#         window_width = 600
#         window_height = 300
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         x_position = (screen_width - window_width) // 2
#         y_position = (screen_height - window_height) // 2

#         # Set window size and position
#         self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

#         # Create a frame for better organization
#         frame = ttk.Frame(self.root, padding="20")
#         frame.pack(expand=True)

#         # Add a heading
#         heading_label = ttk.Label(frame, text="Login", font=("Helvetica", 16, "bold"))
#         heading_label.grid(row=0, columnspan=2, pady=10)

#         # Create email label and entry field
#         self.email_label = ttk.Label(frame, text="Email:")
#         self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
#         self.email_entry = ttk.Entry(frame)
#         self.email_entry.grid(row=1, column=1, padx=10, pady=5)

#         # Create password label and entry field
#         self.password_label = ttk.Label(frame, text="Password:")
#         self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
#         self.password_entry = ttk.Entry(frame, show="*")
#         self.password_entry.grid(row=2, column=1, padx=10, pady=5)

#         # Create a sign-in button
#         login_button = ttk.Button(frame, text="Sign In", command=self.validate_login)
#         login_button.grid(row=3, columnspan=2, pady=10)

#         # Center the frame
#         frame.columnconfigure(0, weight=1)
#         frame.columnconfigure(1, weight=1)
#         frame.rowconfigure(1, weight=1)
#         frame.rowconfigure(2, weight=1)
 



#     def login(self):
#         email = self.email_entry.get()
#         password = self.password_entry.get()

#         api_url = "https://mudeerapi.abasa.com/user/login"
#         data = {
#             "email": email,
#             "password": password
#         }

#         try:
#             response = requests.post(api_url, json=data)
#             # response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             messagebox.showerror("Error", f"Login failed. {str(e)}")
#             return

      

#         if response.status_code == 200:
#             response_data = response.json()
#             Timer.bearer_token = response_data['token']
#             Timer.User_id = response_data['_id']
#             self.MarkAttendance(
#                 user_id = response_data['_id'],
#                 name = response_data['first_name'],
#                 department = response_data['department'],
#                 status = " ",
#                 appversion="v2",
                
#             )
#             messagebox.showinfo("Success", "Login successful!")
#             self.root.destroy()
#             self.create_timer_window()
#         else:
#             response_data = response.json()
#             messagebox.showerror("Error",response_data["messge"] )

#     def MarkAttendance(self, user_id, name, status, department, appversion):
        
#         api_url = "https://mudeerapi.abasa.com/user/attendance"
        
#         data = {
#                "user_id":user_id,
#                "name":name,
#                "attendanceStatus":status,
#                "department":department,
#                "app_version":appversion,
#                "createdAt":""
 
            
#         }
#         try:
#             headers = {
#                 "Authorization": f"Bearer {Timer.bearer_token}",
#             }
#             response = requests.post(api_url, json=data, headers=headers)
#             # response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
#             return

#         if response.status_code == 200:
#             response_data = response.json()
#             print(response_data['message'])
#         else:
#             print("Failed to mark attendance")
#             print(response.status_code)
        
#     def create_timer_window(self):
#         root2 = tkinter.Tk()
#         # root2.wm_attributes('-toolwindow', 'True')
#         # if sys.platform.startswith('win'):
#         #     root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        
#         # root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
#         root2.title("Timer")
#         root2.geometry("1100x500+100+100")

#         # Create the Timer instance and start the main loop
#         timer = Timer(root2)
#         root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
#         root2.mainloop()

#     def on_closing(self, window):
#         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
#             stop_logging_thread()
#             window.destroy()


        

#     def validate_login(self):
#         email = self.email_entry.get()
#         password = self.password_entry.get()

#         if email == "" or password == "":
#             messagebox.showerror("Error", "Please fill in both email and password fields.")
#         else:
#             self.login()

#     def on_Login_closing(root):
#         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
#             stop_logging_thread()
#             root.destroy()
from tkinter import messagebox, ttk
import tkinter

from key_logger import stop_logging_thread

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Mudeer")

        # Calculate the center position
        window_width = 600
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set window size and position
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame for better organization
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        # Add a heading
        heading_label = ttk.Label(frame, text="Login", font=("Helvetica", 16, "bold"))
        heading_label.grid(row=0, columnspan=2, pady=10)

        # Create email label and entry field
        self.email_label = ttk.Label(frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(frame)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create password label and entry field
        self.password_label = ttk.Label(frame, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create a sign-in button
        login_button = ttk.Button(frame, text="Sign In", command=self.validate_login)
        login_button.grid(row=3, columnspan=2, pady=10)

        # Center the frame
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

    def validate_login(self):
        from api_services import login
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "Please fill in both email and password fields.")
        else:
            response_data = login(email, password)
            if response_data:
                self.root.destroy()
                self.create_timer_window()

    def create_timer_window(self):
        from timer_screen import Timer
        root2 = tkinter.Tk()
        # root2.wm_attributes('-toolwindow', 'True')
        # if sys.platform.startswith('win'):
        #     root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        
        # root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        root2.title("Timer")
        root2.geometry("1100x500+100+100")

        # Create the Timer instance and start the main loop
        timer = Timer(root2)
        root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
        root2.mainloop()

    def on_closing(self, window):
        from key_logger import stop_logging_thread
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            stop_logging_thread()
            window.destroy()
            
            
    def on_Login_closing(root):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            stop_logging_thread()
            root.destroy()
            
            
if __name__ == "__main__":
    root = tkinter.Tk()
    app = LoginApp(root)
    root.mainloop()
