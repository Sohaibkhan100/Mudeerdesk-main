# # # # # # import json
# # # # # # import os
# # # # # # import platform
# # # # # # import tkinter as tk
# # # # # # import threading
# # # # # # import time
# # # # # # from tkinter import messagebox
# # # # # # from PIL import Image, ImageGrab
# # # # # # from io import BytesIO
# # # # # # from pynput.mouse import Listener
# # # # # # from cryptography.fernet import Fernet





# # # # # # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # # # # # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # # # # # state_file = "program.json"
# # # # # # system_platform = platform.system()


# # # # # # class Timer:
# # # # # #     recursion = False
# # # # # #     activity_recursion = False
# # # # # #     isclicked = "false"
# # # # # #     imagepath = ""
# # # # # #     bearer_token = ""
# # # # # #     User_id = ""
# # # # # #     CurrentTime = ""
# # # # # #     CurrentTab = ""
# # # # # #     ispressed = "false"
# # # # # #     image_bytes=""
# # # # # #     employeeStatus = 0

# # # # # #     def __init__(self, root):
# # # # # #         self.root = root
# # # # # #         self.root.title("Mudeer")
# # # # # #         window_width = 600
# # # # # #         window_height = 300
# # # # # #         x_position = (root.winfo_screenwidth() - window_width) // 2
# # # # # #         y_position = (root.winfo_screenheight() - window_height) // 2
# # # # # #         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

# # # # # #         self.time = 0
# # # # # #         self.running = False
# # # # # #         self.abs_start_time = time.time()  # Absolute start time of the timer
# # # # # #         self.elapsed_time = 0
# # # # # #         self.is_tracking = False
# # # # # #         self.tracking_thread = None
# # # # # #         self.pause_tracking = False  # Flag to indicate tracking should pause
# # # # # #         self.clickArray = []

# # # # # #         rootFrame = tk.Frame(root, pady=10, padx=10)
# # # # # #         rootFrame.pack(expand=True)

# # # # # #         lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
# # # # # #         lblTitle.pack(pady=(0, 10))

# # # # # #         MainFrame = tk.Frame(root, pady=10, padx=10)
# # # # # #         MainFrame.pack(expand=True)

# # # # # #         MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
# # # # # #         MainFrameTop.pack()

# # # # # #         MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
# # # # # #         MainFrameDown.pack()

# # # # # #         self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
# # # # # #         self.lblTimer.pack(pady=10)

# # # # # #         self.btnStart = tk.Button(
# # # # # #             MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
# # # # # #             command=self.start_timer
# # # # # #         )
# # # # # #         self.btnStart.pack(side=tk.LEFT, padx=10)

# # # # # #         self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # # # # #                                  command=self.stop_timer)
# # # # # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # # # # #         self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # # # # #                                  command=self.end_shift)
# # # # # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # # # # #         self.load_state()  # Load saved state when initializing]

# # # # # #         # self.pusing_eventActivity()
# # # # # #         self.posting_clicks()

# # # # # #         self.update_timer()

# # # # # #     def start_timer(self):
# # # # # #         if not self.running:
# # # # # #             self.running = True
# # # # # #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# # # # # #             self.pause_tracking = False  # Resume tracking if paused

# # # # # #             Timer.recursion = True
# # # # # #             Timer.activity_recursion = True
# # # # # #             self.activity()
# # # # # #             self.take_screenshot()
# # # # # #             self.start_tracking()

# # # # # #     def pusing_eventActivity(self):
# # # # # #         from api_services import event_activity
# # # # # #         # print(self.running)
# # # # # #         if self.running:
# # # # # #             print("event Activity Pushed")
            
# # # # # #             print(Timer.isclicked)      
# # # # # #             print(Timer.ispressed)
# # # # # #             print(Timer.employeeStatus)
# # # # # #             print(Timer.CurrentTab)
# # # # # #             print(round(self.elapsed_time))
# # # # # #             print(Timer.User_id)
# # # # # #             print(Timer.bearer_token)
      
# # # # # #             event_activity(mouseclick=Timer.isclicked,
# # # # # #                            keystroke=Timer.ispressed,
# # # # # #                            employeeStatus=Timer.employeeStatus,
# # # # # #                            activeTab=Timer.CurrentTab,
# # # # # #                            hoursPassed=round(self.elapsed_time),
# # # # # #                            shiftstatus="working",
# # # # # #                            user_id=Timer.User_id,
# # # # # #                            bearer_token=Timer.bearer_token,)

# # # # # #         print("event Activity not pushed")
# # # # # #         self.root.after(17000, self.pusing_eventActivity)

# # # # # #     def posting_clicks(self):
# # # # # #         from api_services import post_clicks

# # # # # #         print(self.running)
# # # # # #         if self.running:
# # # # # #             print("Clicks Posted")
# # # # # #             post_clicks(
# # # # # #                 imagepath=Timer.image_bytes,
# # # # # #                 activeTab=Timer.CurrentTab,
# # # # # #                 shiftStatus="working",
# # # # # #                 user_id=Timer.User_id)
# # # # # #             # print(Timer.image_bytes)
# # # # # #             print(Timer.CurrentTab)
# # # # # #             print(Timer.User_id)

# # # # # #         print("Clicks not Posted")
# # # # # #         self.root.after(10000, self.posting_clicks)

# # # # # #     def stop_timer(self):
# # # # # #         if self.running:
# # # # # #             self.running = False
# # # # # #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
# # # # # #             # self.save_state()
# # # # # #             if self.is_tracking:
# # # # # #                 self.pause_tracking = True  # Pause tracking
# # # # # #                 Timer.recursion = False
# # # # # #                 Timer.activity_recursion = False

# # # # # #     def end_shift(self):
# # # # # #         from helper_functions import encrypt_data, set_permissions ,fernet_key
# # # # # #         from api_services import checkout
# # # # # #         self.stop_timer()
# # # # # #         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# # # # # #         if confirmation:
# # # # # #             messagebox.showinfo("Shift Ended", "Shift has ended.")
# # # # # #             state = {
# # # # # #                 "elapsed_time": 0,
# # # # # #                 "abs_start_time": 0,
# # # # # #                 "running": False
# # # # # #             }
# # # # # #             with open(state_file, "wb") as f:
# # # # # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # # # # #             set_permissions(state_file)  # Set file permissions after writing
# # # # # #             checkout(Timer.User_id);
# # # # # #             print("State saved.")
# # # # # #         else:
# # # # # #             self.start_timer()

# # # # # #     def start_tracking(self):
# # # # # #         if not self.is_tracking:
# # # # # #             self.tracking_thread = threading.Thread(target=self.track_mouse)
# # # # # #             self.tracking_thread.daemon = True
# # # # # #             self.tracking_thread.start()
# # # # # #             self.is_tracking = True

# # # # # #     def track_mouse(self):
# # # # # #         with Listener(on_click=self.on_click) as listener:
# # # # # #             listener.join()

# # # # # #     def on_click(self, x, y, button, pressed):
# # # # # #         if not self.pause_tracking:
# # # # # #             if pressed:
# # # # # #                 Timer.isclicked = "true"
# # # # # #                 Timer.employeeStatus = 1

# # # # # #     def activity(self):
# # # # # #         from helper_functions import ActiveTabs

# # # # # #         ActiveTabs()
# # # # # #         if self.activity_recursion and self.running:
# # # # # #             self.root.after(15000, self.activity)

# # # # # #     def take_screenshot(self):
# # # # # #         from helper_functions import ActiveTabs

# # # # # #         if Timer.recursion and self.running:
# # # # # #             ActiveTabs()
# # # # # #             try:
# # # # # #                 screenshot = ImageGrab.grab()

# # # # # #                 # Convert image to RGB if it has an alpha channel
# # # # # #                 if screenshot.mode == 'RGBA':
# # # # # #                     screenshot = screenshot.convert('RGB')

# # # # # #                 image_stream = BytesIO()
# # # # # #                 # Save as JPEG with quality setting
# # # # # #                 screenshot.save(image_stream, format='JPEG', quality=5)
# # # # # #                 Timer.image_bytes = image_stream.getvalue()

# # # # # #                 # Print the size of the image in bytes
# # # # # #                 image_size = len(Timer.image_bytes)
# # # # # #                 # print(f"Size of the image: {image_size} bytes")

# # # # # #                 self.root.after(175000, self.take_screenshot)
# # # # # #             except Exception as e:
# # # # # #                 print(f"Error taking screenshot: {e}")
# # # # # #                 self.root.after(175000, self.take_screenshot)

# # # # # #     def save_state(self):
# # # # # #         from helper_functions import encrypt_data, set_permissions ,fernet_key

# # # # # #         try:
# # # # # #             state = {
# # # # # #                 "elapsed_time": self.elapsed_time,
# # # # # #                 "abs_start_time": self.abs_start_time,
# # # # # #                 "running": self.running
# # # # # #                 # Add other variables you want to save
# # # # # #             }
# # # # # #             with open(state_file, "wb") as f:
# # # # # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # # # # #             set_permissions(state_file)  # Set file permissions after writing
# # # # # #             print("State saved.")
# # # # # #         except Exception as e:
# # # # # #             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

# # # # # #     def load_state(self):
# # # # # #         from helper_functions import decrypt_data,fernet_key

