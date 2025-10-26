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
# # #     recursion = False
# # #     activity_recursion = False
# # #     isclicked = "false"
# # #     imagepath = ""
# # #     bearer_token = ""
# # #     User_id = ""
# # #     CurrentTime = ""
# # #     CurrentTab = ""
# # #     ispressed = "false"
# # #     image_bytes=""
# # #     employeeStatus = 0

# # #     def __init__(self, root):
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

# # #         # self.pusing_eventActivity()
# # #         self.posting_clicks()

# # #         self.update_timer()

# # #     def start_timer(self):
# # #         if not self.running:
# # #             self.running = True
# # #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# # #             self.pause_tracking = False  # Resume tracking if paused

# # #             Timer.recursion = True
# # #             Timer.activity_recursion = True
# # #             self.activity()
# # #             self.take_screenshot()
# # #             self.start_tracking()

# # #     def pusing_eventActivity(self):
# # #         from api_services import event_activity
# # #         # print(self.running)
# # #         if self.running:
# # #             print("event Activity Pushed")
            
# # #             print(Timer.isclicked)      
# # #             print(Timer.ispressed)
# # #             print(Timer.employeeStatus)
# # #             print(Timer.CurrentTab)
# # #             print(round(self.elapsed_time))
# # #             print(Timer.User_id)
# # #             print(Timer.bearer_token)
      
# # #             event_activity(mouseclick=Timer.isclicked,
# # #                            keystroke=Timer.ispressed,
# # #                            employeeStatus=Timer.employeeStatus,
# # #                            activeTab=Timer.CurrentTab,
# # #                            hoursPassed=round(self.elapsed_time),
# # #                            shiftstatus="working",
# # #                            user_id=Timer.User_id,
# # #                            bearer_token=Timer.bearer_token,)

# # #         print("event Activity not pushed")
# # #         self.root.after(17000, self.pusing_eventActivity)

# # #     def posting_clicks(self):
# # #         from api_services import post_clicks

# # #         print(self.running)
# # #         if self.running:
# # #             print("Clicks Posted")
# # #             post_clicks(
# # #                 imagepath=Timer.image_bytes,
# # #                 activeTab=Timer.CurrentTab,
# # #                 shiftStatus="working",
# # #                 user_id=Timer.User_id)
# # #             # print(Timer.image_bytes)
# # #             print(Timer.CurrentTab)
# # #             print(Timer.User_id)

# # #         print("Clicks not Posted")
# # #         self.root.after(10000, self.posting_clicks)

# # #     def stop_timer(self):
# # #         if self.running:
# # #             self.running = False
# # #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
# # #             # self.save_state()
# # #             if self.is_tracking:
# # #                 self.pause_tracking = True  # Pause tracking
# # #                 Timer.recursion = False
# # #                 Timer.activity_recursion = False

# # #     def end_shift(self):
# # #         from helper_functions import encrypt_data, set_permissions ,fernet_key
# # #         from api_services import checkout
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
# # #             checkout(Timer.User_id);
# # #             print("State saved.")
# # #         else:
# # #             self.start_timer()

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
# # #                 Timer.isclicked = "true"
# # #                 Timer.employeeStatus = 1

# # #     def activity(self):
# # #         from helper_functions import ActiveTabs

# # #         ActiveTabs()
# # #         if self.activity_recursion and self.running:
# # #             self.root.after(15000, self.activity)

# # #     def take_screenshot(self):
# # #         from helper_functions import ActiveTabs

# # #         if Timer.recursion and self.running:
# # #             ActiveTabs()
# # #             try:
# # #                 screenshot = ImageGrab.grab()

# # #                 # Convert image to RGB if it has an alpha channel
# # #                 if screenshot.mode == 'RGBA':
# # #                     screenshot = screenshot.convert('RGB')

