# # import datetime
# # import requests
# # from tkinter import messagebox
# # from timer_screen import Timer
# # from helper_functions import update_employeeStatus, update_isclicked, update_ispressed

# # def login(email, password):
# #     api_url = "https://mudeerapi.abasa.com/user/login"
# #     data = {
# #         "email": email,
# #         "password": password
# #     }

# #     try:
# #         response = requests.post(api_url, json=data)
# #         # response.raise_for_status()
# #     except requests.exceptions.RequestException as e:
# #         messagebox.showerror("Error", f"Login failed. {str(e)}")
# #         return None

# #     if response.status_code == 200:
# #         response_data = response.json()
# #         Timer.bearer_token = response_data['token']
# #         Timer.User_id = response_data['_id']
# #         mark_attendance(
# #             user_id=response_data['_id'],
# #             name=response_data['first_name'],
# #             department=response_data['department'],
# #             status=" ",
# #             appversion="v2",
# #         )
# #         messagebox.showinfo("Success", "Login successful!")
# #         return response_data
# #     else:
# #         response_data = response.json()
# #         messagebox.showerror("Error", response_data["message"])
# #         return None

# # def mark_attendance(user_id, name, status, department, appversion):
# #     api_url = "https://mudeerapi.abasa.com/user/attendance"
# #     data = {
# #         "user_id": user_id,
# #         "name": name,
# #         "attendanceStatus": status,
# #         "department": department,
# #         "app_version": appversion,
# #         "createdAt": ""
# #     }

# #     try:
# #         headers = {
# #             "Authorization": f"Bearer {Timer.bearer_token}",
# #         }
# #         response = requests.post(api_url, json=data, headers=headers)
# #         # response.raise_for_status()
# #     except requests.exceptions.RequestException as e:
# #         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
# #         return

# #     if response.status_code == 200:
# #         response_data = response.json()
# #         print(response_data['message'])
# #     else:
# #         print("Failed to mark attendance")
# #         print(response.status_code)

# # def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab, employeeStatus,user_id,bearer_token):
# #     try:
# #         api_url = "https://mudeerapi.abasa.com/user/eventactivity"
# #         data = {
# #             "user_id": user_id,
# #             "mouseclick": mouseclick,
# #             "activeTab": activeTab,
# #             "keystroke": keystroke,
# #             "employeeStatus": employeeStatus,
# #             "hoursPassed": hoursPassed,
# #             "shiftStatus": shiftstatus,
# #         }
# #         headers = {
# #             "Authorization": f"Bearer {bearer_token}",
# #         }
# #         response = requests.post(api_url, data=data, headers=headers)
# #         if response.status_code == 200:
# #             print(data)
# #             print("event_activity")
# #             update_isclicked("false")
# #             update_ispressed("false")
# #             update_employeeStatus(0)
# #         else:
# #             print(f"Failed to send event activity data: {response.status_code}")
# #     except Exception as e:
# #         print(f"Error in event_activity: {e}")
              
# # def post_clicks(imagepath, activeTab, shiftStatus,user_id):
# #     try:
# #         api_url = "https://mudeerapi.abasa.com/user/activewindow"
# #         data = {
# #             "user_id": user_id,
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
    
    
# # def checkout(user_id):
# #     api_url = "https://mudeerapi.abasa.com/user/attendance/checkout"
# #     data = {
# #         "user_id": user_id,
# #     }
# #     try:
# #         headers = {
# #             "Authorization": f"Bearer {Timer.bearer_token}",
# #         }
# #         response = requests.post(api_url, json=data, headers=headers)
# #         # response.raise_for_status()
# #         print(api_url)
# #         print(data)
# #     except requests.exceptions.RequestException as e:
# #         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
# #         return

# #     if response.status_code == 200:
# #         response_data = response.json()
# #         print(response_data['message'])
# #     else:
# #         print("Failed to checkout")
# #         print(response.status_code)
        
