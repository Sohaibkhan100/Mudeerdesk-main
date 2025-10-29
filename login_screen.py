
# # # # # from tkinter import messagebox, ttk
# # # # # import tkinter

# # # # # from key_logger import stop_logging_thread

# # # # # class LoginApp:
# # # # #     def __init__(self, root):
# # # # #         self.root = root
# # # # #         self.setup_ui()

# # # # #     def setup_ui(self):
# # # # #         self.root.title("Mudeer")

# # # # #         # Calculate the center position
# # # # #         window_width = 600
# # # # #         window_height = 300
# # # # #         screen_width = self.root.winfo_screenwidth()
# # # # #         screen_height = self.root.winfo_screenheight()
# # # # #         x_position = (screen_width - window_width) // 2
# # # # #         y_position = (screen_height - window_height) // 2

# # # # #         # Set window size and position
# # # # #         self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# # # # #         # Create a frame for better organization
# # # # #         frame = ttk.Frame(self.root, padding="20")
# # # # #         frame.pack(expand=True)

# # # # #         # Add a heading
# # # # #         heading_label = ttk.Label(frame, text="Login", font=("Helvetica", 16, "bold"))
# # # # #         heading_label.grid(row=0, columnspan=2, pady=10)

# # # # #         # Create email label and entry field
# # # # #         self.email_label = ttk.Label(frame, text="Email:")
# # # # #         self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
# # # # #         self.email_entry = ttk.Entry(frame)
# # # # #         self.email_entry.grid(row=1, column=1, padx=10, pady=5)

# # # # #         # Create password label and entry field
# # # # #         self.password_label = ttk.Label(frame, text="Password:")
# # # # #         self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
# # # # #         self.password_entry = ttk.Entry(frame, show="*")
# # # # #         self.password_entry.grid(row=2, column=1, padx=10, pady=5)

# # # # #         # Create a sign-in button
# # # # #         login_button = ttk.Button(frame, text="Sign In", command=self.validate_login)
# # # # #         login_button.grid(row=3, columnspan=2, pady=10)

# # # # #         # Center the frame
# # # # #         frame.columnconfigure(0, weight=1)
# # # # #         frame.columnconfigure(1, weight=1)
# # # # #         frame.rowconfigure(1, weight=1)
# # # # #         frame.rowconfigure(2, weight=1)

# # # # #     def validate_login(self):
# # # # #         from api_services import login
# # # # #         email = self.email_entry.get()
# # # # #         password = self.password_entry.get()

# # # # #         if email == "" or password == "":
# # # # #             messagebox.showerror("Error", "Please fill in both email and password fields.")
# # # # #         else:
# # # # #             response_data = login(email, password)
# # # # #             if response_data:
# # # # #                 self.root.destroy()
# # # # #                 self.create_timer_window()

# # # # #     def create_timer_window(self):
# # # # #         from timer_screen import Timer
# # # # #         root2 = tkinter.Tk()
# # # # #         # root2.wm_attributes('-toolwindow', 'True')
# # # # #         # if sys.platform.startswith('win'):
# # # # #         #     root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        
# # # # #         # root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
# # # # #         root2.title("Timer")
# # # # #         root2.geometry("1100x500+100+100")

# # # # #         # Create the Timer instance and start the main loop
# # # # #         timer = Timer(root2)
# # # # #         root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
# # # # #         root2.mainloop()

# # # # #     def on_closing(self, window):
# # # # #         from key_logger import stop_logging_thread
# # # # #         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
# # # # #             stop_logging_thread()
# # # # #             window.destroy()
            
            
# # # # #     def on_Login_closing(root):
# # # # #         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
# # # # #             stop_logging_thread()
# # # # #             root.destroy()
            
            
# # # # # if __name__ == "__main__":
# # # # #     root = tkinter.Tk()
# # # # #     app = LoginApp(root)
# # # # #     root.mainloop()


# # # # from tkinter import messagebox, ttk
# # # # import tkinter

# # # # from key_logger import stop_logging_thread

# # # # class LoginApp:
# # # #     def __init__(self, root):
# # # #         self.root = root
# # # #         self.setup_ui()

# # # #     def setup_ui(self):
# # # #         self.root.title("Mudeer")

# # # #         # Calculate the center position
# # # #         window_width = 600
# # # #         window_height = 300
# # # #         screen_width = self.root.winfo_screenwidth()
# # # #         screen_height = self.root.winfo_screenheight()
# # # #         x_position = (screen_width - window_width) // 2
# # # #         y_position = (screen_height - window_height) // 2

