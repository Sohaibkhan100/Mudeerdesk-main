
# # # import json
# # # import os
# # # import platform
# # # import sys
# # # import tkinter as tk
# # # from tkinter import PhotoImage, ttk, messagebox
# # # from PIL import Image, ImageGrab, UnidentifiedImageError
# # # from io import BytesIO
# # # import threading
# # # import time
# # # import csv
# # # import datetime
# # # from pynput.mouse import Listener
# # # import time
# # # import requests
# # # import pygetwindow as gw
# # # from pynput import keyboard

# # # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # # state_file = "app_state.json"

# # # # Determine the system platform
# # # system_platform = platform.system()

# # # def on_press(key):
# # #     try:
# # #         print(f"Key pressed: {key.char}")
# # #     except AttributeError:
# # #         print(f"Special key pressed: {key}")

# # # def generate_log():
# # #     print("Generating log...")
# # #     with keyboard.Listener(on_press=on_press) as keyboardlistener:
# # #         keyboardlistener.join()

# # # def start_logging_thread():
# # #     try:
# # #         logging_thread = threading.Thread(target=generate_log)
# # #         logging_thread.start()
# # #     except Exception as e:
# # #         print(f"Exception in start_logging_thread: {e}")

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
# # #     employeeStatus = 0
    

# # #     def __init__(self, root):
# # #         try:
# # #             self.root = root
# # #             self.root.title("Mudeer")
# # #             window_width = 600
# # #             window_height = 300
# # #             x_position = (root.winfo_screenwidth() - window_width) // 2
# # #             y_position = (root.winfo_screenheight() - window_height) // 2
# # #             root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# # #             frame = ttk.Frame(root, padding="20")
# # #             frame.pack(expand=True)

# # #             self.time = 0
# # #             self.running = False
# # #             # self.start_time = None
# # #             self.end_time = None
# # #             self.elapsed_time = 0
# # #             self.is_tracking = False
# # #             self.tracking_thread = None
# # #             self.pause_tracking = False  # Flag to indicate tracking should pause
# # #             self.clickArray = []

# # #             rootFrame = tk.Frame(root, pady=10, padx=10)
# # #             rootFrame.pack(expand=True)

# # #             lblTitle = tk.Label(rootFrame, font=('Arial', 40), text=" مدير ", justify=tk.CENTER)
# # #             lblTitle.pack(pady=(0, 10))

# # #             MainFrame = tk.Frame(root, pady=10, padx=10)
# # #             MainFrame.pack(expand=True)

# # #             MainFrameTop = tk.Frame(MainFrame, pady=10, padx=10)
# # #             MainFrameTop.pack()

# # #             MainFrameDown = tk.Frame(MainFrame, pady=10, padx=10)
# # #             MainFrameDown.pack()

# # #             self.lblTimer = tk.Label(MainFrameTop, font=('Arial', 40), text="00:00:00", width=19, justify=tk.CENTER)
# # #             self.lblTimer.pack(pady=10)

# # #             self.btnStart = tk.Button(
# # #                 MainFrameDown, text="Start", font=('Arial', 20,), bd=5, relief=tk.SOLID, width=10,
# # #                 command=self.start_timer
# # #             )
# # #             self.btnStart.pack(side=tk.LEFT, padx=10)

# # #             self.btnStop = tk.Button(MainFrameDown, text="Pause", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # #                                      command=self.stop_timer)
# # #             self.btnStop.pack(side=tk.LEFT, padx=10)

# # #             self.btnStop = tk.Button(MainFrameDown, text="End Shift", font=('Arial', 20), bd=5, relief=tk.SOLID, width=10,
# # #                                      command=self.end_shift)
# # #             self.btnStop.pack(side=tk.LEFT, padx=10)
            
            
# # #             self.load_state()

            
# # #             self.update_timer()

        
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 1", error_message)
# # #             print("1")