# # #                 image_stream = BytesIO()
# # #                 # Save as JPEG with quality setting
# # #                 screenshot.save(image_stream, format='JPEG', quality=5)
# # #                 Timer.image_bytes = image_stream.getvalue()

# # #                 # Print the size of the image in bytes
# # #                 image_size = len(Timer.image_bytes)
# # #                 # print(f"Size of the image: {image_size} bytes")

# # #                 self.root.after(175000, self.take_screenshot)
# # #             except Exception as e:
# # #                 print(f"Error taking screenshot: {e}")
# # #                 self.root.after(175000, self.take_screenshot)

# # #     def save_state(self):
# # #         from helper_functions import encrypt_data, set_permissions ,fernet_key

# # #         try:
# # #             state = {
# # #                 "elapsed_time": self.elapsed_time,
# # #                 "abs_start_time": self.abs_start_time,
# # #                 "running": self.running
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
# # #         self.root.after(1000, self.update_timer)





# # # def display_timer():
# # #     root = tk.Tk()
# # #     Timer(root)
# # #     root.mainloop()


# # # if __name__ == "__main__":
# # #     display_timer()


# # import json
# # import os
# # import platform
# # import tkinter as tk
# # import threading
# # import time
# # from tkinter import messagebox
# # from PIL import Image, ImageGrab
# # from io import BytesIO
# # from pynput.mouse import Listener
# # from cryptography.fernet import Fernet





# # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # state_file = "program.json"
# # system_platform = platform.system()


# # class Timer:
# #     recursion = False
# #     activity_recursion = False
# #     isclicked = "false"
# #     imagepath = ""
# #     bearer_token = ""
# #     User_id = ""
# #     CurrentTime = ""
# #     CurrentTab = ""
# #     ispressed = "false"
# #     image_bytes=""
# #     employeeStatus = 0

# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Mudeer")
# #         window_width = 600
# #         window_height = 300
# #         x_position = (root.winfo_screenwidth() - window_width) // 2
# #         y_position = (root.winfo_screenheight() - window_height) // 2
# #         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Corrected line

# #         self.time = 0
# #         self.running = False
# #         self.abs_start_time = time.time()  # Absolute start time of the timer
# #         self.elapsed_time = 0
# #         self.is_tracking = False
# #         self.tracking_thread = None
# #         self.pause_tracking = False  # Flag to indicate tracking should pause
# #         self.clickArray = []
# #         self.first_start = True  # Flag to track if it's the first start

# #         rootFrame = tk.Frame(root, pady=10, padx=10)
# #         rootFrame.pack(expand=True)

# #         lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
# #         lblTitle.pack(pady=(0, 10))

# #         MainFrame = tk.Frame(root, pady=10, padx=10)
# #         MainFrame.pack(expand=True)

# #         MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
# #         MainFrameTop.pack()

# #         MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
# #         MainFrameDown.pack()

# #         self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
# #         self.lblTimer.pack(pady=10)

# #         self.btnStart = tk.Button(
# #             MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
# #             command=self.start_timer
# #         )
# #         self.btnStart.pack(side=tk.LEFT, padx=10)

# #         self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# #                                  command=self.stop_timer)
# #         self.btnStop.pack(side=tk.LEFT, padx=10)

# #         self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# #                                  command=self.end_shift)
# #         self.btnStop.pack(side=tk.LEFT, padx=10)

# #         self.load_state()  # Load saved state when initializing]

# #         self.pusing_eventActivity()
# #         self.posting_clicks()

# #         self.update_timer()

# #     def start_timer(self):
# #         if not self.running:
# #             self.running = True
# #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# #             self.pause_tracking = False  # Resume tracking if paused

# #             # If it's not the first start (i.e., resuming from pause), call stop_break
# #             if not self.first_start:
# #                 from api_services import stop_break
# #                 stop_break(Timer.User_id)
# #                 print("Break stopped - Resuming work")
            
# #             # Set first_start to False after the first start
# #             self.first_start = False