# # # # # #         try:
# # # # # #             if os.path.exists(state_file):
# # # # # #                 with open(state_file, "rb") as f:
# # # # # #                     encrypted_state = f.read()
# # # # # #                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
# # # # # #                 state = json.loads(decrypted_state)
# # # # # #                 self.elapsed_time = state.get("elapsed_time", 0)
# # # # # #                 self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
# # # # # #                 self.running = state.get("running", False)
# # # # # #                 if self.running:
# # # # # #                     self.pause_tracking = False  # Resume tracking if paused
# # # # # #                     Timer.recursion = True
# # # # # #                     Timer.activity_recursion = True
# # # # # #                     self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
# # # # # #                     self.activity()
# # # # # #                     self.take_screenshot()
# # # # # #                     self.start_tracking()

# # # # # #                 print("State loaded.")
# # # # # #             else:
# # # # # #                 self.elapsed_time = 0
# # # # # #                 self.abs_start_time = time.time()  # Default to current time if no saved state
# # # # # #                 print("No previous state found.")
# # # # # #         except Exception as e:
# # # # # #             messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

# # # # # #     def update_timer(self):
# # # # # #         if self.running:
# # # # # #             self.elapsed_time = time.time() - self.abs_start_time
# # # # # #             # self.save_state()

# # # # # #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# # # # # #         hours, minutes = divmod(minutes, 60)
# # # # # #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# # # # # #         self.lblTimer.config(text=time_str)

# # # # # #         # Schedule the next update
# # # # # #         self.root.after(1000, self.update_timer)





# # # # # # def display_timer():
# # # # # #     root = tk.Tk()
# # # # # #     Timer(root)
# # # # # #     root.mainloop()


# # # # # # if __name__ == "__main__":
# # # # # #     display_timer()


# # # # # import json
# # # # # import os
# # # # # import platform
# # # # # import tkinter as tk
# # # # # import threading
# # # # # import time
# # # # # from tkinter import messagebox
# # # # # from PIL import Image, ImageGrab
# # # # # from io import BytesIO
# # # # # from pynput.mouse import Listener
# # # # # from cryptography.fernet import Fernet





# # # # # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # # # # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # # # # state_file = "program.json"
# # # # # system_platform = platform.system()


# # # # # class Timer:
# # # # #     recursion = False
# # # # #     activity_recursion = False
# # # # #     isclicked = "false"
# # # # #     imagepath = ""
# # # # #     bearer_token = ""
# # # # #     User_id = ""
# # # # #     CurrentTime = ""
# # # # #     CurrentTab = ""
# # # # #     ispressed = "false"
# # # # #     image_bytes=""
# # # # #     employeeStatus = 0

# # # # #     def __init__(self, root):
# # # # #         self.root = root
# # # # #         self.root.title("Mudeer")
# # # # #         window_width = 600
# # # # #         window_height = 300
# # # # #         x_position = (root.winfo_screenwidth() - window_width) // 2
# # # # #         y_position = (root.winfo_screenheight() - window_height) // 2
# # # # #         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

# # # # #         self.time = 0
# # # # #         self.running = False
# # # # #         self.abs_start_time = time.time()  # Absolute start time of the timer
# # # # #         self.elapsed_time = 0
# # # # #         self.is_tracking = False
# # # # #         self.tracking_thread = None
# # # # #         self.pause_tracking = False  # Flag to indicate tracking should pause
# # # # #         self.clickArray = []
# # # # #         self.first_start = True  # Flag to track if it's the first start

# # # # #         rootFrame = tk.Frame(root, pady=10, padx=10)
# # # # #         rootFrame.pack(expand=True)

# # # # #         lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
# # # # #         lblTitle.pack(pady=(0, 10))

# # # # #         MainFrame = tk.Frame(root, pady=10, padx=10)
# # # # #         MainFrame.pack(expand=True)

# # # # #         MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
# # # # #         MainFrameTop.pack()

# # # # #         MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
# # # # #         MainFrameDown.pack()

# # # # #         self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
# # # # #         self.lblTimer.pack(pady=10)

# # # # #         self.btnStart = tk.Button(
# # # # #             MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
# # # # #             command=self.start_timer
# # # # #         )
# # # # #         self.btnStart.pack(side=tk.LEFT, padx=10)

# # # # #         self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # # # #                                  command=self.stop_timer)
# # # # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # # # #         self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # # # #                                  command=self.end_shift)
# # # # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # # # #         self.load_state()  # Load saved state when initializing]

# # # # #         self.pusing_eventActivity()
# # # # #         self.posting_clicks()

# # # # #         self.update_timer()

# # # # #     def start_timer(self):
# # # # #         if not self.running:
# # # # #             self.running = True
# # # # #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# # # # #             self.pause_tracking = False  # Resume tracking if paused

# # # # #             # If it's not the first start (i.e., resuming from pause), call stop_break
# # # # #             if not self.first_start:
# # # # #                 from api_services import stop_break
# # # # #                 stop_break(Timer.User_id)
# # # # #                 print("Break stopped - Resuming work")
            
# # # # #             # Set first_start to False after the first start
# # # # #             self.first_start = False

# # # # #             Timer.recursion = True
# # # # #             Timer.activity_recursion = True
# # # # #             self.activity()
# # # # #             self.take_screenshot()
# # # # #             self.start_tracking()

# # # # #     def pusing_eventActivity(self):
# # # # #         from api_services import event_activity
# # # # #         # print(self.running)
# # # # #         if self.running:
# # # # #             print("event Activity Pushed")
            
# # # # #             print(Timer.isclicked)      
# # # # #             print(Timer.ispressed)
# # # # #             print(Timer.employeeStatus)
# # # # #             print(Timer.CurrentTab)
# # # # #             print(round(self.elapsed_time))
# # # # #             print(Timer.User_id)
# # # # #             print(Timer.bearer_token)
      
# # # # #             event_activity(mouseclick=Timer.isclicked,
# # # # #                            keystroke=Timer.ispressed,
# # # # #                            employeeStatus=Timer.employeeStatus,
# # # # #                            activeTab=Timer.CurrentTab,
# # # # #                            hoursPassed=round(self.elapsed_time),
# # # # #                            shiftstatus="working",
# # # # #                            user_id=Timer.User_id,
# # # # #                            bearer_token=Timer.bearer_token,)

# # # # #         print("event Activity not pushed")
# # # # #         self.root.after(17000, self.pusing_eventActivity)

# # # # #     def posting_clicks(self):
# # # # #         from api_services import post_clicks

# # # # #         print(self.running)
# # # # #         if self.running:
# # # # #             print("Clicks Posted")
# # # # #             post_clicks(
# # # # #                 imagepath=Timer.image_bytes,
# # # # #                 activeTab=Timer.CurrentTab,
# # # # #                 shiftStatus="working",
# # # # #                 user_id=Timer.User_id)
# # # # #             # print(Timer.image_bytes)
# # # # #             print(Timer.CurrentTab)
# # # # #             print(Timer.User_id)

# # # # #         print("Clicks not Posted")
# # # # #         self.root.after(10000, self.posting_clicks)

# # # # #     def stop_timer(self):
# # # # #         if self.running:
# # # # #             self.running = False
# # # # #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
# # # # #             # Call start_break when pausing
# # # # #             from api_services import start_break
# # # # #             start_break(Timer.User_id)
# # # # #             print("Break started - Timer paused")
            
# # # # #             # self.save_state()
# # # # #             if self.is_tracking:
# # # # #                 self.pause_tracking = True  # Pause tracking
# # # # #                 Timer.recursion = False
# # # # #                 Timer.activity_recursion = False

# # # # #     def end_shift(self):
# # # # #         from helper_functions import encrypt_data, set_permissions ,fernet_key
# # # # #         from api_services import checkout
# # # # #         self.stop_timer()
# # # # #         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# # # # #         if confirmation:
# # # # #             messagebox.showinfo("Shift Ended", "Shift has ended.")
# # # # #             state = {
# # # # #                 "elapsed_time": 0,
# # # # #                 "abs_start_time": 0,
# # # # #                 "running": False
# # # # #             }
# # # # #             with open(state_file, "wb") as f:
# # # # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # # # #             set_permissions(state_file)  # Set file permissions after writing
# # # # #             checkout(Timer.User_id)
# # # # #             print("State saved.")
            
# # # # #             # Reset first_start flag when shift ends
# # # # #             self.first_start = True
# # # # #         else:
# # # # #             self.start_timer()

# # # # #     def start_tracking(self):
# # # # #         if not self.is_tracking:
# # # # #             self.tracking_thread = threading.Thread(target=self.track_mouse)
# # # # #             self.tracking_thread.daemon = True
# # # # #             self.tracking_thread.start()
# # # # #             self.is_tracking = True

# # # # #     def track_mouse(self):
# # # # #         with Listener(on_click=self.on_click) as listener:
# # # # #             listener.join()

# # # # #     def on_click(self, x, y, button, pressed):
# # # # #         if not self.pause_tracking:
# # # # #             if pressed:
# # # # #                 Timer.isclicked = "true"
# # # # #                 Timer.employeeStatus = 1

# # # # #     def activity(self):
# # # # #         from helper_functions import ActiveTabs

# # # # #         ActiveTabs()
# # # # #         if self.activity_recursion and self.running:
# # # # #             self.root.after(15000, self.activity)

# # # # #     def take_screenshot(self):
# # # # #         from helper_functions import ActiveTabs

# # # # #         if Timer.recursion and self.running:
# # # # #             ActiveTabs()
# # # # #             try:
# # # # #                 screenshot = ImageGrab.grab()

# # # # #                 # Convert image to RGB if it has an alpha channel
# # # # #                 if screenshot.mode == 'RGBA':
# # # # #                     screenshot = screenshot.convert('RGB')