# #     # def start_timer(self):
# #     #     if not self.running:
# #     #         self.running = True
# #     #     if self.start_time is None:
# #     #         # Only reset start_time if it's None, otherwise keep the current value
# #     #         self.start_time = time.time() - self.elapsed_time
# #     #         print(self.start_time)
# #     #         print("start timeeeeee @ start_timer()")

# #     #     if not self.is_tracking:
# #     #         self.start_tracking()
# #     #         Timer.recursion = True
# #     #         Timer.activity_recursion = True
# #     #         self.take_screenshot()
# #     #         self.activity()
# #     #     elif self.pause_tracking:
# #     #         self.pause_tracking = False  # Resume tracking if paused
# #     #         Timer.recursion = True
# #     #         Timer.activity_recursion = True
# #     #         self.activity()
# #     #         self.take_screenshot()


                    
                    

# # #     def save_state(self):
# # #         state = {
# # #             "elapsed_time": self.elapsed_time,
# # #             "start_time": self.start_time,
# # #             "running": self.running
# # #             # Add other variables you want to save
# # #         }
# # #         with open(state_file, "w") as f:
# # #             json.dump(state, f)
# # #         print("State saved.")



# # #     def load_state(self):
# # #         if os.path.exists(state_file):
# # #             with open(state_file, "r") as f:
# # #                 state = json.load(f)
# # #                 self.elapsed_time = state.get("elapsed_time", 0)
# # #                 self.running = state.get("running", False)
# # #                 if self.running:
# # #                     self.start_time = time.time() - self.elapsed_time
# # #                     self.pause_tracking = False  # Resume tracking if paused
# # #                     Timer.recursion = True
# # #                     Timer.activity_recursion = True
# # #                     self.activity()
# # #                     self.take_screenshot()
# # #                 else:
# # #                     self.start_time = None
# # #             print("State loaded.")
# # #         else:
# # #             self.elapsed_time = 0
# # #             print("No previous state found.")
            
            

# # #     def update_timer(self):
# # #         if self.running:
# # #             self.elapsed_time = time.time() - self.start_time
# # #             self.save_state()

# # #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# # #         hours, minutes = divmod(minutes, 60)
# # #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# # #         self.lblTimer.config(text=time_str)

# # #         self.root.after(1000, self.update_timer)


# # #     def stop_timer(self):
# # #         try:
# # #             if self.running:
# # #                 self.running = False
# # #                 # if self.timer_thread and self.timer_thread.is_alive():
# # #                 #     self.timer_thread.join()

# # #                 if self.is_tracking:
# # #                     self.pause_tracking = True  # Pause tracking
# # #                     print("stop")
# # #                     Timer.recursion = False
# # #                     Timer.activity_recursion = False
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             # messagebox.showerror("Error 3", error_message)
# # #             print("3")

# # #     def end_shift(self):
# # #         try:
# # #             self.stop_timer()
# # #             confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# # #             if confirmation:
# # #                 messagebox.showinfo("Shift Ended", "Shift has ended.")
# # #                 print("Shift ended")
# # #                 # Call save_state on end_shift
# # #                 self.save_state()
# # #                 # Clear state file on end_shift
# # #                 if os.path.exists(state_file):
# # #                     os.remove(state_file)
# # #                     print("State file cleared.")
# # #         # Other end_shift functionality...
# # #             else:
# # #                 self.start_timer()
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 4", error_message)
# # #             print("4")
            


# # #     def start_tracking(self):
# # #         try:
# # #             if not self.is_tracking:
# # #                 self.start_time = time.time()
# # #                 self.tracking_thread = threading.Thread(target=self.track_mouse)
# # #                 self.tracking_thread.daemon = True
# # #                 self.tracking_thread.start()
# # #                 self.is_tracking = True
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 6", error_message)
# # #             print("6")
# # #             # Apply functionality of try block in except block
        