# # def start_break(user_id):
# #     api_url = "https://mudeerapi.abasa.com/user/attendance/break/start"
# #     data = {
# #         "user_id": user_id,
# #     }
# #     try:
# #         headers = {
# #             "Authorization": f"Bearer {Timer.bearer_token}",
# #         }
# #         response = requests.post(api_url, json=data, headers=headers)
# #         # response.raise_for_status()
# #         print(api_url)
# #         print(data)
# #     except requests.exceptions.RequestException as e:
# #         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
# #         return

# #     if response.status_code == 200:
# #         response_data = response.json()
# #         print(response_data['message'])
# #     else:
# #         print("Failed to checkout")
# #         print(response.status_code)
        
        
# # def stop_break(user_id):
# #     api_url = "https://mudeerapi.abasa.com/user/attendance/break/stop"
# #     data = {
# #         "user_id": user_id,
# #     }
# #     try:
# #         headers = {
# #             "Authorization": f"Bearer {Timer.bearer_token}",
# #         }
# #         response = requests.post(api_url, json=data, headers=headers)
# #         # response.raise_for_status()
# #         print(api_url)
# #         print(data)
# #     except requests.exceptions.RequestException as e:
# #         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
# #         return

# #     if response.status_code == 200:
# #         response_data = response.json()
# #         print(response_data['message'])
# #     else:
# #         print("Failed to checkout")
# #         print(response.status_code)

# import datetime
# import requests
# from tkinter import messagebox
# from timer_screen import Timer
# from helper_functions import update_employeeStatus, update_isclicked, update_ispressed

# def login(email, password):
#     api_url = "https://mudeerapi.abasa.com/user/login"
#     print(f"API HIT: {api_url}")
#     data = {
#         "email": email,
#         "password": password
#     }

#     try:
#         response = requests.post(api_url, json=data)
#         # response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Login failed. {str(e)}")
#         return None

#     if response.status_code == 200:
#         response_data = response.json()
#         Timer.bearer_token = response_data['token']
#         Timer.User_id = response_data['_id']
#         mark_attendance(
#             user_id=response_data['_id'],
#             name=response_data['first_name'],
#             department=response_data['department'],
#             status=" ",
#             appversion="v2",
#         )
#         messagebox.showinfo("Success", "Login successful!")
#         return response_data
#     else:
#         response_data = response.json()
#         messagebox.showerror("Error", response_data["message"])
#         return None

# def mark_attendance(user_id, name, status, department, appversion):
#     api_url = "https://mudeerapi.abasa.com/user/attendance"
#     print(f"API HIT: {api_url}")
#     data = {
#         "user_id": user_id,
#         "name": name,
#         "attendanceStatus": status,
#         "department": department,
#         "app_version": appversion,
#         "createdAt": ""
#     }

#     try:
#         headers = {
#             "Authorization": f"Bearer {Timer.bearer_token}",
#         }
#         response = requests.post(api_url, json=data, headers=headers)
#         # response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
#         return

#     if response.status_code == 200:
#         response_data = response.json()
#         print(response_data['message'])
#     else:
#         print("Failed to mark attendance")
#         print(response.status_code)

# def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab, employeeStatus,user_id,bearer_token):
#     api_url = "https://mudeerapi.abasa.com/user/eventactivity"
#     print(f"API HIT: {api_url}")
#     try:
#         data = {
#             "user_id": user_id,
#             "mouseclick": mouseclick,
#             "activeTab": activeTab,
#             "keystroke": keystroke,
#             "employeeStatus": employeeStatus,
#             "hoursPassed": hoursPassed,
#             "shiftStatus": shiftstatus,
#         }
#         headers = {
#             "Authorization": f"Bearer {bearer_token}",
#         }
#         response = requests.post(api_url, data=data, headers=headers)
#         if response.status_code == 200:
#             print(data)
#             print("event_activity")
#             update_isclicked("false")
#             update_ispressed("false")
#             update_employeeStatus(0)
#         else:
#             print(f"Failed to send event activity data: {response.status_code}")
#     except Exception as e:
#         print(f"Error in event_activity: {e}")
              