# # # # #                 image_stream = BytesIO()
# # # # #                 # Save as JPEG with quality setting
# # # # #                 screenshot.save(image_stream, format='JPEG', quality=5)
# # # # #                 Timer.image_bytes = image_stream.getvalue()

# # # # #                 # Print the size of the image in bytes
# # # # #                 image_size = len(Timer.image_bytes)
# # # # #                 # print(f"Size of the image: {image_size} bytes")

# # # # #                 self.root.after(175000, self.take_screenshot)
# # # # #             except Exception as e:
# # # # #                 print(f"Error taking screenshot: {e}")
# # # # #                 self.root.after(175000, self.take_screenshot)

# # # # #     def save_state(self):
# # # # #         from helper_functions import encrypt_data, set_permissions ,fernet_key

# # # # #         try:
# # # # #             state = {
# # # # #                 "elapsed_time": self.elapsed_time,
# # # # #                 "abs_start_time": self.abs_start_time,
# # # # #                 "running": self.running,
# # # # #                 "first_start": self.first_start  # Save first_start flag
# # # # #                 # Add other variables you want to save
# # # # #             }
# # # # #             with open(state_file, "wb") as f:
# # # # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # # # #             set_permissions(state_file)  # Set file permissions after writing
# # # # #             print("State saved.")
# # # # #         except Exception as e:
# # # # #             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

# # # # #     def load_state(self):
# # # # #         from helper_functions import decrypt_data,fernet_key

# # # # #         try:
# # # # #             if os.path.exists(state_file):
# # # # #                 with open(state_file, "rb") as f:
# # # # #                     encrypted_state = f.read()
# # # # #                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
# # # # #                 state = json.loads(decrypted_state)
# # # # #                 self.elapsed_time = state.get("elapsed_time", 0)
# # # # #                 self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
# # # # #                 self.running = state.get("running", False)
# # # # #                 self.first_start = state.get("first_start", True)  # Load first_start flag
                
# # # # #                 if self.running:
# # # # #                     self.pause_tracking = False  # Resume tracking if paused
# # # # #                     Timer.recursion = True
# # # # #                     Timer.activity_recursion = True
# # # # #                     self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
# # # # #                     self.activity()
# # # # #                     self.take_screenshot()
# # # # #                     self.start_tracking()

# # # # #                 print("State loaded.")
# # # # #             else:
# # # # #                 self.elapsed_time = 0
# # # # #                 self.abs_start_time = time.time()  # Default to current time if no saved state
# # # # #                 print("No previous state found.")
# # # # #         except Exception as e:
# # # # #             messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

# # # # #     def update_timer(self):
# # # # #         if self.running:
# # # # #             self.elapsed_time = time.time() - self.abs_start_time
# # # # #             # self.save_state()

# # # # #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# # # # #         hours, minutes = divmod(minutes, 60)
# # # # #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# # # # #         self.lblTimer.config(text=time_str)

# # # # #         # Schedule the next update
# # # # #         self.root.after(1000, self.update_timer)





# # # # # def display_timer():
# # # # #     root = tk.Tk()
# # # # #     Timer(root)
# # # # #     root.mainloop()


# # # # # if __name__ == "__main__":
# # # # #     display_timer()






# # # # import json
# # # # import os
# # # # import platform
# # # # import tkinter as tk
# # # # import threading
# # # # import time
# # # # from tkinter import messagebox
# # # # from PIL import Image, ImageGrab
# # # # from io import BytesIO
# # # # from pynput.mouse import Listener
# # # # from cryptography.fernet import Fernet





# # # # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # # # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # # # state_file = "program.json"
# # # # system_platform = platform.system()


# # # # class Timer:
# # # #     recursion = False
# # # #     activity_recursion = False
# # # #     isclicked = "false"
# # # #     imagepath = ""
# # # #     bearer_token = ""
# # # #     User_id = ""
# # # #     CurrentTime = ""
# # # #     CurrentTab = ""
# # # #     ispressed = "false"
# # # #     image_bytes=""
# # # #     employeeStatus = 0

# # # #     def __init__(self, root):
# # # #         self.root = root
# # # #         self.root.title("Mudeer")
# # # #         window_width = 600
# # # #         window_height = 300
# # # #         x_position = (root.winfo_screenwidth() - window_width) // 2
# # # #         y_position = (root.winfo_screenheight() - window_height) // 2
# # # #         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

# # # #         self.time = 0
# # # #         self.running = False
# # # #         self.abs_start_time = time.time()  # Absolute start time of the timer
# # # #         self.elapsed_time = 0
# # # #         self.is_tracking = False
# # # #         self.tracking_thread = None
# # # #         self.pause_tracking = False  # Flag to indicate tracking should pause
# # # #         self.clickArray = []
# # # #         self.first_start = True  # Flag to track if it's the first start
# # # #         self.scheduled_tasks = {}  # Track all scheduled callbacks for proper cleanup

# # # #         rootFrame = tk.Frame(root, pady=10, padx=10)
# # # #         rootFrame.pack(expand=True)

# # # #         lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
# # # #         lblTitle.pack(pady=(0, 10))

# # # #         MainFrame = tk.Frame(root, pady=10, padx=10)
# # # #         MainFrame.pack(expand=True)

# # # #         MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
# # # #         MainFrameTop.pack()

# # # #         MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
# # # #         MainFrameDown.pack()

# # # #         self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
# # # #         self.lblTimer.pack(pady=10)

# # # #         self.btnStart = tk.Button(
# # # #             MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
# # # #             command=self.start_timer
# # # #         )
# # # #         self.btnStart.pack(side=tk.LEFT, padx=10)

# # # #         self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # # #                                  command=self.stop_timer)
# # # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # # #         self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # # #                                  command=self.end_shift)
# # # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # # #         self.load_state()  # Load saved state when initializing]

# # # #         self.pusing_eventActivity()
# # # #         self.posting_clicks()

# # # #         self.update_timer()

# # # #     def schedule_task(self, task_name, callback, interval):
# # # #         """Schedule a task with proper tracking and cancellation"""
# # # #         # Cancel existing task if any
# # # #         self.cancel_task(task_name)
        
# # # #         # Schedule new task and store the ID
# # # #         task_id = self.root.after(interval, callback)
# # # #         self.scheduled_tasks[task_name] = task_id
# # # #         return task_id
    
# # # #     def cancel_task(self, task_name):
# # # #         """Cancel a specific scheduled task"""
# # # #         if task_name in self.scheduled_tasks:
# # # #             try:
# # # #                 self.root.after_cancel(self.scheduled_tasks[task_name])
# # # #             except:
# # # #                 pass  # Task might already be executed
# # # #             del self.scheduled_tasks[task_name]
    
# # # #     def cancel_all_tasks(self):
# # # #         """Cancel all scheduled tasks"""
# # # #         for task_name in list(self.scheduled_tasks.keys()):
# # # #             self.cancel_task(task_name)

# # # #     def start_timer(self):
# # # #         if not self.running:
# # # #             self.running = True
# # # #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# # # #             self.pause_tracking = False  # Resume tracking if paused

# # # #             # If it's not the first start (i.e., resuming from pause), call stop_break
# # # #             if not self.first_start:
# # # #                 # Run in background thread to avoid blocking UI
# # # #                 threading.Thread(target=self._stop_break_worker, daemon=True).start()
            
# # # #             # Set first_start to False after the first start
# # # #             self.first_start = False

# # # #             Timer.recursion = True
# # # #             Timer.activity_recursion = True
# # # #             self.activity()
# # # #             self.take_screenshot()
# # # #             self.start_tracking()
    
# # # #     def _stop_break_worker(self):
# # # #         """Background worker for stop_break - doesn't block UI"""
# # # #         try:
# # # #             from api_services import stop_break
# # # #             stop_break(Timer.User_id)
# # # #             print("Break stopped - Resuming work")
# # # #         except Exception as e:
# # # #             print(f"Error stopping break: {e}")

# # # #     def pusing_eventActivity(self):
# # # #         if self.running:
# # # #             # Run API call in background thread to avoid blocking UI
# # # #             threading.Thread(target=self._pusing_eventActivity_worker, daemon=True).start()
# # # #         else:
# # # #             print("event Activity not pushed")
        
# # # #         self.schedule_task('event_activity', self.pusing_eventActivity, 17000)
    
# # # #     def _pusing_eventActivity_worker(self):
# # # #         """Background worker for event activity - doesn't block UI"""
# # # #         try:
# # # #             from api_services import event_activity
            
# # # #             print("event Activity Pushed")
# # # #             print(Timer.isclicked)      
# # # #             print(Timer.ispressed)
# # # #             print(Timer.employeeStatus)
# # # #             print(Timer.CurrentTab)
# # # #             print(round(self.elapsed_time))
# # # #             print(Timer.User_id)
# # # #             print(Timer.bearer_token)
      
# # # #             event_activity(mouseclick=Timer.isclicked,
# # # #                            keystroke=Timer.ispressed,
# # # #                            employeeStatus=Timer.employeeStatus,
# # # #                            activeTab=Timer.CurrentTab,
# # # #                            hoursPassed=round(self.elapsed_time),
# # # #                            shiftstatus="working",
# # # #                            user_id=Timer.User_id,
# # # #                            bearer_token=Timer.bearer_token,)
# # # #         except Exception as e:
# # # #             print(f"Error in event activity: {e}")

# # # #     def posting_clicks(self):
# # # #         if self.running:
# # # #             # Run API call in background thread to avoid blocking UI
# # # #             threading.Thread(target=self._posting_clicks_worker, daemon=True).start()
# # # #         else:
# # # #             print("Clicks not Posted")
        