# # #     def track_mouse(self):
# # #         try:
# # #             with Listener(on_click=self.on_click) as listener:
# # #                 listener.join()
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 7", error_message)
# # #             print("7")
# # #             # with Listener(on_click=self.on_click) as listener:
# # #             #     listener.join()


# # #     def stop_tracking(self):
# # #         try:
# # #             print("stop tracking")
# # #             if self.is_tracking:
# # #                 if self.tracking_thread.is_alive():
# # #                     self.tracking_thread.join()
# # #                 self.end_time = None
# # #                 self.is_tracking = False
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 8", error_message)
# # #             print("8")
            

# # #     def on_click(self, x, y, button, pressed):
# # #         try:
# # #             if not self.pause_tracking:
# # #                 if pressed:
# # #                     Timer.isclicked = "true"
# # #                     Timer.employeeStatus = 1
# # #                 else:
# # #                     print("")
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 9", error_message)
# # #             print("9")
        


# # #     def activity(self):
# # #         try:
# # #             ActiveTabs()
# # #             if self.activity_recursion:
# # #                 event_activity(mouseclick=Timer.isclicked,
# # #                                keystroke=Timer.ispressed,
# # #                                employeeStatus = Timer.employeeStatus,
# # #                                activeTab=Timer.CurrentTab,
# # #                                hoursPassed=round(self.elapsed_time),
# # #                                shiftstatus="working")
# # #                 print(round(self.elapsed_time))
# # #                 self.root.after(15000, self.activity)
# # #         except Exception as e:
# # #             error_message = f"An error occurred: {e}"
# # #             print(error_message)
# # #             messagebox.showerror("Error 10", error_message)
# # #             print("10")

# # #     def take_screenshot(self):
# # #         try:
# # #             if Timer.recursion:
# # #                 ActiveTabs()
# # #                 print("Taking screenshot...")
# # #                 screen_width, screen_height = ImageGrab.grab().size
# # #                 top_height = int(1 * screen_height)
# # #                 region = (0, 0, screen_width, top_height)
# # #                 screenshot = ImageGrab.grab(bbox=region)
# # #                 image_stream = BytesIO()
# # #                 screenshot.save(image_stream, format='PNG')
# # #                 image_bytes = image_stream.getvalue()
# # #                 print("Screenshot taken...")
# # #                 post_clicks(imagepath=image_bytes, activeTab=Timer.CurrentTab, shiftStatus="working")
# # #                 self.root.after(60000, self.take_screenshot)
# # #             else:
# # #                 image_bytes = None
# # #                 print(image_bytes)

# # #         except UnidentifiedImageError as e:
# # #             error_message = f"Error: {e}"
# # #             print(error_message)
# # #             # messagebox.showerror("Error 11(a)", error_message)
# # #             print("11(a)")
# # #             image_bytes = None
# # #             time.sleep(1)
# # #             self.take_screenshot()

# # #         except Exception as e:
# # #             error_message = f"Unexpected error: {e}"
# # #             print(error_message)
# # #             # messagebox.showerror("Error 11(b)", error_message)
# # #             print("11(b)")
# # #             self.take_screenshot()
# # #             image_bytes = None

# # #         return image_bytes

# # # def on_press(key, self):
# # #     try:
# # #         print(f"Key pressed: {key.char}")
# # #     except AttributeError:
# # #         print(f"Special key pressed: {key}")

# # # def generate_log(self):
# # #     print("Generating log...")
# # #     with keyboard.Listener(on_press=on_press) as keyboardlistener:
# # #         keyboardlistener.join()

# # # def start_logging_thread(self):
# # #     try:
# # #         logging_thread = threading.Thread(target=self.generate_log)
# # #         logging_thread.start()
# # #     except Exception as e:
# # #         print(f"Exception in start_logging_thread: {e}")