# # # #         # Set window size and position
# # # #         self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# # # #         # Create a frame for better organization
# # # #         frame = ttk.Frame(self.root, padding="20")
# # # #         frame.pack(expand=True)

# # # #         # Add a heading
# # # #         heading_label = ttk.Label(frame, text="Login", font=("Helvetica", 16, "bold"))
# # # #         heading_label.grid(row=0, columnspan=2, pady=10)

# # # #         # Create email label and entry field
# # # #         self.email_label = ttk.Label(frame, text="Email:")
# # # #         self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
# # # #         self.email_entry = ttk.Entry(frame)
# # # #         self.email_entry.grid(row=1, column=1, padx=10, pady=5)

# # # #         # Create password label and entry field
# # # #         self.password_label = ttk.Label(frame, text="Password:")
# # # #         self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
# # # #         self.password_entry = ttk.Entry(frame, show="*")
# # # #         self.password_entry.grid(row=2, column=1, padx=10, pady=5)

# # # #         # Create a sign-in button
# # # #         login_button = ttk.Button(frame, text="Sign In", command=self.validate_login)
# # # #         login_button.grid(row=3, columnspan=2, pady=10)

# # # #         # Center the frame
# # # #         frame.columnconfigure(0, weight=1)
# # # #         frame.columnconfigure(1, weight=1)
# # # #         frame.rowconfigure(1, weight=1)
# # # #         frame.rowconfigure(2, weight=1)

# # # #     def validate_login(self):
# # # #         from api_services import login
# # # #         email = self.email_entry.get()
# # # #         password = self.password_entry.get()

# # # #         if email == "" or password == "":
# # # #             messagebox.showerror("Error", "Please fill in both email and password fields.")
# # # #         else:
# # # #             response_data = login(email, password)
# # # #             if response_data:
# # # #                 self.root.destroy()
# # # #                 self.create_timer_window()

# # # #     def create_timer_window(self):
# # # #         from timer_screen import Timer
# # # #         root2 = tkinter.Tk()
# # # #         # root2.wm_attributes('-toolwindow', 'True')
# # # #         # if sys.platform.startswith('win'):
# # # #         #     root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        
# # # #         # root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
# # # #         root2.title("Timer")
# # # #         root2.geometry("1100x500+100+100")

# # # #         # Create the Timer instance and start the main loop
# # # #         timer = Timer(root2)
        
# # # #         # Store timer instance for cleanup
# # # #         root2.timer_instance = timer
        
# # # #         root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
# # # #         root2.mainloop()

# # # #     def on_closing(self, window):
# # # #         from key_logger import stop_logging_thread
# # # #         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
# # # #             # Proper cleanup before destroying
# # # #             if hasattr(window, 'timer_instance'):
# # # #                 window.timer_instance.cancel_all_tasks()
# # # #             stop_logging_thread()
# # # #             window.destroy()
            
            
# # # #     def on_Login_closing(root):
# # # #         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
# # # #             stop_logging_thread()
# # # #             root.destroy()
            
            
# # # # if __name__ == "__main__":
# # # #     root = tkinter.Tk()
# # # #     app = LoginApp(root)
# # # #     root.mainloop()

# # # from tkinter import messagebox, ttk
# # # import tkinter

# # # from key_logger import stop_logging_thread

# # # class LoginApp:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.setup_ui()

# # #     def setup_ui(self):
# # #         self.root.title("Mudeer")

# # #         # Calculate the center position
# # #         window_width = 600
# # #         window_height = 300
# # #         screen_width = self.root.winfo_screenwidth()
# # #         screen_height = self.root.winfo_screenheight()
# # #         x_position = (screen_width - window_width) // 2
# # #         y_position = (screen_height - window_height) // 2

# # #         # Set window size and position
# # #         self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# # #         # Create a frame for better organization
# # #         frame = ttk.Frame(self.root, padding="20")
# # #         frame.pack(expand=True)

# # #         # Add a heading
# # #         heading_label = ttk.Label(frame, text="Login", font=("Helvetica", 16, "bold"))
# # #         heading_label.grid(row=0, columnspan=2, pady=10)

# # #         # Create email label and entry field
# # #         self.email_label = ttk.Label(frame, text="Email:")
# # #         self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
# # #         self.email_entry = ttk.Entry(frame)
# # #         self.email_entry.grid(row=1, column=1, padx=10, pady=5)

# # #         # Create password label and entry field
# # #         self.password_label = ttk.Label(frame, text="Password:")
# # #         self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
# # #         self.password_entry = ttk.Entry(frame, show="*")
# # #         self.password_entry.grid(row=2, column=1, padx=10, pady=5)