# #             Timer.recursion = True
# #             Timer.activity_recursion = True
# #             self.activity()
# #             self.take_screenshot()
# #             self.start_tracking()

# #     def pusing_eventActivity(self):
# #         from api_services import event_activity
# #         # print(self.running)
# #         if self.running:
# #             print("event Activity Pushed")
            
# #             print(Timer.isclicked)      
# #             print(Timer.ispressed)
# #             print(Timer.employeeStatus)
# #             print(Timer.CurrentTab)
# #             print(round(self.elapsed_time))
# #             print(Timer.User_id)
# #             print(Timer.bearer_token)
      
# #             event_activity(mouseclick=Timer.isclicked,
# #                            keystroke=Timer.ispressed,
# #                            employeeStatus=Timer.employeeStatus,
# #                            activeTab=Timer.CurrentTab,
# #                            hoursPassed=round(self.elapsed_time),
# #                            shiftstatus="working",
# #                            user_id=Timer.User_id,
# #                            bearer_token=Timer.bearer_token,)

# #         print("event Activity not pushed")
# #         self.root.after(17000, self.pusing_eventActivity)

# #     def posting_clicks(self):
# #         from api_services import post_clicks

# #         print(self.running)
# #         if self.running:
# #             print("Clicks Posted")
# #             post_clicks(
# #                 imagepath=Timer.image_bytes,
# #                 activeTab=Timer.CurrentTab,
# #                 shiftStatus="working",
# #                 user_id=Timer.User_id)
# #             # print(Timer.image_bytes)
# #             print(Timer.CurrentTab)
# #             print(Timer.User_id)

# #         print("Clicks not Posted")
# #         self.root.after(10000, self.posting_clicks)

# #     def stop_timer(self):
# #         if self.running:
# #             self.running = False
# #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
# #             # Call start_break when pausing
# #             from api_services import start_break
# #             start_break(Timer.User_id)
# #             print("Break started - Timer paused")
            
# #             # self.save_state()
# #             if self.is_tracking:
# #                 self.pause_tracking = True  # Pause tracking
# #                 Timer.recursion = False
# #                 Timer.activity_recursion = False

# #     def end_shift(self):
# #         from helper_functions import encrypt_data, set_permissions ,fernet_key
# #         from api_services import checkout
# #         self.stop_timer()
# #         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# #         if confirmation:
# #             messagebox.showinfo("Shift Ended", "Shift has ended.")
# #             state = {
# #                 "elapsed_time": 0,
# #                 "abs_start_time": 0,
# #                 "running": False
# #             }
# #             with open(state_file, "wb") as f:
# #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# #             set_permissions(state_file)  # Set file permissions after writing
# #             checkout(Timer.User_id)
# #             print("State saved.")
            
# #             # Reset first_start flag when shift ends
# #             self.first_start = True
# #         else:
# #             self.start_timer()

# #     def start_tracking(self):
# #         if not self.is_tracking:
# #             self.tracking_thread = threading.Thread(target=self.track_mouse)
# #             self.tracking_thread.daemon = True
# #             self.tracking_thread.start()
# #             self.is_tracking = True

# #     def track_mouse(self):
# #         with Listener(on_click=self.on_click) as listener:
# #             listener.join()

# #     def on_click(self, x, y, button, pressed):
# #         if not self.pause_tracking:
# #             if pressed:
# #                 Timer.isclicked = "true"
# #                 Timer.employeeStatus = 1

# #     def activity(self):
# #         from helper_functions import ActiveTabs

# #         ActiveTabs()
# #         if self.activity_recursion and self.running:
# #             self.root.after(15000, self.activity)

# #     def take_screenshot(self):
# #         from helper_functions import ActiveTabs

# #         if Timer.recursion and self.running:
# #             ActiveTabs()
# #             try:
# #                 screenshot = ImageGrab.grab()

# #                 # Convert image to RGB if it has an alpha channel
# #                 if screenshot.mode == 'RGBA':
# #                     screenshot = screenshot.convert('RGB')