# # # #         self.schedule_task('post_clicks', self.posting_clicks, 10000)
    
# # # #     def _posting_clicks_worker(self):
# # # #         """Background worker for posting clicks - doesn't block UI"""
# # # #         try:
# # # #             from api_services import post_clicks
            
# # # #             print(self.running)
# # # #             print("Clicks Posted")
# # # #             post_clicks(
# # # #                 imagepath=Timer.image_bytes,
# # # #                 activeTab=Timer.CurrentTab,
# # # #                 shiftStatus="working",
# # # #                 user_id=Timer.User_id)
# # # #             # print(Timer.image_bytes)
# # # #             print(Timer.CurrentTab)
# # # #             print(Timer.User_id)
# # # #         except Exception as e:
# # # #             print(f"Error in posting clicks: {e}")

# # # #     def stop_timer(self):
# # # #         if self.running:
# # # #             self.running = False
# # # #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
# # # #             # Call start_break when pausing - run in background thread
# # # #             threading.Thread(target=self._start_break_worker, daemon=True).start()
            
# # # #             # Cancel tasks that should stop when paused
# # # #             self.cancel_task('activity')
# # # #             self.cancel_task('screenshot')
            
# # # #             # self.save_state()
# # # #             if self.is_tracking:
# # # #                 self.pause_tracking = True  # Pause tracking
# # # #                 Timer.recursion = False
# # # #                 Timer.activity_recursion = False
    
# # # #     def _start_break_worker(self):
# # # #         """Background worker for start_break - doesn't block UI"""
# # # #         try:
# # # #             from api_services import start_break
# # # #             start_break(Timer.User_id)
# # # #             print("Break started - Timer paused")
# # # #         except Exception as e:
# # # #             print(f"Error starting break: {e}")

# # # #     def end_shift(self):
# # # #         from helper_functions import encrypt_data, set_permissions ,fernet_key
# # # #         self.stop_timer()
# # # #         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# # # #         if confirmation:
# # # #             messagebox.showinfo("Shift Ended", "Shift has ended.")
# # # #             state = {
# # # #                 "elapsed_time": 0,
# # # #                 "abs_start_time": 0,
# # # #                 "running": False
# # # #             }
# # # #             with open(state_file, "wb") as f:
# # # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # # #             set_permissions(state_file)  # Set file permissions after writing
            
# # # #             # Run checkout in background thread
# # # #             threading.Thread(target=self._checkout_worker, daemon=True).start()
            
# # # #             print("State saved.")
            
# # # #             # Reset first_start flag when shift ends
# # # #             self.first_start = True
# # # #         else:
# # # #             self.start_timer()
    
# # # #     def _checkout_worker(self):
# # # #         """Background worker for checkout - doesn't block UI"""
# # # #         try:
# # # #             from api_services import checkout
# # # #             checkout(Timer.User_id)
# # # #         except Exception as e:
# # # #             print(f"Error in checkout: {e}")

# # # #     def start_tracking(self):
# # # #         if not self.is_tracking:
# # # #             self.tracking_thread = threading.Thread(target=self.track_mouse)
# # # #             self.tracking_thread.daemon = True
# # # #             self.tracking_thread.start()
# # # #             self.is_tracking = True

# # # #     def track_mouse(self):
# # # #         with Listener(on_click=self.on_click) as listener:
# # # #             listener.join()

# # # #     def on_click(self, x, y, button, pressed):
# # # #         if not self.pause_tracking:
# # # #             if pressed:
# # # #                 Timer.isclicked = "true"
# # # #                 Timer.employeeStatus = 1

# # # #     def activity(self):
# # # #         from helper_functions import ActiveTabs

# # # #         ActiveTabs()
# # # #         if self.activity_recursion and self.running:
# # # #             self.schedule_task('activity', self.activity, 15000)

# # # #     def take_screenshot(self):
# # # #         from helper_functions import ActiveTabs

# # # #         if Timer.recursion and self.running:
# # # #             ActiveTabs()
# # # #             try:
# # # #                 screenshot = ImageGrab.grab()

# # # #                 # Convert image to RGB if it has an alpha channel
# # # #                 if screenshot.mode == 'RGBA':
# # # #                     screenshot = screenshot.convert('RGB')

# # # #                 image_stream = BytesIO()
# # # #                 # Save as JPEG with quality setting
# # # #                 screenshot.save(image_stream, format='JPEG', quality=5)
# # # #                 Timer.image_bytes = image_stream.getvalue()

# # # #                 # Print the size of the image in bytes
# # # #                 image_size = len(Timer.image_bytes)
# # # #                 # print(f"Size of the image: {image_size} bytes")

# # # #                 self.schedule_task('screenshot', self.take_screenshot, 175000)
# # # #             except Exception as e:
# # # #                 print(f"Error taking screenshot: {e}")
# # # #                 self.schedule_task('screenshot', self.take_screenshot, 175000)

# # # #     def save_state(self):
# # # #         from helper_functions import encrypt_data, set_permissions ,fernet_key

# # # #         try:
# # # #             state = {
# # # #                 "elapsed_time": self.elapsed_time,
# # # #                 "abs_start_time": self.abs_start_time,
# # # #                 "running": self.running,
# # # #                 "first_start": self.first_start  # Save first_start flag
# # # #                 # Add other variables you want to save
# # # #             }
# # # #             with open(state_file, "wb") as f:
# # # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # # #             set_permissions(state_file)  # Set file permissions after writing
# # # #             print("State saved.")
# # # #         except Exception as e:
# # # #             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

# # # #     def load_state(self):
# # # #         from helper_functions import decrypt_data,fernet_key

# # # #         try:
# # # #             if os.path.exists(state_file):
# # # #                 with open(state_file, "rb") as f:
# # # #                     encrypted_state = f.read()
# # # #                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
# # # #                 state = json.loads(decrypted_state)
# # # #                 self.elapsed_time = state.get("elapsed_time", 0)
# # # #                 self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
# # # #                 self.running = state.get("running", False)
# # # #                 self.first_start = state.get("first_start", True)  # Load first_start flag
                
# # # #                 if self.running:
# # # #                     self.pause_tracking = False  # Resume tracking if paused
# # # #                     Timer.recursion = True
# # # #                     Timer.activity_recursion = True
# # # #                     self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
# # # #                     self.activity()
# # # #                     self.take_screenshot()
# # # #                     self.start_tracking()

# # # #                 print("State loaded.")
# # # #             else:
# # # #                 self.elapsed_time = 0
# # # #                 self.abs_start_time = time.time()  # Default to current time if no saved state
# # # #                 print("No previous state found.")
# # # #         except Exception as e:
# # # #             messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

# # # #     def update_timer(self):
# # # #         if self.running:
# # # #             self.elapsed_time = time.time() - self.abs_start_time
# # # #             # self.save_state()

# # # #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# # # #         hours, minutes = divmod(minutes, 60)
# # # #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# # # #         self.lblTimer.config(text=time_str)

# # # #         # Schedule the next update
# # # #         self.schedule_task('timer_display', self.update_timer, 1000)





# # # # def display_timer():
# # # #     root = tk.Tk()
# # # #     Timer(root)
# # # #     root.mainloop()


# # # # if __name__ == "__main__":
# # # #     display_timer()


# # # import json
# # # import os
# # # import platform
# # # import tkinter as tk
# # # import threading
# # # import time
# # # from tkinter import messagebox
# # # from PIL import Image, ImageGrab
# # # from io import BytesIO
# # # from pynput.mouse import Listener
# # # from cryptography.fernet import Fernet





# # # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # # state_file = "program.json"
# # # system_platform = platform.system()


# # # class Timer:
# # #     def __init__(self, root):
# # #         # Convert class variables to instance variables
# # #         self.recursion = False
# # #         self.activity_recursion = False
# # #         self.isclicked = "false"
# # #         self.imagepath = ""
# # #         self.bearer_token = ""
# # #         self.user_id = ""
# # #         self.current_time = ""
# # #         self.current_tab = ""
# # #         self.ispressed = "false"
# # #         self.image_bytes = b""
# # #         self.employee_status = 0
        
# # #         self.root = root
# # #         self.root.title("Mudeer")
# # #         window_width = 600
# # #         window_height = 300
# # #         x_position = (root.winfo_screenwidth() - window_width) // 2
# # #         y_position = (root.winfo_screenheight() - window_height) // 2
# # #         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

# # #         self.time = 0
# # #         self.running = False
# # #         self.abs_start_time = time.time()  # Absolute start time of the timer
# # #         self.elapsed_time = 0
# # #         self.is_tracking = False
# # #         self.tracking_thread = None
# # #         self.pause_tracking = False  # Flag to indicate tracking should pause
# # #         self.clickArray = []
# # #         self.first_start = True  # Flag to track if it's the first start
# # #         self.scheduled_tasks = {}  # Track all scheduled callbacks for proper cleanup

# # #         rootFrame = tk.Frame(root, pady=10, padx=10)
# # #         rootFrame.pack(expand=True)

# # #         lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
# # #         lblTitle.pack(pady=(0, 10))

# # #         MainFrame = tk.Frame(root, pady=10, padx=10)
# # #         MainFrame.pack(expand=True)

# # #         MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
# # #         MainFrameTop.pack()

# # #         MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
# # #         MainFrameDown.pack()

# # #         self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
# # #         self.lblTimer.pack(pady=10)

# # #         self.btnStart = tk.Button(
# # #             MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
# # #             command=self.start_timer
# # #         )
# # #         self.btnStart.pack(side=tk.LEFT, padx=10)