# # #         # Create a sign-in button
# # #         login_button = ttk.Button(frame, text="Sign In", command=self.validate_login)
# # #         login_button.grid(row=3, columnspan=2, pady=10)

# # #         # Center the frame
# # #         frame.columnconfigure(0, weight=1)
# # #         frame.columnconfigure(1, weight=1)
# # #         frame.rowconfigure(1, weight=1)
# # #         frame.rowconfigure(2, weight=1)

# # #     def validate_login(self):
# # #         from api_services import login
# # #         email = self.email_entry.get()
# # #         password = self.password_entry.get()

# # #         if email == "" or password == "":
# # #             messagebox.showerror("Error", "Please fill in both email and password fields.")
# # #         else:
# # #             response_data = login(email, password)
# # #             if response_data:
# # #                 self.root.destroy()
# # #                 self.create_timer_window(response_data)

# # #     def create_timer_window(self, response_data):
# # #         from timer_screen import Timer
# # #         root2 = tkinter.Tk()
# # #         # root2.wm_attributes('-toolwindow', 'True')
# # #         # if sys.platform.startswith('win'):
# # #         #     root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        
# # #         # root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
# # #         root2.title("Timer")
# # #         root2.geometry("1100x500+100+100")

# # #         # Create the Timer instance and start the main loop
# # #         timer = Timer(root2)
        
# # #         # Set authentication credentials from login response
# # #         timer.bearer_token = response_data.get('bearer_token', '')
# # #         timer.user_id = response_data.get('user_id', '')
        
# # #         # Store timer instance for cleanup
# # #         root2.timer_instance = timer
        
# # #         root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
# # #         root2.mainloop()

# # #     def on_closing(self, window):
# # #         from key_logger import stop_logging_thread
# # #         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
# # #             # Proper cleanup before destroying
# # #             if hasattr(window, 'timer_instance'):
# # #                 window.timer_instance.cancel_all_tasks()
# # #             stop_logging_thread()
# # #             window.destroy()
            
            
# # #     def on_Login_closing(root):
# # #         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
# # #             stop_logging_thread()
# # #             root.destroy()
            
            
# # # if __name__ == "__main__":
# # #     root = tkinter.Tk()
# # #     app = LoginApp(root)
# # #     root.mainloop()

# from tkinter import messagebox, ttk
# import tkinter

# from key_logger import stop_logging_thread

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

#     def validate_login(self):
#         from api_services import login
#         email = self.email_entry.get()
#         password = self.password_entry.get()

#         if email == "" or password == "":
#             messagebox.showerror("Error", "Please fill in both email and password fields.")
#         else:
#             response_data = login(email, password)
#             if response_data:
#                 self.root.destroy()
#                 self.create_timer_window(response_data)

#     def create_timer_window(self, response_data):
#         from timer_screen import Timer
#         root2 = tkinter.Tk()
#         # root2.wm_attributes('-toolwindow', 'True')
#         # if sys.platform.startswith('win'):
#         #     root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
        
#         # root2.iconbitmap("C:\\Users\\MRC\\Desktop\\icon.ico")
#         root2.title("Timer")
#         root2.geometry("1100x500+100+100")

#         # Create the Timer instance and start the main loop
#         timer = Timer(root2)
        
#         # Set authentication credentials from login response
#         timer.bearer_token = response_data.get('bearer_token', '')
#         timer.user_id = response_data.get('user_id', '')
        
#         # Store timer instance for cleanup
#         root2.timer_instance = timer
        
#         root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
#         root2.mainloop()

#     def on_closing(self, window):
#         from key_logger import stop_logging_thread
#         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
#             # Save state before closing (emergency save)
#             if hasattr(window, 'timer_instance'):
#                 window.timer_instance.save_state()
#                 window.timer_instance.cancel_all_tasks()
#             stop_logging_thread()
#             window.destroy()
            
            
#     def on_Login_closing(root):
#         if messagebox.askokcancel("Quit", "Do you really want to quit?"):
#             stop_logging_thread()
#             root.destroy()
            
            
# if __name__ == "__main__":
#     import os
#     import json
#     from helper_functions import decrypt_data, fernet_key
    
#     # Check if there's a resumable session
#     state_file = "program.json"
#     should_skip_login = False
    
#     try:
#         if os.path.exists(state_file):
#             with open(state_file, "rb") as f:
#                 encrypted_state = f.read()
#             decrypted_state = decrypt_data(encrypted_state, fernet_key)
#             state = json.loads(decrypted_state)
            