# #                 image_stream = BytesIO()
# #                 # Save as JPEG with quality setting
# #                 screenshot.save(image_stream, format='JPEG', quality=5)
# #                 Timer.image_bytes = image_stream.getvalue()

# #                 # Print the size of the image in bytes
# #                 image_size = len(Timer.image_bytes)
# #                 # print(f"Size of the image: {image_size} bytes")

# #                 self.root.after(175000, self.take_screenshot)
# #             except Exception as e:
# #                 print(f"Error taking screenshot: {e}")
# #                 self.root.after(175000, self.take_screenshot)

# #     def save_state(self):
# #         from helper_functions import encrypt_data, set_permissions ,fernet_key

# #         try:
# #             state = {
# #                 "elapsed_time": self.elapsed_time,
# #                 "abs_start_time": self.abs_start_time,
# #                 "running": self.running,
# #                 "first_start": self.first_start  # Save first_start flag
# #                 # Add other variables you want to save
# #             }
# #             with open(state_file, "wb") as f:
# #                 f.write(encrypt_data(json.dumps(state), fernet_key))
# #             set_permissions(state_file)  # Set file permissions after writing
# #             print("State saved.")
# #         except Exception as e:
# #             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

# #     def load_state(self):
# #         from helper_functions import decrypt_data,fernet_key

# #         try:
# #             if os.path.exists(state_file):
# #                 with open(state_file, "rb") as f:
# #                     encrypted_state = f.read()
# #                 decrypted_state = decrypt_data(encrypted_state, fernet_key)
# #                 state = json.loads(decrypted_state)
# #                 self.elapsed_time = state.get("elapsed_time", 0)
# #                 self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
# #                 self.running = state.get("running", False)
# #                 self.first_start = state.get("first_start", True)  # Load first_start flag
                
# #                 if self.running:
# #                     self.pause_tracking = False  # Resume tracking if paused
# #                     Timer.recursion = True
# #                     Timer.activity_recursion = True
# #                     self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
# #                     self.activity()
# #                     self.take_screenshot()
# #                     self.start_tracking()

# #                 print("State loaded.")
# #             else:
# #                 self.elapsed_time = 0
# #                 self.abs_start_time = time.time()  # Default to current time if no saved state
# #                 print("No previous state found.")
# #         except Exception as e:
# #             messagebox.showerror("Error", f"An error occurred while loading the state:\n{str(e)}")

# #     def update_timer(self):
# #         if self.running:
# #             self.elapsed_time = time.time() - self.abs_start_time
# #             # self.save_state()

# #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# #         hours, minutes = divmod(minutes, 60)
# #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# #         self.lblTimer.config(text=time_str)

# #         # Schedule the next update
# #         self.root.after(1000, self.update_timer)





# # def display_timer():
# #     root = tk.Tk()
# #     Timer(root)
# #     root.mainloop()


# # if __name__ == "__main__":
# #     display_timer()






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

#         self.pusing_eventActivity()
#         self.posting_clicks()

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

#             Timer.recursion = True
#             Timer.activity_recursion = True
#             self.activity()
#             self.take_screenshot()
#             self.start_tracking()
    
#     def _stop_break_worker(self):
#         """Background worker for stop_break - doesn't block UI"""
#         try:
#             from api_services import stop_break
#             stop_break(Timer.User_id)
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
#         except Exception as e:
#             print(f"Error in event activity: {e}")

#     def posting_clicks(self):
#         if self.running:
#             # Run API call in background thread to avoid blocking UI
#             threading.Thread(target=self._posting_clicks_worker, daemon=True).start()
#         else:
#             print("Clicks not Posted")
        
#         self.schedule_task('post_clicks', self.posting_clicks, 10000)
    
#     def _posting_clicks_worker(self):
#         """Background worker for posting clicks - doesn't block UI"""
#         try:
#             from api_services import post_clicks
            