# # #         self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # #                                  command=self.stop_timer)
# # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # #         self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # #                                  command=self.end_shift)
# # #         self.btnStop.pack(side=tk.LEFT, padx=10)

# # #         self.load_state()  # Load saved state when initializing]

# # #         # Register this timer instance with the key logger
# # #         from key_logger import set_timer_instance
# # #         set_timer_instance(self)

# # #         self.pusing_eventActivity()
# # #         self.posting_clicks()

# # #         self.update_timer()

# # #     def schedule_task(self, task_name, callback, interval):
# # #         """Schedule a task with proper tracking and cancellation"""
# # #         # Cancel existing task if any
# # #         self.cancel_task(task_name)
        
# # #         # Schedule new task and store the ID
# # #         task_id = self.root.after(interval, callback)
# # #         self.scheduled_tasks[task_name] = task_id
# # #         return task_id
    
# # #     def cancel_task(self, task_name):
# # #         """Cancel a specific scheduled task"""
# # #         if task_name in self.scheduled_tasks:
# # #             try:
# # #                 self.root.after_cancel(self.scheduled_tasks[task_name])
# # #             except:
# # #                 pass  # Task might already be executed
# # #             del self.scheduled_tasks[task_name]
    
# # #     def cancel_all_tasks(self):
# # #         """Cancel all scheduled tasks"""
# # #         for task_name in list(self.scheduled_tasks.keys()):
# # #             self.cancel_task(task_name)

# # #     def start_timer(self):
# # #         if not self.running:
# # #             self.running = True
# # #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# # #             self.pause_tracking = False  # Resume tracking if paused

# # #             # If it's not the first start (i.e., resuming from pause), call stop_break
# # #             if not self.first_start:
# # #                 # Run in background thread to avoid blocking UI
# # #                 threading.Thread(target=self._stop_break_worker, daemon=True).start()
            
# # #             # Set first_start to False after the first start
# # #             self.first_start = False

# # #             self.recursion = True
# # #             self.activity_recursion = True
# # #             self.activity()
# # #             self.take_screenshot()
# # #             self.start_tracking()
    
# # #     def _stop_break_worker(self):
# # #         """Background worker for stop_break - doesn't block UI"""
# # #         try:
# # #             from api_services import stop_break
# # #             stop_break(self.user_id, self.bearer_token)
# # #             print("Break stopped - Resuming work")
# # #         except Exception as e:
# # #             print(f"Error stopping break: {e}")

# # #     def pusing_eventActivity(self):
# # #         if self.running:
# # #             # Run API call in background thread to avoid blocking UI
# # #             threading.Thread(target=self._pusing_eventActivity_worker, daemon=True).start()
# # #         else:
# # #             print("event Activity not pushed")
        
# # #         self.schedule_task('event_activity', self.pusing_eventActivity, 17000)
    
# # #     def _pusing_eventActivity_worker(self):
# # #         """Background worker for event activity - doesn't block UI"""
# # #         try:
# # #             from api_services import event_activity
            
# # #             print("event Activity Pushed")
# # #             print(self.isclicked)      
# # #             print(self.ispressed)
# # #             print(self.employee_status)
# # #             print(self.current_tab)
# # #             print(round(self.elapsed_time))
# # #             print(self.user_id)
# # #             print(self.bearer_token)
      
# # #             event_activity(mouseclick=self.isclicked,
# # #                            keystroke=self.ispressed,
# # #                            employeeStatus=self.employee_status,
# # #                            activeTab=self.current_tab,
# # #                            hoursPassed=round(self.elapsed_time),
# # #                            shiftstatus="working",
# # #                            user_id=self.user_id,
# # #                            bearer_token=self.bearer_token,
# # #                            timer_instance=self)  # Pass self to update flags
# # #         except Exception as e:
# # #             print(f"Error in event activity: {e}")

# # #     def posting_clicks(self):
# # #         if self.running:
# # #             # Run API call in background thread to avoid blocking UI
# # #             threading.Thread(target=self._posting_clicks_worker, daemon=True).start()
# # #         else:
# # #             print("Clicks not Posted")
        
# # #         self.schedule_task('post_clicks', self.posting_clicks, 17500)
    
# # #     def _posting_clicks_worker(self):
# # #         """Background worker for posting clicks - doesn't block UI"""
# # #         try:
# # #             from api_services import post_clicks
            
# # #             print(self.running)
# # #             print("Clicks Posted")
# # #             post_clicks(
# # #                 imagepath=self.image_bytes,
# # #                 activeTab=self.current_tab,
# # #                 shiftStatus="working",
# # #                 user_id=self.user_id,
# # #                 bearer_token=self.bearer_token)
# # #             # print(self.image_bytes)
# # #             print(self.current_tab)
# # #             print(self.user_id)
# # #         except Exception as e:
# # #             print(f"Error in posting clicks: {e}")

# # #     def stop_timer(self):
# # #         if self.running:
# # #             self.running = False
# # #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
# # #             # Call start_break when pausing - run in background thread
# # #             threading.Thread(target=self._start_break_worker, daemon=True).start()
            
# # #             # Cancel tasks that should stop when paused
# # #             self.cancel_task('activity')
# # #             self.cancel_task('screenshot')
            
# # #             # self.save_state()
# # #             if self.is_tracking:
# # #                 self.pause_tracking = True  # Pause tracking
# # #                 self.recursion = False
# # #                 self.activity_recursion = False
    
# # #     def _start_break_worker(self):
# # #         """Background worker for start_break - doesn't block UI"""
# # #         try:
# # #             from api_services import start_break
# # #             start_break(self.user_id, self.bearer_token)
# # #             print("Break started - Timer paused")
# # #         except Exception as e:
# # #             print(f"Error starting break: {e}")

# # #     def end_shift(self):
# # #         from helper_functions import encrypt_data, set_permissions ,fernet_key
# # #         self.stop_timer()
# # #         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# # #         if confirmation:
# # #             messagebox.showinfo("Shift Ended", "Shift has ended.")
# # #             state = {
# # #                 "elapsed_time": 0,
# # #                 "abs_start_time": 0,
# # #                 "running": False
# # #             }
# # #             with open(state_file, "wb") as f:
# # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # #             set_permissions(state_file)  # Set file permissions after writing
            
# # #             # Run checkout in background thread
# # #             threading.Thread(target=self._checkout_worker, daemon=True).start()
            
# # #             print("State saved.")
            
# # #             # Reset first_start flag when shift ends
# # #             self.first_start = True
# # #         else:
# # #             self.start_timer()
    
# # #     def _checkout_worker(self):
# # #         """Background worker for checkout - doesn't block UI"""
# # #         try:
# # #             from api_services import checkout
# # #             checkout(self.user_id, self.bearer_token)
# # #         except Exception as e:
# # #             print(f"Error in checkout: {e}")

# # #     def start_tracking(self):
# # #         if not self.is_tracking:
# # #             self.tracking_thread = threading.Thread(target=self.track_mouse)
# # #             self.tracking_thread.daemon = True
# # #             self.tracking_thread.start()
# # #             self.is_tracking = True

# # #     def track_mouse(self):
# # #         with Listener(on_click=self.on_click) as listener:
# # #             listener.join()

# # #     def on_click(self, x, y, button, pressed):
# # #         if not self.pause_tracking:
# # #             if pressed:
# # #                 self.isclicked = "true"
# # #                 self.employee_status = 1

# # #     def activity(self):
# # #         from helper_functions import ActiveTabs

# # #         ActiveTabs(self)  # Pass self to update instance variables
# # #         if self.activity_recursion and self.running:
# # #             self.schedule_task('activity', self.activity, 15000)

# # #     def take_screenshot(self):
# # #         from helper_functions import ActiveTabs

# # #         if self.recursion and self.running:
# # #             ActiveTabs(self)  # Pass self to update instance variables
# # #             try:
# # #                 screenshot = ImageGrab.grab()

# # #                 # Convert image to RGB if it has an alpha channel
# # #                 if screenshot.mode == 'RGBA':
# # #                     screenshot = screenshot.convert('RGB')

# # #                 image_stream = BytesIO()
# # #                 # Save as JPEG with quality setting
# # #                 screenshot.save(image_stream, format='JPEG', quality=40, optimize=True)
# # #                 self.image_bytes = image_stream.getvalue()

# # #                 # Print the size of the image in bytes
# # #                 image_size = len(self.image_bytes)
# # #                 # print(f"Size of the image: {image_size} bytes")

# # #                 self.schedule_task('screenshot', self.take_screenshot, 170000)
# # #             except Exception as e:
# # #                 print(f"Error taking screenshot: {e}")
# # #                 self.schedule_task('screenshot', self.take_screenshot, 170000)

# # #     def save_state(self):
# # #         from helper_functions import encrypt_data, set_permissions ,fernet_key

# # #         try:
# # #             state = {
# # #                 "elapsed_time": self.elapsed_time,
# # #                 "abs_start_time": self.abs_start_time,
# # #                 "running": self.running,
# # #                 "first_start": self.first_start  # Save first_start flag
# # #                 # Add other variables you want to save
# # #             }
# # #             with open(state_file, "wb") as f:
# # #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# # #             set_permissions(state_file)  # Set file permissions after writing
# # #             print("State saved.")
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

# # #     def load_state(self):
# # #         from helper_functions import decrypt_data,fernet_key