# # # def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab , employeeStatus):
# # #     try:
# # #         api_url = "https://mudeerapi.abasa.com/user/eventactivity"
# # #         data = {
# # #             "user_id": Timer.User_id,
# # #             "mouseclick": mouseclick,
# # #             "activeTab": activeTab,
# # #             "keystroke": keystroke,
# # #             "employeeStatus": employeeStatus,
# # #             "hoursPassed": hoursPassed,
# # #             "shiftStatus": shiftstatus,
# # #         }
# # #         print(data)
# # #         headers = {
# # #             "Authorization": f"Bearer {Timer.bearer_token}",
# # #         }
# # #         response = requests.post(api_url, data=data, headers=headers)
# # #         if response.status_code == 200:
# # #             # print(Timer.ispressed)
# # #             # print(response.status_code)
# # #             # print("--------------------------------")
# # #             Timer.isclicked = "false"
# # #             Timer.ispressed = "false"
# # #             Timer.employeeStatus = 0
# # #             # print("successss")
# # #             # print(Timer.ispressed)
# # #         else:
# # #             # print("faileddddddddddd")
# # #             print(response.status_code)
# # #     except requests.ConnectionError as e:
# # #         print("no internet")
# # #         # messagebox.showinfo("Connection Error",
# # #         #                     "Internet connection is not available. Please Connect to a reliable Internet.")
# # #     except Exception as e:
# # #         print("no internetttttttttt exception")

# # # def post_clicks(imagepath, activeTab, shiftStatus):
# # #     try:
# # #         api_url = "https://mudeerapi.abasa.com/user/activewindow"
# # #         data = {
# # #             "user_id": Timer.User_id,
# # #             "shiftStatus": shiftStatus,
# # #             "activeTab": activeTab
# # #         }
# # #         headers = {
# # #             "Authorization": f"Bearer {Timer.bearer_token}",
# # #         }
# # #         image_path = imagepath
# # #         files = {'testImage': (f'{datetime.datetime.now()}image.png', image_path)}
# # #         response = requests.post(api_url, data=data, headers=headers, files=files)
# # #         if response.status_code == 200:
# # #             print(response.status_code)
# # #             print("successss")
# # #         else:
# # #             print("faileddddddddddd")
# # #             print(response.status_code)
# # #     except requests.ConnectionError as e:
# # #         print(f"Connection error: {e}")
# # #         # messagebox.showinfo("Connection Error",
# # #         #                     "Interne connection is not available. Please Connect to a reliable Internet.")
# # #     except Exception as e:
# # #         print(f"Error 13: {e}")
# # #         print("13")

# # # def ActiveTabs():
# # #     try:
# # #         if system_platform == 'Darwin':
# # #             active_window = gw.getActiveWindow()
# # #             if active_window:
# # #                 Timer.CurrentTab = active_window
# # #                 print("Active window title:", active_window)
# # #             else:
# # #                 Timer.CurrentTab = active_window
# # #                 print("No active window detected")
# # #         else:
# # #             active_window = gw.getActiveWindow()
# # #             if active_window:
# # #                 Timer.CurrentTab = active_window.title
# # #                 print("Active window title:", active_window.title)
# # #             else:
# # #                 Timer.CurrentTab = "No Active"
# # #                 print("No active window detected")
# # #     except Exception as e:
# # #         messagebox.showerror("Error 12", f"An error occurred: {e}")
# # #         print("12")

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
# # import datetime
# # import requests
# # import pygetwindow as gw
# # from pynput.mouse import Listener

# # # Set TK_SILENCE_DEPRECATION to suppress the warning
# # os.environ["TK_SILENCE_DEPRECATION"] = "1"
# # state_file = "appState.json"

# # # Determine the system platform
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
# #         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# #         self.time = 0
# #         self.running = False
# #         self.abs_start_time = time.time()  # Absolute start time of the timer
# #         self.elapsed_time = 0
# #         self.is_tracking = False
# #         self.tracking_thread = None
# #         self.pause_tracking = False  # Flag to indicate tracking should pause
# #         self.clickArray = []

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
        
# #         self.test()
# #         self.test2()