#             print(self.running)
#             print("Clicks Posted")
#             post_clicks(
#                 imagepath=Timer.image_bytes,
#                 activeTab=Timer.CurrentTab,
#                 shiftStatus="working",
#                 user_id=Timer.User_id)
#             # print(Timer.image_bytes)
#             print(Timer.CurrentTab)
#             print(Timer.User_id)
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
            
#             # self.save_state()
#             if self.is_tracking:
#                 self.pause_tracking = True  # Pause tracking
#                 Timer.recursion = False
#                 Timer.activity_recursion = False
    
#     def _start_break_worker(self):
#         """Background worker for start_break - doesn't block UI"""
#         try:
#             from api_services import start_break
#             start_break(Timer.User_id)
#             print("Break started - Timer paused")
#         except Exception as e:
#             print(f"Error starting break: {e}")

#     def end_shift(self):
#         from helper_functions import encrypt_data, set_permissions ,fernet_key
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
            
#             # Run checkout in background thread
#             threading.Thread(target=self._checkout_worker, daemon=True).start()
            
#             print("State saved.")
            
#             # Reset first_start flag when shift ends
#             self.first_start = True
#         else:
#             self.start_timer()
    
#     def _checkout_worker(self):
#         """Background worker for checkout - doesn't block UI"""
#         try:
#             from api_services import checkout
#             checkout(Timer.User_id)
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
#                 Timer.isclicked = "true"
#                 Timer.employeeStatus = 1

#     def activity(self):
#         from helper_functions import ActiveTabs

#         ActiveTabs()
#         if self.activity_recursion and self.running:
#             self.schedule_task('activity', self.activity, 15000)

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

#                 self.schedule_task('screenshot', self.take_screenshot, 175000)
#             except Exception as e:
#                 print(f"Error taking screenshot: {e}")
#                 self.schedule_task('screenshot', self.take_screenshot, 175000)

#     def save_state(self):
#         from helper_functions import encrypt_data, set_permissions ,fernet_key

