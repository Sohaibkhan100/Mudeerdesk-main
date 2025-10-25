# import json
# import os
# import platform
# import tkinter as tk
# import threading
# import time
# from tkinter import messagebox
# from PIL import Image, ImageGrab
# from io import BytesIO
# from pynput.mouse import Listener
# from cryptography.fernet import Fernet





# # Set TK_SILENCE_DEPRECATION to suppress the warning
# os.environ["TK_SILENCE_DEPRECATION"] = "1"
# state_file = "program.json"
# system_platform = platform.system()


# class Timer:
#     recursion = False
#     activity_recursion = False
#     isclicked = "false"
#     imagepath = ""
#     bearer_token = ""
#     User_id = ""
#     CurrentTime = ""
#     CurrentTab = ""
#     ispressed = "false"
#     image_bytes=""
#     employeeStatus = 0

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Mudeer")
#         window_width = 600
#         window_height = 300
#         x_position = (root.winfo_screenwidth() - window_width) // 2
#         y_position = (root.winfo_screenheight() - window_height) // 2
#         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

#         self.time = 0
#         self.running = False
#         self.abs_start_time = time.time()  # Absolute start time of the timer
#         self.elapsed_time = 0
#         self.is_tracking = False
#         self.tracking_thread = None
#         self.pause_tracking = False  # Flag to indicate tracking should pause
#         self.clickArray = []

#         rootFrame = tk.Frame(root, pady=10, padx=10)
#         rootFrame.pack(expand=True)

#         lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
#         lblTitle.pack(pady=(0, 10))

#         MainFrame = tk.Frame(root, pady=10, padx=10)
#         MainFrame.pack(expand=True)

#         MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
#         MainFrameTop.pack()

#         MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
#         MainFrameDown.pack()

#         self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
#         self.lblTimer.pack(pady=10)

#         self.btnStart = tk.Button(
#             MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
#             command=self.start_timer
#         )
#         self.btnStart.pack(side=tk.LEFT, padx=10)

#         self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
#                                  command=self.stop_timer)
#         self.btnStop.pack(side=tk.LEFT, padx=10)

#         self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
#                                  command=self.end_shift)
#         self.btnStop.pack(side=tk.LEFT, padx=10)

#         self.load_state()  # Load saved state when initializing]

#         # self.pusing_eventActivity()
#         self.posting_clicks()

#         self.update_timer()

#     def start_timer(self):
#         if not self.running:
#             self.running = True
#             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
#             self.pause_tracking = False  # Resume tracking if paused

#             Timer.recursion = True
#             Timer.activity_recursion = True
#             self.activity()
#             self.take_screenshot()
#             self.start_tracking()

#     def pusing_eventActivity(self):
#         from api_services import event_activity
#         # print(self.running)
#         if self.running:
#             print("event Activity Pushed")
            
#             print(Timer.isclicked)      
#             print(Timer.ispressed)
#             print(Timer.employeeStatus)
#             print(Timer.CurrentTab)
#             print(round(self.elapsed_time))
#             print(Timer.User_id)
#             print(Timer.bearer_token)
      
#             event_activity(mouseclick=Timer.isclicked,
#                            keystroke=Timer.ispressed,
#                            employeeStatus=Timer.employeeStatus,
#                            activeTab=Timer.CurrentTab,
#                            hoursPassed=round(self.elapsed_time),
#                            shiftstatus="working",
#                            user_id=Timer.User_id,
#                            bearer_token=Timer.bearer_token,)

#         print("event Activity not pushed")
#         self.root.after(17000, self.pusing_eventActivity)

#     def posting_clicks(self):
#         from api_services import post_clicks

#         print(self.running)
#         if self.running:
#             print("Clicks Posted")
#             post_clicks(
#                 imagepath=Timer.image_bytes,
#                 activeTab=Timer.CurrentTab,
#                 shiftStatus="working",
#                 user_id=Timer.User_id)
#             # print(Timer.image_bytes)
#             print(Timer.CurrentTab)
#             print(Timer.User_id)

#         print("Clicks not Posted")
#         self.root.after(10000, self.posting_clicks)