# #         self.update_timer()

# #     def start_timer(self):
# #         if not self.running:
# #             self.running = True
# #             self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
# #             self.pause_tracking = False  # Resume tracking if paused
            
# #             Timer.recursion = True
# #             Timer.activity_recursion = True
# #             self.activity()
# #             self.take_screenshot()
# #             self.start_tracking()
           
            

            
            
# #     def test(self):
# #         print(self.running)
# #         if self.running:
# #             print("runinggggggggggggggggggggggggggggggggggg")
# #             event_activity(mouseclick=Timer.isclicked,
# #                            keystroke=Timer.ispressed,
# #                            employeeStatus=Timer.employeeStatus,
# #                            activeTab=Timer.CurrentTab,
# #                            hoursPassed=round(self.elapsed_time),
# #                            shiftstatus="working")
            
# #         print("not runiningggggggggggggggggggggggggggg")    
# #         self.root.after(17000, self.test)
        
        
        
# #     def test2(self):
# #         print(self.running)
# #         if self.running:
# #             print("runinggggggggggggggggggggggggggggggggggg2222222")
# #             post_clicks(imagepath=Timer.image_bytes, activeTab=Timer.CurrentTab, shiftStatus="working")
        
# #         print("not runiningggggggggggggggggggggggggggg22222222")    
# #         self.root.after(180000, self.test2)

# #     def stop_timer(self):
# #         if self.running:
# #             self.running = False
# #             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
# #             self.save_state()
# #             if self.is_tracking:
# #                 self.pause_tracking = True  # Pause tracking
# #                 Timer.recursion = False
# #                 Timer.activity_recursion = False

# #     def end_shift(self):
# #         self.stop_timer()
# #         confirmation = messagebox.askyesno("End Shift Confirmation", "Are you sure your Work Hours are Completed?")
# #         if confirmation:
# #             messagebox.showinfo("Shift Ended", "Shift has ended.")
# #             state = {
# #             "elapsed_time": 0,
# #             "abs_start_time":0,
# #             "running": False
# #             }
# #             with open(state_file, "w") as f:
# #                 json.dump(state, f)
# #             print("State saved.")
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
# #         print("on clickkkkkkkkkkkkkkkkkkkkkkkkkk")
# #         if not self.pause_tracking:
# #             if pressed:
# #                 print("presseeeeeeeeeeeeeeeeddddd")
# #                 Timer.isclicked = "true"
# #                 Timer.employeeStatus = 1

# #     def activity(self):
# #         ActiveTabs()
# #         if self.activity_recursion and self.running:
         
# #             self.root.after(15000, self.activity)

# #     def take_screenshot(self):
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
# #                 print(f"Size of the image: {image_size} bytes")
                
# #                 self.root.after(175000, self.take_screenshot)
# #             except Exception as e:
# #                 print(f"Error taking screenshot: {e}")
# #                 self.root.after(175000, self.take_screenshot)

# #     def save_state(self):
# #         try:
# #             state = {
# #                 "elapsed_time": self.elapsed_time,
# #                 "abs_start_time": self.abs_start_time,
# #                 "running": self.running
# #                 # Add other variables you want to save
# #             }
# #             with open(state_file, "w") as f:
# #                 json.dump(state, f)
# #             print("State saved.")
# #         except Exception as e:
# #             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")


# #     def load_state(self):
# #         try:
# #             if os.path.exists(state_file):
# #                 with open(state_file, "r") as f:
# #                     state = json.load(f)
# #                     self.elapsed_time = state.get("elapsed_time", 0)
# #                     self.abs_start_time = state.get("abs_start_time", time.time() - self.elapsed_time)
# #                     self.running = state.get("running", False)
# #                     if self.running:
# #                         self.pause_tracking = False  # Resume tracking if paused
# #                         Timer.recursion = True
# #                         Timer.activity_recursion = True
# #                         self.abs_start_time = time.time() - self.elapsed_time  # Correct absolute start time
# #                         self.activity()
# #                         self.take_screenshot()
# #                         self.start_tracking()

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
# #             self.save_state()