#         try:
#             state = {
#                 "elapsed_time": self.elapsed_time,
#                 "abs_start_time": self.abs_start_time,
#                 "running": self.running,
#                 "first_start": self.first_start  # Save first_start flag
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
#                 self.first_start = state.get("first_start", True)  # Load first_start flag
                
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
    def __init__(self, root):
        # Convert class variables to instance variables
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
        self.scheduled_tasks = {}  # Track all scheduled callbacks for proper cleanup

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

        # Register this timer instance with the key logger
        from key_logger import set_timer_instance
        set_timer_instance(self)

        self.pusing_eventActivity()
        self.posting_clicks()

        self.update_timer()

    def schedule_task(self, task_name, callback, interval):
        """Schedule a task with proper tracking and cancellation"""
        # Cancel existing task if any
        self.cancel_task(task_name)
        
        # Schedule new task and store the ID
        task_id = self.root.after(interval, callback)
        self.scheduled_tasks[task_name] = task_id
        return task_id
    
    def cancel_task(self, task_name):
        """Cancel a specific scheduled task"""
        if task_name in self.scheduled_tasks:
            try:
                self.root.after_cancel(self.scheduled_tasks[task_name])
            except:
                pass  # Task might already be executed
            del self.scheduled_tasks[task_name]
    
    def cancel_all_tasks(self):
        """Cancel all scheduled tasks"""
        for task_name in list(self.scheduled_tasks.keys()):
            self.cancel_task(task_name)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
            self.pause_tracking = False  # Resume tracking if paused

            # If it's not the first start (i.e., resuming from pause), call stop_break
            if not self.first_start:
                # Run in background thread to avoid blocking UI
                threading.Thread(target=self._stop_break_worker, daemon=True).start()
            
            # Set first_start to False after the first start
            self.first_start = False

            self.recursion = True
            self.activity_recursion = True
            self.activity()
            self.take_screenshot()
            self.start_tracking()
    
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
            # Run API call in background thread to avoid blocking UI
            threading.Thread(target=self._pusing_eventActivity_worker, daemon=True).start()
        else:
            print("event Activity not pushed")
        
        self.schedule_task('event_activity', self.pusing_eventActivity, 17000)
    
    def _pusing_eventActivity_worker(self):
        """Background worker for event activity - doesn't block UI"""
        try:
            from api_services import event_activity
            
            print("event Activity Pushed")
            print(self.isclicked)      
            print(self.ispressed)
            print(self.employee_status)
            print(self.current_tab)
            print(round(self.elapsed_time))
            print(self.user_id)
            print(self.bearer_token)
      
            event_activity(mouseclick=self.isclicked,
                           keystroke=self.ispressed,
                           employeeStatus=self.employee_status,
                           activeTab=self.current_tab,
                           hoursPassed=round(self.elapsed_time),
                           shiftstatus="working",
                           user_id=self.user_id,
                           bearer_token=self.bearer_token,
                           timer_instance=self)  # Pass self to update flags
        except Exception as e:
            print(f"Error in event activity: {e}")

    def posting_clicks(self):
        if self.running:
            # Run API call in background thread to avoid blocking UI
            threading.Thread(target=self._posting_clicks_worker, daemon=True).start()
        else:
            print("Clicks not Posted")
        
        self.schedule_task('post_clicks', self.posting_clicks, 17500)
    
    def _posting_clicks_worker(self):
        """Background worker for posting clicks - doesn't block UI"""
        try:
            from api_services import post_clicks
            
            print(self.running)
            print("Clicks Posted")
            post_clicks(
                imagepath=self.image_bytes,
                activeTab=self.current_tab,
                shiftStatus="working",
                user_id=self.user_id,
                bearer_token=self.bearer_token)
            # print(self.image_bytes)
            print(self.current_tab)
            print(self.user_id)
        except Exception as e:
            print(f"Error in posting clicks: {e}")

    def stop_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            
            # Call start_break when pausing - run in background thread
            threading.Thread(target=self._start_break_worker, daemon=True).start()
            
            # Cancel tasks that should stop when paused
            self.cancel_task('activity')
            self.cancel_task('screenshot')
            
            # self.save_state()
            if self.is_tracking:
                self.pause_tracking = True  # Pause tracking
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
        from helper_functions import encrypt_data, set_permissions ,fernet_key
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
            
            # Run checkout in background thread
            threading.Thread(target=self._checkout_worker, daemon=True).start()
            
            print("State saved.")
            
            # Reset first_start flag when shift ends
            self.first_start = True
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

        ActiveTabs(self)  # Pass self to update instance variables
        if self.activity_recursion and self.running:
            self.schedule_task('activity', self.activity, 15000)

    def take_screenshot(self):
        from helper_functions import ActiveTabs

        if self.recursion and self.running:
            ActiveTabs(self)  # Pass self to update instance variables
            try:
                screenshot = ImageGrab.grab()

                # Convert image to RGB if it has an alpha channel
                if screenshot.mode == 'RGBA':
                    screenshot = screenshot.convert('RGB')

                image_stream = BytesIO()
                # Save as JPEG with quality setting
                screenshot.save(image_stream, format='JPEG', quality=40, optimize=True)
                self.image_bytes = image_stream.getvalue()

                # Print the size of the image in bytes
                image_size = len(self.image_bytes)
                # print(f"Size of the image: {image_size} bytes")

                self.schedule_task('screenshot', self.take_screenshot, 170000)
            except Exception as e:
                print(f"Error taking screenshot: {e}")
                self.schedule_task('screenshot', self.take_screenshot, 170000)

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
        self.schedule_task('timer_display', self.update_timer, 1000)





def display_timer():
    root = tk.Tk()
    Timer(root)
    root.mainloop()


if __name__ == "__main__":
    display_timer()