# def post_clicks(imagepath, activeTab, shiftStatus,user_id):
#     api_url = "https://mudeerapi.abasa.com/user/activewindow"
#     print(f"API HIT: {api_url}")
#     try:
#         data = {
#             "user_id": user_id,
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
    
    
# def checkout(user_id):
#     api_url = "https://mudeerapi.abasa.com/user/attendance/checkout"
#     print(f"API HIT: {api_url}")
#     data = {
#         "user_id": user_id,
#     }
#     try:
#         headers = {
#             "Authorization": f"Bearer {Timer.bearer_token}",
#         }
#         response = requests.post(api_url, json=data, headers=headers)
#         # response.raise_for_status()
#         print(data)
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
#         return

#     if response.status_code == 200:
#         response_data = response.json()
#         print(response_data['message'])
#     else:
#         print("Failed to checkout")
#         print(response.status_code)
        
# def start_break(user_id):
#     api_url = "https://mudeerapi.abasa.com/user/attendance/break/start"
#     print(f"API HIT: {api_url}")
#     data = {
#         "user_id": user_id,
#     }
#     try:
#         headers = {
#             "Authorization": f"Bearer {Timer.bearer_token}",
#         }
#         response = requests.post(api_url, json=data, headers=headers)
#         # response.raise_for_status()
#         print(data)
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
#         return

#     if response.status_code == 200:
#         response_data = response.json()
#         print(response_data['message'])
#     else:
#         print("Failed to start break")
#         print(response.status_code)
        
        
# def stop_break(user_id):
#     api_url = "https://mudeerapi.abasa.com/user/attendance/break/stop"
#     print(f"API HIT: {api_url}")
#     data = {
#         "user_id": user_id,
#     }
#     try:
#         headers = {
#             "Authorization": f"Bearer {Timer.bearer_token}",
#         }
#         response = requests.post(api_url, json=data, headers=headers)
#         # response.raise_for_status()
#         print(data)
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
#         return

#     if response.status_code == 200:
#         response_data = response.json()
#         print(response_data['message'])
#     else:
#         print("Failed to stop break")
#         print(response.status_code)

import datetime
import requests
from tkinter import messagebox

def login(email, password):
    api_url = "https://mudeerapi.abasa.com/user/login"
    print(f"API HIT: {api_url}")
    data = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(api_url, json=data, timeout=10)
        # response.raise_for_status()
    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "Login request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "Cannot connect to server. Please check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Login failed. {str(e)}")
        return None

    if response.status_code == 200:
        response_data = response.json()
        bearer_token = response_data['token']
        user_id = response_data['_id']
        
        mark_attendance(
            user_id=user_id,
            bearer_token=bearer_token,
            name=response_data['first_name'],
            department=response_data['department'],
            status=" ",
            appversion="v2",
        )
        messagebox.showinfo("Success", "Login successful!")
        
        # Return token and user_id separately
        response_data['bearer_token'] = bearer_token
        response_data['user_id'] = user_id
        return response_data
    else:
        try:
            response_data = response.json()
            messagebox.showerror("Error", response_data.get("message", "Login failed"))
        except:
            messagebox.showerror("Error", f"Login failed with status code: {response.status_code}")
        return None

def mark_attendance(user_id, bearer_token, name, status, department, appversion):
    api_url = "https://mudeerapi.abasa.com/user/attendance"
    print(f"API HIT: {api_url}")
    data = {
        "user_id": user_id,
        "name": name,
        "attendanceStatus": status,
        "department": department,
        "app_version": appversion,
        "createdAt": ""
    }

    try:
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers, timeout=10)
        # response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Mark attendance request timed out")
        return
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server for attendance")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error marking attendance: {str(e)}")
        return

    if response.status_code == 200:
        try:
            response_data = response.json()
            print(response_data.get('message', 'Attendance marked'))
        except:
            print("Attendance marked successfully")
    else:
        print(f"Failed to mark attendance - Status: {response.status_code}")