# #         minutes, seconds = divmod(int(self.elapsed_time), 60)
# #         hours, minutes = divmod(minutes, 60)
# #         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
# #         self.lblTimer.config(text=time_str)
        
# #         # Schedule the next update
# #         self.root.after(1000, self.update_timer)


# # def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab, employeeStatus):
# #     try:
# #         api_url = "https://mudeerapi.abasa.com/user/eventactivity"
# #         data = {
# #             "user_id": Timer.User_id,
# #             "mouseclick": mouseclick,
# #             "activeTab": activeTab,
# #             "keystroke": keystroke,
# #             "employeeStatus": employeeStatus,
# #             "hoursPassed": hoursPassed,
# #             "shiftStatus": shiftstatus,
# #         }
# #         headers = {
# #             "Authorization": f"Bearer {Timer.bearer_token}",
# #         }
# #         response = requests.post(api_url, data=data, headers=headers)
# #         if response.status_code == 200:
# #             print(data)
# #             print("event_activity")
# #             Timer.isclicked = "false"
# #             Timer.ispressed = "false"
# #             Timer.employeeStatus = 0
# #         else:
# #             print(f"Failed to send event activity data: {response.status_code}")
# #     except Exception as e:
# #         print(f"Error in event_activity: {e}")


# # def post_clicks(imagepath, activeTab, shiftStatus):
# #     try:
# #         api_url = "https://mudeerapi.abasa.com/user/activewindow"
# #         data = {
# #             "user_id": Timer.User_id,
# #             "shiftStatus": shiftStatus,
# #             "activeTab": activeTab
# #         }
# #         headers = {
# #             "Authorization": f"Bearer {Timer.bearer_token}",
# #         }
# #         image_path = imagepath
# #         files = {'testImage': (f'{datetime.datetime.now()}image.png', image_path)}
# #         response = requests.post(api_url, data=data, headers=headers, files=files)
# #         if response.status_code == 200:
# #             print(data)
# #             print("post_activity")
# #             print("Success")
# #         else:
# #             print(f"Failed to send screenshot: {response.status_code}")
# #     except Exception as e:
# #         print(f"Error in post_clicks: {e}")


# # def ActiveTabs():
# #     try:
# #         if system_platform == 'Darwin':
# #             active_window = gw.getActiveWindow()
# #             if active_window:
# #                 Timer.CurrentTab = active_window
# #                 print(active_window)
# #             else:
# #                 Timer.CurrentTab = None
# #         else:
# #             active_window = gw.getActiveWindow()
# #             if active_window:
# #                 Timer.CurrentTab = active_window.title
# #             else:
# #                 Timer.CurrentTab = "No Active Window"
# #     except Exception as e:
# #         print(f"Error in ActiveTabs: {e}")

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
# import datetime
# import requests
# import pygetwindow as gw
# from pynput.mouse import Listener
# from cryptography.fernet import Fernet

# # Set TK_SILENCE_DEPRECATION to suppress the warning
# os.environ["TK_SILENCE_DEPRECATION"] = "1"
# state_file = "program.json"
# encryption_key_file = "support.txt"

# # Determine the system platform
# system_platform = platform.system()

# # Generate and load the encryption key
# def generate_key():
#     return Fernet.generate_key()

# def save_key(key, filename):
#     with open(filename, "wb") as key_file:
#         key_file.write(key)

# def load_key(filename):
#     return open(filename, "rb").read()

# # Generate and save the encryption key if not already generated
# if not os.path.exists(encryption_key_file):
#     key = generate_key()
#     save_key(key, encryption_key_file)
# else:
#     key = load_key(encryption_key_file)

# # Encrypt data using the encryption key
# def encrypt_data(data, key):
#     fernet = Fernet(key)
#     encrypted_data = fernet.encrypt(data.encode())
#     return encrypted_data