# # #         try:
# # #             if os.path.exists(state_file):
# # #                 with open(state_file, "rb") as f:
# # #                     encrypted_state = f.read()
# # #                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
# # #                 state = json.loads(decrypted_state)
# # #                 self.elapsed_time = state.get("elapsed_time", 0)
# # #                 self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
# # #                 self.running = state.get("running", False)
# # #                 self.first_start = state.get("first_start", True)  # Load first_start flag
                
# # #                 if self.running:
# # #                     self.pause_tracking = False  # Resume tracking if paused
# # #                     Timer.recursion = True
# # #                     Timer.activity_recursion = True
# # #                     self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
# # #                     self.activity()
# # #                     self.take_screenshot()
# # #                     self.start_tracking()

# # #                 print("State loaded.")
# # #             else:
# # #                 self.elapsed_time = 0
# # #                 self.abs_start_time = time.time()  # Default to current time if no saved state
# # #                 print("No previous state found.")
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

# # #     def update_timer(self):
# # #         if self.running:
# # #             self.elapsed_time = time.time() - self.abs_start_time
# # #             # self.save_state()

# # #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# # #         hours, minutes = divmod(minutes, 60)
# # #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# # #         self.lblTimer.config(text=time_str)

# # #         # Schedule the next update
# # #         self.schedule_task('timer_display', self.update_timer, 1000)





# # # def display_timer():
# # #     root = tk.Tk()
# # #     Timer(root)
# # #     root.mainloop()


# # # if __name__ == "__main__":
# # #     display_timer()

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
#     def __init__(self, root):
#         # Convert class variables to instance variables
#         self.recursion = False
#         self.activity_recursion = False
#         self.isclicked = "false"
#         self.imagepath = ""
#         self.bearer_token = ""
#         self.user_id = ""
#         self.current_time = ""
#         self.current_tab = ""
#         self.ispressed = "false"
#         self.image_bytes = b""
#         self.employee_status = 0
        
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
#         self.first_start = True  # Flag to track if it's the first start
#         self.scheduled_tasks = {}  # Track all scheduled callbacks for proper cleanup

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

#         # Register this timer instance with the key logger
#         from key_logger import set_timer_instance
#         set_timer_instance(self)

#         self.pusing_eventActivity()
#         self.posting_clicks()
#         self.start_autosave()  # Start auto-save scheduler

#         self.update_timer()

#     def schedule_task(self, task_name, callback, interval):
#         """Schedule a task with proper tracking and cancellation"""
#         # Cancel existing task if any
#         self.cancel_task(task_name)
        
#         # Schedule new task and store the ID
#         task_id = self.root.after(interval, callback)
#         self.scheduled_tasks[task_name] = task_id
#         return task_id
    
#     def cancel_task(self, task_name):
#         """Cancel a specific scheduled task"""
#         if task_name in self.scheduled_tasks:
#             try:
#                 self.root.after_cancel(self.scheduled_tasks[task_name])
#             except:
#                 pass  # Task might already be executed
#             del self.scheduled_tasks[task_name]
    
#     def cancel_all_tasks(self):
#         """Cancel all scheduled tasks"""
#         for task_name in list(self.scheduled_tasks.keys()):
#             self.cancel_task(task_name)
    
#     def start_autosave(self):
#         """Start auto-save scheduler - saves every 60 seconds"""
#         self.schedule_task('autosave', self.auto_save_state, 60000)  # Every 60 seconds
    
#     def auto_save_state(self):
#         """Auto-save timer state in background"""
#         if self.running:
#             # Save in background thread to avoid blocking UI
#             threading.Thread(target=self.save_state, daemon=True).start()
        
#         # Reschedule next auto-save
#         self.schedule_task('autosave', self.auto_save_state, 60000)

#     def start_timer(self):
#         if not self.running:
#             self.running = True
#             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
#             self.pause_tracking = False  # Resume tracking if paused

#             # If it's not the first start (i.e., resuming from pause), call stop_break
#             if not self.first_start:
#                 # Run in background thread to avoid blocking UI
#                 threading.Thread(target=self._stop_break_worker, daemon=True).start()
            
#             # Set first_start to False after the first start
#             self.first_start = False

#             self.recursion = True
#             self.activity_recursion = True
#             self.activity()
#             self.take_screenshot()
#             self.start_tracking()
            
#             # Save state immediately when timer starts
#             self.save_state()
    
#     def _stop_break_worker(self):
#         """Background worker for stop_break - doesn't block UI"""
#         try:
#             from api_services import stop_break
#             stop_break(self.user_id, self.bearer_token)
#             print("Break stopped - Resuming work")
#         except Exception as e:
#             print(f"Error stopping break: {e}")

#     def pusing_eventActivity(self):
#         if self.running:
#             # Run API call in background thread to avoid blocking UI
#             threading.Thread(target=self._pusing_eventActivity_worker, daemon=True).start()
#         else:
#             print("event Activity not pushed")
        
#         self.schedule_task('event_activity', self.pusing_eventActivity, 17000)
    
#     def _pusing_eventActivity_worker(self):
#         """Background worker for event activity - doesn't block UI"""
#         try:
#             from api_services import event_activity
            
#             print("event Activity Pushed")
#             print(self.isclicked)      
#             print(self.ispressed)
#             print(self.employee_status)
#             print(self.current_tab)
#             print(round(self.elapsed_time))
#             print(self.user_id)
#             print(self.bearer_token)
      
#             event_activity(mouseclick=self.isclicked,
#                            keystroke=self.ispressed,
#                            employeeStatus=self.employee_status,
#                            activeTab=self.current_tab,
#                            hoursPassed=round(self.elapsed_time),
#                            shiftstatus="working",
#                            user_id=self.user_id,
#                            bearer_token=self.bearer_token,
#                            timer_instance=self)  # Pass self to update flags
#         except Exception as e:
#             print(f"Error in event activity: {e}")

#     def posting_clicks(self):
#         if self.running:
#             # Run API call in background thread to avoid blocking UI
#             threading.Thread(target=self._posting_clicks_worker, daemon=True).start()
#         else:
#             print("Clicks not Posted")
        
#         self.schedule_task('post_clicks', self.posting_clicks, 175000)
    
#     def _posting_clicks_worker(self):
#         """Background worker for posting clicks - doesn't block UI"""
#         try:
#             from api_services import post_clicks
            
#             print(self.running)
#             print("Clicks Posted")
#             post_clicks(
#                 imagepath=self.image_bytes,
#                 activeTab=self.current_tab,
#                 shiftStatus="working",
#                 user_id=self.user_id,
#                 bearer_token=self.bearer_token)
#             # print(self.image_bytes)
#             print(self.current_tab)
#             print(self.user_id)
#         except Exception as e:
#             print(f"Error in posting clicks: {e}")
    
#     def stop_timer(self):
#         if self.running:
#             self.running = False
#             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
#             # Call start_break when pausing - run in background thread
#             threading.Thread(target=self._start_break_worker, daemon=True).start()
            
#             # Cancel tasks that should stop when paused
#             self.cancel_task('activity')
#             self.cancel_task('screenshot')
            
#             # Save state immediately when paused
#             self.save_state()
            
#             if self.is_tracking:
#                 self.pause_tracking = True  # Pause tracking
#                 self.recursion = False
#                 self.activity_recursion = False
    
#     def _start_break_worker(self):
#         """Background worker for start_break - doesn't block UI"""
#         try:
#             from api_services import start_break
#             start_break(self.user_id, self.bearer_token)
#             print("Break started - Timer paused")
#         except Exception as e:
#             print(f"Error starting break: {e}")

#     def end_shift(self):
#         from helper_functions import encrypt_data, set_permissions, fernet_key
#         self.stop_timer()
#         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
#         if confirmation:
#             messagebox.showinfo("Shift Ended", "Shift has ended.")
            
#             # Reset state completely - clear credentials
#             state = {
#                 "elapsed_time": 0,
#                 "abs_start_time": 0,
#                 "running": False,
#                 "first_start": True,
#                 "bearer_token": "",  # Clear credentials
#                 "user_id": "",       # Clear user_id
#                 "last_saved": time.time()
#             }
#             with open(state_file, "wb") as f:
#                 f.write(encrypt_data(json.dumps(state), fernet_key))
#             set_permissions(state_file)  # Set file permissions after writing
            
#             # Run checkout in background thread
#             threading.Thread(target=self._checkout_worker, daemon=True).start()
            
#             print("State reset and credentials cleared.")
            
#             # Reset instance variables including credentials
#             self.elapsed_time = 0
#             self.abs_start_time = time.time()
#             self.first_start = True
#             self.running = False
#             self.bearer_token = ""
#             self.user_id = ""
#         else:
#             self.start_timer()
    
#     def _checkout_worker(self):
#         """Background worker for checkout - doesn't block UI"""
#         try:
#             from api_services import checkout
#             checkout(self.user_id, self.bearer_token)
#         except Exception as e:
#             print(f"Error in checkout: {e}")

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
#                 self.isclicked = "true"
#                 self.employee_status = 1

#     def activity(self):
#         from helper_functions import ActiveTabs

#         ActiveTabs(self)  # Pass self to update instance variables
#         if self.activity_recursion and self.running:
#             self.schedule_task('activity', self.activity, 15000)

#     def take_screenshot(self):
#         from helper_functions import ActiveTabs

#         if self.recursion and self.running:
#             ActiveTabs(self)  # Pass self to update instance variables
#             try:
#                 screenshot = ImageGrab.grab()

#                 # Convert image to RGB if it has an alpha channel
#                 if screenshot.mode == 'RGBA':
#                     screenshot = screenshot.convert('RGB')