#     def stop_timer(self):
#         if self.running:
#             self.running = False
#             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
#             # self.save_state()
#             if self.is_tracking:
#                 self.pause_tracking = True  # Pause tracking
#                 Timer.recursion = False
#                 Timer.activity_recursion = False

#     def end_shift(self):
#         from helper_functions import encrypt_data, set_permissions ,fernet_key
#         from api_services import checkout
#         self.stop_timer()
#         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
#         if confirmation:
#             messagebox.showinfo("Shift Ended", "Shift has ended.")
#             state = {
#                 "elapsed_time": 0,
#                 "abs_start_time": 0,
#                 "running": False
#             }
#             with open(state_file, "wb") as f:
#                 f.write(encrypt_data(json.dumps(state), fernet_key))
#             set_permissions(state_file)  # Set file permissions after writing
#             checkout(Timer.User_id);
#             print("State saved.")
#         else:
#             self.start_timer()

#     def start_tracking(self):
#         if not self.is_tracking:
#             self.tracking_thread = threading.Thread(target=self.track_mouse)
#             self.tracking_thread.daemon = True
#             self.tracking_thread.start()
#             self.is_tracking = True

#     def track_mouse(self):
#         with Listener(on_click=self.on_click) as listener:
#             listener.join()

#     def on_click(self, x, y, button, pressed):
#         if not self.pause_tracking:
#             if pressed:
#                 Timer.isclicked = "true"
#                 Timer.employeeStatus = 1

#     def activity(self):
#         from helper_functions import ActiveTabs

#         ActiveTabs()
#         if self.activity_recursion and self.running:
#             self.root.after(15000, self.activity)

#     def take_screenshot(self):
#         from helper_functions import ActiveTabs

#         if Timer.recursion and self.running:
#             ActiveTabs()
#             try:
#                 screenshot = ImageGrab.grab()

#                 # Convert image to RGB if it has an alpha channel
#                 if screenshot.mode == 'RGBA':
#                     screenshot = screenshot.convert('RGB')

#                 image_stream = BytesIO()
#                 # Save as JPEG with quality setting
#                 screenshot.save(image_stream, format='JPEG', quality=5)
#                 Timer.image_bytes = image_stream.getvalue()

#                 # Print the size of the image in bytes
#                 image_size = len(Timer.image_bytes)
#                 # print(f"Size of the image: {image_size} bytes")

#                 self.root.after(175000, self.take_screenshot)
#             except Exception as e:
#                 print(f"Error taking screenshot: {e}")
#                 self.root.after(175000, self.take_screenshot)

#     def save_state(self):
#         from helper_functions import encrypt_data, set_permissions ,fernet_key

#         try:
#             state = {
#                 "elapsed_time": self.elapsed_time,
#                 "abs_start_time": self.abs_start_time,
#                 "running": self.running
#                 # Add other variables you want to save
#             }
#             with open(state_file, "wb") as f:
#                 f.write(encrypt_data(json.dumps(state), fernet_key))
#             set_permissions(state_file)  # Set file permissions after writing
#             print("State saved.")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

#     def load_state(self):
#         from helper_functions import decrypt_data,fernet_key

#         try:
#             if os.path.exists(state_file):
#                 with open(state_file, "rb") as f:
#                     encrypted_state = f.read()
#                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
#                 state = json.loads(decrypted_state)
#                 self.elapsed_time = state.get("elapsed_time", 0)
#                 self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
#                 self.running = state.get("running", False)
#                 if self.running:
#                     self.pause_tracking = False  # Resume tracking if paused
#                     Timer.recursion = True
#                     Timer.activity_recursion = True
#                     self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
#                     self.activity()
#                     self.take_screenshot()
#                     self.start_tracking()

#                 print("State loaded.")
#             else:
#                 self.elapsed_time = 0
#                 self.abs_start_time = time.time()  # Default to current time if no saved state
#                 print("No previous state found.")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

#     def update_timer(self):
#         if self.running:
#             self.elapsed_time = time.time() - self.abs_start_time
#             # self.save_state()

#         minutes, seconds = divmod(int(self.elapsed_time), 60)
#         hours, minutes = divmod(minutes, 60)
#         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
#         self.lblTimer.config(text=time_str)