# # Decrypt data using the encryption key
# def decrypt_data(encrypted_data, key):
#     fernet = Fernet(key)
#     decrypted_data = fernet.decrypt(encrypted_data).decode()
#     return decrypted_data

# # Set file permissions (600 for Unix-like systems)
# def set_permissions(filepath):
#     os.chmod(filepath, 0o600)  # Read and write permissions for the owner only

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
#         root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

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

#         self.test()
#         self.test2()

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

#     def test(self):
#         print(self.running)
#         if self.running:
#             print("runinggggggggggggggggggggggggggggggggggg")
#             event_activity(mouseclick=Timer.isclicked,
#                            keystroke=Timer.ispressed,
#                            employeeStatus=Timer.employeeStatus,
#                            activeTab=Timer.CurrentTab,
#                            hoursPassed=round(self.elapsed_time),
#                            shiftstatus="working")

#         print("not runiningggggggggggggggggggggggggggg")
#         self.root.after(17000, self.test)

#     def test2(self):
#         print(self.running)
#         if self.running:
#             print("runinggggggggggggggggggggggggggggggggggg2222222")
#             post_clicks(imagepath=Timer.image_bytes, activeTab=Timer.CurrentTab, shiftStatus="working")

#         print("not runiningggggggggggggggggggggggggggg22222222")
#         self.root.after(180000, self.test2)

#     def stop_timer(self):
#         if self.running:
#             self.running = False
#             self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
#             self.save_state()
#             if self.is_tracking:
#                 self.pause_tracking = True  # Pause tracking
#                 Timer.recursion = False
#                 Timer.activity_recursion = False

#     def end_shift(self):
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
#                 f.write(encrypt_data(json.dumps(state), key))
#             set_permissions(state_file)  # Set file permissions after writing
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
#         print("on clickkkkkkkkkkkkkkkkkkkkkkkkkk")
#         if not self.pause_tracking:
#             if pressed:
#                 print("presseeeeeeeeeeeeeeeeddddd")
#                 Timer.isclicked = "true"
#                 Timer.employeeStatus = 1

#     def activity(self):
#         ActiveTabs()
#         if self.activity_recursion and self.running:
#             self.root.after(15000, self.activity)

#     def take_screenshot(self):
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
#                 print(f"Size of the image: {image_size} bytes")

#                 self.root.after(175000, self.take_screenshot)
#             except Exception as e:
#                 print(f"Error taking screenshot: {e}")
#                 self.root.after(175000, self.take_screenshot)

#     def save_state(self):
#         try:
#             state = {
#                 "elapsed_time": self.elapsed_time,
#                 "abs_start_time": self.abs_start_time,
#                 "running": self.running
#                 # Add other variables you want to save
#             }
#             state_json = json.dumps(state)
#             encrypted_state = encrypt_data(state_json, key)
#             with open(state_file, "wb") as f:
#                 f.write(encrypted_state)
#             set_permissions(state_file)  # Set file permissions after writing
#             print("State saved.")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred while saving the state:\n{str(e)}")

#     def load_state(self):
#         try:
#             if os.path.exists(state_file):
#                 with open(state_file, "rb") as f:
#                     encrypted_state = f.read()
#                 decrypted_state = decrypt_data(encrypted_state, key)
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
#             self.save_state()

#         minutes, seconds = divmod(int(self.elapsed_time), 60)
#         hours, minutes = divmod(minutes, 60)
#         time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
#         self.lblTimer.config(text=time_str)

#         # Schedule the next update
#         self.root.after(1000, self.update_timer)