#                 image_stream = BytesIO()
#                 # Save as JPEG with quality setting
#                 screenshot.save(image_stream, format='JPEG', quality=5)
#                 self.image_bytes = image_stream.getvalue()

#                 # Print the size of the image in bytes
#                 image_size = len(self.image_bytes)
#                 # print(f"Size of the image: {image_size} bytes")

#                 self.schedule_task('screenshot', self.take_screenshot, 175000)
#             except Exception as e:
#                 print(f"Error taking screenshot: {e}")
#                 self.schedule_task('screenshot', self.take_screenshot, 175000)

#     def save_state(self):
#         from helper_functions import encrypt_data, set_permissions, fernet_key

#         try:
#             state = {
#                 "elapsed_time": self.elapsed_time,
#                 "abs_start_time": self.abs_start_time,
#                 "running": self.running,
#                 "first_start": self.first_start,
#                 "bearer_token": self.bearer_token,  # Save credentials for session continuity
#                 "user_id": self.user_id,            # Save user_id for API calls
#                 "last_saved": time.time()           # Timestamp for debugging
#             }
#             with open(state_file, "wb") as f:
#                 f.write(encrypt_data(json.dumps(state), fernet_key))
#             set_permissions(state_file)  # Set file permissions after writing
#             print(f"State saved at {time.strftime('%H:%M:%S')}")
#         except Exception as e:
#             print(f"Error saving state: {str(e)}")

#     def load_state(self):
#         from helper_functions import decrypt_data, fernet_key

#         try:
#             if os.path.exists(state_file):
#                 with open(state_file, "rb") as f:
#                     encrypted_state = f.read()
#                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
#                 state = json.loads(decrypted_state)
                
#                 saved_elapsed = state.get("elapsed_time", 0)
#                 saved_running = state.get("running", False)
#                 saved_token = state.get("bearer_token", "")
#                 saved_user_id = state.get("user_id", "")
                
#                 # Check if there's a previous session to recover
#                 if saved_elapsed > 0 and saved_token and saved_user_id:
#                     # Format time for display
#                     hours = int(saved_elapsed // 3600)
#                     minutes = int((saved_elapsed % 3600) // 60)
#                     seconds = int(saved_elapsed % 60)
#                     time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    
#                     # Ask user if they want to resume
#                     resume = messagebox.askyesno(
#                         "Resume Timer?",
#                         f"Your timer was {'running' if saved_running else 'paused'} at {time_str} when the app closed.\n\n"
#                         f"Do you want to resume from where you left off?"
#                     )
                    
#                     if resume:
#                         # Restore timer state AND credentials
#                         self.elapsed_time = saved_elapsed
#                         self.abs_start_time = time.time() - self.elapsed_time
#                         self.running = saved_running
#                         self.first_start = state.get("first_start", False)
#                         self.bearer_token = saved_token       # Restore credentials
#                         self.user_id = saved_user_id          # Restore user_id
                        
#                         if self.running:
#                             # Resume everything if it was running
#                             self.pause_tracking = False
#                             self.recursion = True
#                             self.activity_recursion = True
#                             self.activity()
#                             self.take_screenshot()
#                             self.start_tracking()
                        
#                         print(f"State restored: {time_str} with credentials")
#                         return True  # Signal that session was resumed
#                     else:
#                         # User chose not to resume - start fresh
#                         self.elapsed_time = 0
#                         self.abs_start_time = time.time()
#                         self.running = False
#                         self.first_start = True
#                         self.bearer_token = ""
#                         self.user_id = ""
#                         print("User chose to start fresh")
#                         return False  # Signal that new login is needed
#                 else:
#                     # No previous session or already reset
#                     self.elapsed_time = 0
#                     self.abs_start_time = time.time()
#                     self.first_start = True
#                     print("No previous session found")
#                     return False  # Signal that new login is needed
#             else:
#                 # No state file exists
#                 self.elapsed_time = 0
#                 self.abs_start_time = time.time()
#                 print("No state file found - fresh start")
#                 return False  # Signal that new login is needed
#         except Exception as e:
#             print(f"Error loading state: {str(e)}")
#             # On error, start fresh
#             self.elapsed_time = 0
#             self.abs_start_time = time.time()
#             return False  # Signal that new login is needed

#     def update_timer(self):
#         if self.running:
#             self.elapsed_time = time.time() - self.abs_start_time
#             # self.save_state()

#         minutes, seconds = divmod(int(self.elapsed_time), 60)
#         hours, minutes = divmod(minutes, 60)
#         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
#         self.lblTimer.config(text=time_str)

#         # Schedule the next update
#         self.schedule_task('timer_display', self.update_timer, 1000)





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
from tkinter import messagebox, ttk
from PIL import Image, ImageGrab, ImageTk
from io import BytesIO
from pynput.mouse import Listener

# Set TK_SILENCE_DEPRECATION to suppress the warning
os.environ["TK_SILENCE_DEPRECATION"] = "1"
state_file = "program.json"
system_platform = platform.system()