#         # Schedule the next update
#         self.root.after(1000, self.update_timer)





# def display_timer():
#     root = tk.Tk()
#     Timer(root)
#     root.mainloop()


# if __name__ == "__main__":
#     display_timer()


import json
import os
import platform
import tkinter as tk
import threading
import time
from tkinter import messagebox
from PIL import Image, ImageGrab
from io import BytesIO
from pynput.mouse import Listener
from cryptography.fernet import Fernet





# Set TK_SILENCE_DEPRECATION to suppress the warning
os.environ["TK_SILENCE_DEPRECATION"] = "1"
state_file = "program.json"
system_platform = platform.system()


class Timer:
    recursion = False
    activity_recursion = False
    isclicked = "false"
    imagepath = ""
    bearer_token = ""
    User_id = ""
    CurrentTime = ""
    CurrentTab = ""
    ispressed = "false"
    image_bytes=""
    employeeStatus = 0

    def __init__(self, root):
        self.root = root
        self.root.title("Mudeer")
        window_width = 600
        window_height = 300
        x_position = (root.winfo_screenwidth() - window_width) // 2
        y_position = (root.winfo_screenheight() - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

        self.time = 0
        self.running = False
        self.abs_start_time = time.time()  # Absolute start time of the timer
        self.elapsed_time = 0
        self.is_tracking = False
        self.tracking_thread = None
        self.pause_tracking = False  # Flag to indicate tracking should pause
        self.clickArray = []
        self.first_start = True  # Flag to track if it's the first start

        rootFrame = tk.Frame(root, pady=10, padx=10)
        rootFrame.pack(expand=True)

        lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
        lblTitle.pack(pady=(0, 10))

        MainFrame = tk.Frame(root, pady=10, padx=10)
        MainFrame.pack(expand=True)

        MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
        MainFrameTop.pack()

        MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
        MainFrameDown.pack()

        self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
        self.lblTimer.pack(pady=10)

        self.btnStart = tk.Button(
            MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
            command=self.start_timer
        )
        self.btnStart.pack(side=tk.LEFT, padx=10)

        self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
                                 command=self.stop_timer)
        self.btnStop.pack(side=tk.LEFT, padx=10)

        self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
                                 command=self.end_shift)
        self.btnStop.pack(side=tk.LEFT, padx=10)

        self.load_state()  # Load saved state when initializing]

        self.pusing_eventActivity()
        self.posting_clicks()

        self.update_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
            self.pause_tracking = False  # Resume tracking if paused

            # If it's not the first start (i.e., resuming from pause), call stop_break
            if not self.first_start:
                from api_services import stop_break
                stop_break(Timer.User_id)
                print("Break stopped - Resuming work")
            
            # Set first_start to False after the first start
            self.first_start = False

            Timer.recursion = True
            Timer.activity_recursion = True
            self.activity()
            self.take_screenshot()
            self.start_tracking()

    def pusing_eventActivity(self):
        from api_services import event_activity
        # print(self.running)
        if self.running:
            print("event Activity Pushed")
            
            print(Timer.isclicked)      
            print(Timer.ispressed)
            print(Timer.employeeStatus)
            print(Timer.CurrentTab)
            print(round(self.elapsed_time))
            print(Timer.User_id)
            print(Timer.bearer_token)
      
            event_activity(mouseclick=Timer.isclicked,
                           keystroke=Timer.ispressed,
                           employeeStatus=Timer.employeeStatus,
                           activeTab=Timer.CurrentTab,
                           hoursPassed=round(self.elapsed_time),
                           shiftstatus="working",
                           user_id=Timer.User_id,
                           bearer_token=Timer.bearer_token,)

        print("event Activity not pushed")
        self.root.after(17000, self.pusing_eventActivity)

    def posting_clicks(self):
        from api_services import post_clicks

        print(self.running)
        if self.running:
            print("Clicks Posted")
            post_clicks(
                imagepath=Timer.image_bytes,
                activeTab=Timer.CurrentTab,
                shiftStatus="working",
                user_id=Timer.User_id)
            # print(Timer.image_bytes)
            print(Timer.CurrentTab)
            print(Timer.User_id)

        print("Clicks not Posted")
        self.root.after(10000, self.posting_clicks)

    def stop_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
            # Call start_break when pausing
            from api_services import start_break
            start_break(Timer.User_id)
            print("Break started - Timer paused")
            
            # self.save_state()
            if self.is_tracking:
                self.pause_tracking = True  # Pause tracking
                Timer.recursion = False
                Timer.activity_recursion = False

    def end_shift(self):
        from helper_functions import encrypt_data, set_permissions ,fernet_key
        from api_services import checkout
        self.stop_timer()
        confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
        if confirmation:
            messagebox.showinfo("Shift Ended", "Shift has ended.")
            state = {
                "elapsed_time": 0,
                "abs_start_time": 0,
                "running": False
            }
            with open(state_file, "wb") as f:
                f.write(encrypt_data(json.dumps(state), fernet_key))
            set_permissions(state_file)  # Set file permissions after writing
            checkout(Timer.User_id)
            print("State saved.")
            
            # Reset first_start flag when shift ends
            self.first_start = True
        else:
            self.start_timer()

    def start_tracking(self):
        if not self.is_tracking:
            self.tracking_thread = threading.Thread(target=self.track_mouse)
            self.tracking_thread.daemon = True
            self.tracking_thread.start()
            self.is_tracking = True

    def track_mouse(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        if not self.pause_tracking:
            if pressed:
                Timer.isclicked = "true"
                Timer.employeeStatus = 1

    def activity(self):
        from helper_functions import ActiveTabs

        ActiveTabs()
        if self.activity_recursion and self.running:
            self.root.after(15000, self.activity)

    def take_screenshot(self):
        from helper_functions import ActiveTabs

        if Timer.recursion and self.running:
            ActiveTabs()
            try:
                screenshot = ImageGrab.grab()

                # Convert image to RGB if it has an alpha channel
                if screenshot.mode == 'RGBA':
                    screenshot = screenshot.convert('RGB')

                image_stream = BytesIO()
                # Save as JPEG with quality setting
                screenshot.save(image_stream, format='JPEG', quality=5)
                Timer.image_bytes = image_stream.getvalue()

                # Print the size of the image in bytes
                image_size = len(Timer.image_bytes)
                # print(f"Size of the image: {image_size} bytes")

                self.root.after(175000, self.take_screenshot)
            except Exception as e:
                print(f"Error taking screenshot: {e}")
                self.root.after(175000, self.take_screenshot)

    def save_state(self):
        from helper_functions import encrypt_data, set_permissions ,fernet_key

        try:
            state = {
                "elapsed_time": self.elapsed_time,
                "abs_start_time": self.abs_start_time,
                "running": self.running,
                "first_start": self.first_start  # Save first_start flag
                # Add other variables you want to save
            }
            with open(state_file, "wb") as f:
                f.write(encrypt_data(json.dumps(state), fernet_key))
            set_permissions(state_file)  # Set file permissions after writing
            print("State saved.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

    def load_state(self):
        from helper_functions import decrypt_data,fernet_key

        try:
            if os.path.exists(state_file):
                with open(state_file, "rb") as f:
                    encrypted_state = f.read()
                decrypted_state = decrypt_data(encrypted_state, fernet_key)
                state = json.loads(decrypted_state)
                self.elapsed_time = state.get("elapsed_time", 0)
                self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
                self.running = state.get("running", False)
                self.first_start = state.get("first_start", True)  # Load first_start flag
                
                if self.running:
                    self.pause_tracking = False  # Resume tracking if paused
                    Timer.recursion = True
                    Timer.activity_recursion = True
                    self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
                    self.activity()
                    self.take_screenshot()
                    self.start_tracking()

                print("State loaded.")
            else:
                self.elapsed_time = 0
                self.abs_start_time = time.time()  # Default to current time if no saved state
                print("No previous state found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.abs_start_time
            # self.save_state()

        minutes, seconds = divmod(int(self.elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        self.lblTimer.config(text=time_str)

        # Schedule the next update
        self.root.after(1000, self.update_timer)





def display_timer():
    root = tk.Tk()
    Timer(root)
    root.mainloop()


if __name__ == "__main__":
    display_timer()