# def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab, employeeStatus):
#     try:
#         api_url = "https://mudeerapi.abasa.com/user/eventactivity"
#         data = {
#             "user_id": Timer.User_id,
#             "mouseclick": mouseclick,
#             "activeTab": activeTab,
#             "keystroke": keystroke,
#             "employeeStatus": employeeStatus,
#             "hoursPassed": hoursPassed,
#             "shiftStatus": shiftstatus,
#         }
#         headers = {
#             "Authorization": f"Bearer {Timer.bearer_token}",
#         }
#         response = requests.post(api_url, data=data, headers=headers)
#         if response.status_code == 200:
#             print(data)
#             print("event_activity")
#             Timer.isclicked = "false"
#             Timer.ispressed = "false"
#             Timer.employeeStatus = 0
#         else:
#             print(f"Failed to send event activity data: {response.status_code}")
#     except Exception as e:
#         print(f"Error in event_activity: {e}")


# def post_clicks(imagepath, activeTab, shiftStatus):
#     try:
#         api_url = "https://mudeerapi.abasa.com/user/activewindow"
#         data = {
#             "user_id": Timer.User_id,
#             "shiftStatus": shiftStatus,
#             "activeTab": activeTab
#         }
#         headers = {
#             "Authorization": f"Bearer {Timer.bearer_token}",
#         }
#         image_path = imagepath
#         files = {'testImage': (f'{datetime.datetime.now()}image.png', image_path)}
#         response = requests.post(api_url, data=data, headers=headers, files=files)
#         if response.status_code == 200:
#             print(data)
#             print("post_activity")
#             print("Success")
#         else:
#             print(f"Failed to send screenshot: {response.status_code}")
#     except Exception as e:
#         print(f"Error in post_clicks: {e}")


# def ActiveTabs():
#     try:
#         if system_platform == 'Darwin':
#             active_window = gw.getActiveWindow()
#             if active_window:
#                 Timer.CurrentTab = active_window
#                 print(active_window)
#             else:
#                 Timer.CurrentTab = None
#         else:
#             active_window = gw.getActiveWindow()
#             if active_window:
#                 Timer.CurrentTab = active_window.title
#             else:
#                 Timer.CurrentTab = "No Active Window"
#     except Exception as e:
#         print(f"Error in ActiveTabs: {e}")

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

        self.test()
        self.test2()

        self.update_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.abs_start_time = time.time() - self.elapsed_time  # Update absolute start time
            self.pause_tracking = False  # Resume tracking if paused

            Timer.recursion = True
            Timer.activity_recursion = True
            self.activity()
            self.take_screenshot()
            self.start_tracking()

    def test(self):
        from api_services import event_activity
        print(self.running)
        if self.running:
            print("runinggggggggggggggggggggggggggggggggggggggg")
      
            event_activity(mouseclick=Timer.isclicked,
                           keystroke=Timer.ispressed,
                           employeeStatus=Timer.employeeStatus,
                           activeTab=Timer.CurrentTab,
                           hoursPassed=round(self.elapsed_time),
                           shiftstatus="working",user_id=Timer.User_id,bearer_token=Timer.bearer_token,)

        print("not runiningggggggggggggggggggggggggggg")
        self.root.after(17000, self.test)

    def test2(self):
        from api_services import post_clicks

        print(self.running)
        if self.running:
            print("runinggggggggggggggggggggggggggggggggggg2222222")
            post_clicks(imagepath=Timer.image_bytes, activeTab=Timer.CurrentTab, shiftStatus="working",user_id=Timer.User_id)

        print("not runiningggggggggggggggggggggggggggg22222222")
        self.root.after(180000, self.test2)

    def stop_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.abs_start_time  # Update elapsed time based on absolute start time
            self.save_state()
            if self.is_tracking:
                self.pause_tracking = True  # Pause tracking
                Timer.recursion = False
                Timer.activity_recursion = False

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
            print("State saved.")
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
        print("on clickkkkkkkkkkkkkkkkkkkkkkkkkk")
        if not self.pause_tracking:
            if pressed:
                print("presseeeeeeeeeeeeeeeeddddd")
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
                print(f"Size of the image: {image_size} bytes")

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
                "running": self.running
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
            self.save_state()

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