def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab, employeeStatus, user_id, bearer_token, timer_instance=None):
    api_url = "https://mudeerapi.abasa.com/user/eventactivity"
    print(f"API HIT: {api_url}")
    try:
        data = {
            "user_id": user_id,
            "mouseclick": mouseclick,
            "activeTab": activeTab,
            "keystroke": keystroke,
            "employeeStatus": employeeStatus,
            "hoursPassed": hoursPassed,
            "shiftStatus": shiftstatus,
        }
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        response = requests.post(api_url, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            print(data)
            print("event_activity success")
            
            # Update timer instance if provided
            if timer_instance:
                from helper_functions import update_isclicked, update_ispressed, update_employeeStatus
                update_isclicked(timer_instance, "false")
                update_ispressed(timer_instance, "false")
                update_employeeStatus(timer_instance, 0)
        else:
            print(f"Failed to send event activity data: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Event activity request timed out")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server for event activity")
    except Exception as e:
        print(f"Error in event_activity: {e}")
              
def post_clicks(imagepath, activeTab, shiftStatus, user_id, bearer_token):
    api_url = "https://mudeerapi.abasa.com/user/activewindow"
    print(f"API HIT: {api_url}")
    try:
        data = {
            "user_id": user_id,
            "shiftStatus": shiftStatus,
            "activeTab": activeTab
        }
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        image_path = imagepath
        files = {'testImage': (f'{datetime.datetime.now()}image.png', image_path)}
        response = requests.post(api_url, data=data, headers=headers, files=files, timeout=15)
        if response.status_code == 200:
            print(data)
            print("post_activity success")
        else:
            print(f"Failed to send screenshot: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Post clicks request timed out")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server for screenshot upload")
    except Exception as e:
        print(f"Error in post_clicks: {e}")
    
    
def checkout(user_id, bearer_token):
    api_url = "https://mudeerapi.abasa.com/user/attendance/checkout"
    print(f"API HIT: {api_url}")
    data = {
        "user_id": user_id,
    }
    try:
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers, timeout=10)
        print(data)
        
        if response.status_code == 200:
            try:
                response_data = response.json()
                print(response_data.get('message', 'Checkout successful'))
            except:
                print("Checkout successful")
        else:
            print(f"Failed to checkout - Status: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Checkout request timed out")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server for checkout")
    except requests.exceptions.RequestException as e:
        print(f"Error during checkout: {str(e)}")
        
def start_break(user_id, bearer_token):
    api_url = "https://mudeerapi.abasa.com/user/attendance/break/start"
    print(f"API HIT: {api_url}")
    data = {
        "user_id": user_id,
    }
    try:
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers, timeout=10)
        print(data)
        
        if response.status_code == 200:
            try:
                response_data = response.json()
                print(response_data.get('message', 'Break started'))
            except:
                print("Break started successfully")
        else:
            print(f"Failed to start break - Status: {response.status_code}")
            try:
                error_response = response.json()
                print(f"Error Response: {error_response}")
            except:
                print(f"Raw Response: {response.text}")
    except requests.exceptions.Timeout:
        print("Start break request timed out")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server for break start")
    except requests.exceptions.RequestException as e:
        print(f"Error starting break: {str(e)}")
        
        
def stop_break(user_id, bearer_token):
    api_url = "https://mudeerapi.abasa.com/user/attendance/break/stop"
    print(f"API HIT: {api_url}")
    data = {
        "user_id": user_id,
    }
    try:
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers, timeout=10)
        print(data)
        
        if response.status_code == 200:
            try:
                response_data = response.json()
                print(response_data.get('message', 'Break stopped'))
            except:
                print("Break stopped successfully")
        else:
            print(f"Failed to stop break - Status: {response.status_code}")
            try:
                error_response = response.json()
                print(f"Error Response: {error_response}")
            except:
                print(f"Raw Response: {response.text}")
    except requests.exceptions.Timeout:
        print("Stop break request timed out")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server for break stop")
    except requests.exceptions.RequestException as e:
        print(f"Error stopping break: {str(e)}")