class Timer:
    def __init__(self, root):
        # Instance variables
        self.recursion = False
        self.activity_recursion = False
        self.isclicked = "false"
        self.imagepath = ""
        self.bearer_token = ""
        self.user_id = ""
        self.current_time = ""
        self.current_tab = ""
        self.ispressed = "false"
        self.image_bytes = b""
        self.employee_status = 0
        
        self.root = root
        self.root.title("Mudeer")
        
        # Match login screen colors
        self.bg_color = "#ffffff"
        self.primary_color = "#234297"
        self.text_color = "#111827"
        self.label_color = "#6b7280"
        self.success_color = "#10b981"
        self.warning_color = "#f59e0b"
        self.danger_color = "#dc2626"
        self.border_color = "#e5e7eb"
        
        self.root.configure(bg=self.bg_color)
        
        # MATCH LOGIN SIZE EXACTLY!
        window_width = 420
        window_height = 520
        x_position = (root.winfo_screenwidth() - window_width) // 2
        y_position = (root.winfo_screenheight() - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        root.resizable(False, False)

        self.time = 0
        self.running = False
        self.abs_start_time = time.time()
        self.elapsed_time = 0
        self.is_tracking = False
        self.tracking_thread = None
        self.pause_tracking = False
        self.clickArray = []
        self.first_start = True
        self.scheduled_tasks = {}

        self.setup_modern_ui()
        self.load_state()

        from key_logger import set_timer_instance
        set_timer_instance(self)

        self.pusing_eventActivity()
        self.posting_clicks()
        self.start_autosave()
        self.update_timer()
    
    def setup_modern_ui(self):
        """Setup modern UI matching login screen design"""
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Button styles matching login - ALL SAME WIDTH!
        style.configure('Primary.TButton',
                       background=self.primary_color,
                       foreground='white',
                       borderwidth=0,
                       font=('Helvetica', 11, 'bold'),
                       padding=(15, 10),
                       width=12)
        style.map('Primary.TButton',
                 background=[('active', '#1d3e7a')])
        
        # Red button for End Shift
        style.configure('Danger.TButton',
                       background='#dc2626',
                       foreground='white',
                       borderwidth=0,
                       font=('Helvetica', 11, 'bold'),
                       padding=(15, 10),
                       width=12)
        style.map('Danger.TButton',
                 background=[('active', '#b91c1c')])
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=30, pady=25)
        
        # Logo/Title section
        header_frame = tk.Frame(main_frame, bg=self.bg_color)
        header_frame.pack(pady=(10, 20))
        
        try:
            # Try to load logo - SAME SIZE AS LOGIN (80x80)!
            if os.path.exists("Logo.png"):
                logo_image = Image.open("Logo.png")
                logo_image = logo_image.resize((80, 80), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_image)
                
                logo_label = tk.Label(
                    header_frame,
                    image=self.logo_photo,
                    bg=self.bg_color
                )
                logo_label.pack()
                print("✅ Logo loaded in timer!")
            else:
                # Fallback to text
                title_label = tk.Label(
                    header_frame,
                    text="مدير",
                    font=("Helvetica", 24, "bold"),
                    bg=self.bg_color,
                    fg=self.text_color
                )
                title_label.pack()
        except Exception as e:
            print(f"⚠️ Error loading logo in timer: {e}")
            title_label = tk.Label(
                header_frame,
                text="مدير",
                font=("Helvetica", 24, "bold"),
                bg=self.bg_color,
                fg=self.text_color
            )
            title_label.pack()
        
        # Timer display
        timer_frame = tk.Frame(main_frame, bg=self.bg_color)
        timer_frame.pack(pady=(0, 20))
        
        self.lblTimer = tk.Label(
            timer_frame,
            text="00:00:00",
            font=("Helvetica", 52, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.lblTimer.pack()
        
        # Status indicator
        self.status_label = tk.Label(
            timer_frame,
            text="● Ready",
            font=("Helvetica", 10),
            bg=self.bg_color,
            fg=self.label_color
        )
        self.status_label.pack(pady=(5, 0))
        
        # Buttons - WITH ICONS, ALL SAME SIZE!
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(pady=(15, 15))
        
        self.btnStart = ttk.Button(
            button_frame,
            text="▶️ Start",
            command=self.start_timer,
            style='Primary.TButton'
        )
        self.btnStart.pack(side=tk.LEFT, padx=5)
        
        self.btnPause = ttk.Button(
            button_frame,
            text="⏸️ Pause",
            command=self.stop_timer,
            style='Primary.TButton'
        )
        self.btnPause.pack(side=tk.LEFT, padx=5)
        
        self.btnEndShift = ttk.Button(
            button_frame,
            text="⬜ End Shift",
            command=self.end_shift,
            style='Danger.TButton'
        )
        self.btnEndShift.pack(side=tk.LEFT, padx=5)
        
        # Info section
        info_frame = tk.Frame(main_frame, bg=self.bg_color)
        info_frame.pack(pady=(10, 0), fill=tk.X)
        
        # Current activity
        self.activity_label = tk.Label(
            info_frame,
            text="",
            font=("Helvetica", 9),
            bg=self.bg_color,
            fg=self.label_color,
            wraplength=400
        )
        self.activity_label.pack()

    def schedule_task(self, task_name, callback, interval):
        """Schedule a task with proper tracking and cancellation"""
        self.cancel_task(task_name)
        task_id = self.root.after(interval, callback)
        self.scheduled_tasks[task_name] = task_id
        return task_id
    
    def cancel_task(self, task_name):
        """Cancel a specific scheduled task"""
        if task_name in self.scheduled_tasks:
            try:
                self.root.after_cancel(self.scheduled_tasks[task_name])
            except:
                pass
            del self.scheduled_tasks[task_name]
    
    def cancel_all_tasks(self):
        """Cancel all scheduled tasks"""
        for task_name in list(self.scheduled_tasks.keys()):
            self.cancel_task(task_name)
    
    def start_autosave(self):
        """Start auto-save scheduler - saves every 60 seconds"""
        self.schedule_task('autosave', self.auto_save_state, 60000)
    
    def auto_save_state(self):
        """Auto-save timer state in background"""
        if self.running:
            threading.Thread(target=self.save_state, daemon=True).start()
        self.schedule_task('autosave', self.auto_save_state, 60000)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.abs_start_time = time.time() - self.elapsed_time
            self.pause_tracking = False

            if not self.first_start:
                threading.Thread(target=self._stop_break_worker, daemon=True).start()
            
            self.first_start = False
            self.recursion = True
            self.activity_recursion = True
            self.activity()
            self.take_screenshot()
            self.start_tracking()
            self.save_state()
    
    def _stop_break_worker(self):
        """Background worker for stop_break - doesn't block UI"""
        try:
            from api_services import stop_break
            stop_break(self.user_id, self.bearer_token)
            print("Break stopped - Resuming work")
        except Exception as e:
            print(f"Error stopping break: {e}")

    def pusing_eventActivity(self):
        if self.running:
            threading.Thread(target=self._pusing_eventActivity_worker, daemon=True).start()
        else:
            print("event Activity not pushed")
        self.schedule_task('event_activity', self.pusing_eventActivity, 17000)
    
    def _pusing_eventActivity_worker(self):
        """Background worker for event activity - doesn't block UI"""
        try:
            from api_services import event_activity
            print("event Activity Pushed")
            event_activity(mouseclick=self.isclicked,
                          keystroke=self.ispressed,
                          employeeStatus=self.employee_status,
                          activeTab=self.current_tab,
                          hoursPassed=round(self.elapsed_time),
                          shiftstatus="working",
                          user_id=self.user_id,
                          bearer_token=self.bearer_token,
                          timer_instance=self)
        except Exception as e:
            print(f"Error in event activity: {e}")

    def posting_clicks(self):
        if self.running:
            threading.Thread(target=self._posting_clicks_worker, daemon=True).start()
        else:
            print("Clicks not Posted")
        self.schedule_task('post_clicks', self.posting_clicks, 175000)
    
    def _posting_clicks_worker(self):
        """Background worker for posting clicks - doesn't block UI"""
        try:
            from api_services import post_clicks
            print("Clicks Posted")
            post_clicks(
                imagepath=self.image_bytes,
                activeTab=self.current_tab,
                shiftStatus="working",
                user_id=self.user_id,
                bearer_token=self.bearer_token)
        except Exception as e:
            print(f"Error in posting clicks: {e}")
    
    def stop_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.abs_start_time
            threading.Thread(target=self._start_break_worker, daemon=True).start()
            self.cancel_task('activity')
            self.cancel_task('screenshot')
            self.save_state()
            if self.is_tracking:
                self.pause_tracking = True
                self.recursion = False
                self.activity_recursion = False
    
    def _start_break_worker(self):
        """Background worker for start_break - doesn't block UI"""
        try:
            from api_services import start_break
            start_break(self.user_id, self.bearer_token)
            print("Break started - Timer paused")
        except Exception as e:
            print(f"Error starting break: {e}")

    def end_shift(self):
        from helper_functions import encrypt_data, set_permissions, fernet_key
        self.stop_timer()
        confirmation = messagebox.askyesno("End Shift", "Are you sure your work hours are completed?")
        if confirmation:
            messagebox.showinfo("Shift Ended", "Shift has ended.")
            state = {
                "elapsed_time": 0,
                "abs_start_time": 0,
                "running": False,
                "first_start": True,
                "bearer_token": "",
                "user_id": "",
                "last_saved": time.time()
            }
            with open(state_file, "wb") as f:
                f.write(encrypt_data(json.dumps(state), fernet_key))
            set_permissions(state_file)
            threading.Thread(target=self._checkout_worker, daemon=True).start()
            self.elapsed_time = 0
            self.abs_start_time = time.time()
            self.first_start = True
            self.running = False
            self.bearer_token = ""
            self.user_id = ""
        else:
            self.start_timer()
    
    def _checkout_worker(self):
        """Background worker for checkout - doesn't block UI"""
        try:
            from api_services import checkout
            checkout(self.user_id, self.bearer_token)
        except Exception as e:
            print(f"Error in checkout: {e}")

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
                self.isclicked = "true"
                self.employee_status = 1

    def activity(self):
        from helper_functions import ActiveTabs
        ActiveTabs(self)
        if self.activity_recursion and self.running:
            self.schedule_task('activity', self.activity, 15000)

    def take_screenshot(self):
        from helper_functions import ActiveTabs
        if self.recursion and self.running:
            ActiveTabs(self)
            try:
                screenshot = ImageGrab.grab()
                if screenshot.mode == 'RGBA':
                    screenshot = screenshot.convert('RGB')
                image_stream = BytesIO()
                screenshot.save(image_stream, format='JPEG', quality=5)
                self.image_bytes = image_stream.getvalue()
                self.schedule_task('screenshot', self.take_screenshot, 175000)
            except Exception as e:
                print(f"Error taking screenshot: {e}")
                self.schedule_task('screenshot', self.take_screenshot, 175000)

    def save_state(self):
        from helper_functions import encrypt_data, set_permissions, fernet_key
        try:
            state = {
                "elapsed_time": self.elapsed_time,
                "abs_start_time": self.abs_start_time,
                "running": self.running,
                "first_start": self.first_start,
                "bearer_token": self.bearer_token,
                "user_id": self.user_id,
                "last_saved": time.time()
            }
            with open(state_file, "wb") as f:
                f.write(encrypt_data(json.dumps(state), fernet_key))
            set_permissions(state_file)
            print(f"State saved at {time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"Error saving state: {str(e)}")

    def load_state(self):
        from helper_functions import decrypt_data, fernet_key
        try:
            if os.path.exists(state_file):
                with open(state_file, "rb") as f:
                    encrypted_state = f.read()
                decrypted_state = decrypt_data(encrypted_state, fernet_key)
                state = json.loads(decrypted_state)
                
                saved_elapsed = state.get("elapsed_time", 0)
                saved_running = state.get("running", False)
                saved_token = state.get("bearer_token", "")
                saved_user_id = state.get("user_id", "")
                
                if saved_elapsed > 0 and saved_token and saved_user_id:
                    hours = int(saved_elapsed // 3600)
                    minutes = int((saved_elapsed % 3600) // 60)
                    seconds = int(saved_elapsed % 60)
                    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    
                    resume = messagebox.askyesno(
                        "Resume Timer?",
                        f"Your timer was {'running' if saved_running else 'paused'} at {time_str}.\n\n"
                        f"Resume from where you left off?"
                    )
                    
                    if resume:
                        self.elapsed_time = saved_elapsed
                        self.abs_start_time = time.time() - self.elapsed_time
                        self.running = saved_running
                        self.first_start = state.get("first_start", False)
                        self.bearer_token = saved_token
                        self.user_id = saved_user_id
                        
                        if self.running:
                            self.pause_tracking = False
                            self.recursion = True
                            self.activity_recursion = True
                            self.activity()
                            self.take_screenshot()
                            self.start_tracking()
                        
                        print(f"State restored: {time_str}")
                        return True
                    else:
                        self.elapsed_time = 0
                        self.abs_start_time = time.time()
                        self.running = False
                        self.first_start = True
                        return False
                else:
                    self.elapsed_time = 0
                    self.abs_start_time = time.time()
                    self.first_start = True
                    return False
            else:
                self.elapsed_time = 0
                self.abs_start_time = time.time()
                return False
        except Exception as e:
            print(f"Error loading state: {str(e)}")
            self.elapsed_time = 0
            self.abs_start_time = time.time()
            return False

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.abs_start_time

        minutes, seconds = divmod(int(self.elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        self.lblTimer.config(text=time_str)
        
        # Keep timer text black like login - no color changes!
        self.lblTimer.config(fg=self.text_color)  # Always black
        
        # Update status subtly
        if self.running:
            self.status_label.config(text="● Working", fg=self.success_color)
        else:
            self.status_label.config(text="● Paused", fg=self.label_color)  # Gray, not orange!

        self.schedule_task('timer_display', self.update_timer, 1000)


def display_timer():
    root = tk.Tk()
    Timer(root)
    root.mainloop()


if __name__ == "__main__":
    display_timer()