#             # Check if we have a valid session to resume
#             saved_elapsed = state.get("elapsed_time", 0)
#             saved_token = state.get("bearer_token", "")
#             saved_user_id = state.get("user_id", "")
            
#             # If there's a session with credentials, skip login
#             if saved_elapsed > 0 and saved_token and saved_user_id:
#                 should_skip_login = True
#                 print("Found resumable session - will skip login")
#     except Exception as e:
#         print(f"Error checking state: {e}")
#         should_skip_login = False
    
#     # Start the appropriate window
#     if should_skip_login:
#         # Skip login and go directly to timer screen
#         from timer_screen import Timer
#         root = tkinter.Tk()
#         timer = Timer(root)
#         root.protocol("WM_DELETE_WINDOW", lambda: LoginApp.on_closing(LoginApp, root))
#         root.mainloop()
#     else:
#         # Show normal login screen
#         root = tkinter.Tk()
#         app = LoginApp(root)
#         root.protocol("WM_DELETE_WINDOW", lambda: LoginApp.on_Login_closing(root))
#         root.mainloop()

from tkinter import messagebox, ttk
import tkinter as tk
from PIL import Image, ImageTk
import os

from key_logger import stop_logging_thread

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Mudeer")
        
        # Refined color scheme
        bg_color = "#ffffff"
        card_color = "#ffffff"
        primary_color = "#2563eb"
        text_color = "#111827"
        label_color = "#6b7280"
        input_bg = "#f9fafb"
        border_color = "#d1d5db"
        focus_border = "#2563eb"

        
        self.root.configure(bg=bg_color)

        # Window size
        window_width = 420
        window_height = 520
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.resizable(False, False)

        # Configure ttk style
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Refined.TEntry',
                       fieldbackground=input_bg,
                       foreground=text_color,
                       bordercolor=border_color,
                       lightcolor=focus_border,
                       darkcolor=border_color,
                       borderwidth=1,
                       relief='solid',
                       padding=10)
        
        style.map('Refined.TEntry',
                 fieldbackground=[('focus', '#ffffff')],
                 bordercolor=[('focus', focus_border)],
                 lightcolor=[('focus', focus_border)])
        
        style.configure('Primary.TButton',
                       background="#234297",
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       padding=(0, 14),
                       font=('Helvetica', 12, 'bold'))
        style.map('Primary.TButton',
                 background=[('active', '#1d4ed8'), ('pressed', '#1e40af')])

        # Main container
        main_frame = tk.Frame(self.root, bg=card_color, relief=tk.FLAT)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=45, pady=40)

        # Logo/Icon - Simple version
        icon_frame = tk.Frame(main_frame, bg=card_color)
        icon_frame.pack(pady=(20, 10))
        
        try:
            # Just check if Logo.png exists in same folder
            if os.path.exists("Logo.png"):
                # Load and resize image
                logo_image = Image.open("Logo.png")
                logo_image = logo_image.resize((80, 80), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_image)
                
                icon_label = tk.Label(
                    icon_frame,
                    image=self.logo_photo,
                    bg=card_color
                )
                icon_label.pack()
                print("✅ Logo loaded!")
            else:
                # Use emoji if Logo.png not found
                icon_label = tk.Label(
                    icon_frame,
                    text="🕐",
                    font=("Helvetica", 44),
                    bg=card_color,
                    fg=text_color
                )
                icon_label.pack()
                print("ℹ️ No Logo.png found, using emoji")
                
        except Exception as e:
            # Use emoji on any error
            print(f"⚠️ Error loading logo: {e}")
            icon_label = tk.Label(
                icon_frame,
                text="🕐",
                font=("Helvetica", 44),
                bg=card_color,
                fg=text_color
            )
            icon_label.pack()


        # Email field
        email_label = tk.Label(
            main_frame,
            text="Email Address",
            font=("Helvetica", 10, "bold"),
            bg=card_color,
            fg=text_color,
            anchor="w"
        )
        email_label.pack(fill=tk.X, pady=(0, 6))
        
        self.email_entry = ttk.Entry(
            main_frame,
            font=("Helvetica", 12),
            style='Refined.TEntry'
        )
        self.email_entry.insert(0, "Enter your email")
        self.email_entry.config(foreground='#9ca3af')
        
        self.email_entry.bind('<FocusIn>', self.on_email_focus_in)
        self.email_entry.bind('<FocusOut>', self.on_email_focus_out)
        
        self.email_entry.pack(fill=tk.X, pady=(0, 18))

        # Password field
        password_label = tk.Label(
            main_frame,
            text="Password",
            font=("Helvetica", 10, "bold"),
            bg=card_color,
            fg=text_color,
            anchor="w"
        )
        password_label.pack(fill=tk.X, pady=(0, 6))
        
        self.password_entry = ttk.Entry(
            main_frame,
            font=("Helvetica", 12),
            style='Refined.TEntry'
        )
        self.password_entry.insert(0, "Enter your password")
        self.password_entry.config(foreground='#9ca3af')
        self.password_is_placeholder = True
        
        self.password_entry.bind('<FocusIn>', self.on_password_focus_in)
        self.password_entry.bind('<FocusOut>', self.on_password_focus_out)
        self.password_entry.bind("<Return>", lambda e: self.validate_login())
        
        self.password_entry.pack(fill=tk.X, pady=(0, 28))

        # Sign in button
        self.login_button = ttk.Button(
            main_frame,
            text="Sign In",
            command=self.validate_login,
            style='Primary.TButton'
        )
        self.login_button.pack(fill=tk.X, pady=(0, 12))

        # Status
        status_label = tk.Label(
            main_frame,
            text="● Online",
            font=("Helvetica", 9),
            bg=card_color,
            fg="#10b981"
        )
        status_label.pack(pady=(10, 0))

    # Placeholder management
    def on_email_focus_in(self, event):
        if self.email_entry.get() == "Enter your email":
            self.email_entry.delete(0, tk.END)
            self.email_entry.config(foreground='#111827')
    
    def on_email_focus_out(self, event):
        if self.email_entry.get() == "":
            self.email_entry.insert(0, "Enter your email")
            self.email_entry.config(foreground='#9ca3af')
    
    def on_password_focus_in(self, event):
        if self.password_is_placeholder:
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(show="•", foreground='#111827')
            self.password_is_placeholder = False
    
    def on_password_focus_out(self, event):
        if self.password_entry.get() == "":
            self.password_entry.config(show="")
            self.password_entry.insert(0, "Enter your password")
            self.password_entry.config(foreground='#9ca3af')
            self.password_is_placeholder = True

    def validate_login(self):
        from api_services import login
        
        email = self.email_entry.get()
        if email == "Enter your email":
            email = ""
        
        password = self.password_entry.get()
        if self.password_is_placeholder:
            password = ""

        if email == "" or password == "":
            messagebox.showerror("Error", "Please enter your email & password before Sign in.")
        else:
            self.login_button.config(text="Signing in...", state="disabled")
            self.root.update()
            
            response_data = login(email, password)
            if response_data:
                self.root.destroy()
                self.create_timer_window(response_data)
            else:
                self.login_button.config(text="Sign In", state="normal")

    def create_timer_window(self, response_data):
        from timer_screen import Timer
        root2 = tk.Tk()
        root2.title("Mudeer")
        root2.geometry("900x650+100+100")

        timer = Timer(root2)
        timer.bearer_token = response_data.get('bearer_token', '')
        timer.user_id = response_data.get('user_id', '')
        root2.timer_instance = timer
        
        root2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root2))
        root2.mainloop()

    def on_closing(self, window):
        from key_logger import stop_logging_thread
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            if hasattr(window, 'timer_instance'):
                window.timer_instance.save_state()
                window.timer_instance.cancel_all_tasks()
            stop_logging_thread()
            window.destroy()
            
    def on_Login_closing(root):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            stop_logging_thread()
            root.destroy()
            

if __name__ == "__main__":
    import os
    import json
    from helper_functions import decrypt_data, fernet_key
    
    state_file = "program.json"
    should_skip_login = False
    
    try:
        if os.path.exists(state_file):
            with open(state_file, "rb") as f:
                encrypted_state = f.read()
            decrypted_state = decrypt_data(encrypted_state, fernet_key)
            state = json.loads(decrypted_state)
            
            saved_elapsed = state.get("elapsed_time", 0)
            saved_token = state.get("bearer_token", "")
            saved_user_id = state.get("user_id", "")
            
            if saved_elapsed > 0 and saved_token and saved_user_id:
                should_skip_login = True
                print("Found resumable session - will skip login")
    except Exception as e:
        print(f"Error checking state: {e}")
        should_skip_login = False
    
    if should_skip_login:
        from timer_screen import Timer
        root = tk.Tk()
        timer = Timer(root)
        root.protocol("WM_DELETE_WINDOW", lambda: LoginApp.on_closing(LoginApp, root))
        root.mainloop()
    else:
        root = tk.Tk()
        app = LoginApp(root)
        root.protocol("WM_DELETE_WINDOW", lambda: LoginApp.on_Login_closing(root))
        root.mainloop()