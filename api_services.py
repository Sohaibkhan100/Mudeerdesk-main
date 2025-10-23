import datetime
import requests
from tkinter import messagebox
from timer_screen import Timer
from helper_functions import update_employeeStatus, update_isclicked, update_ispressed

def login(email, password):
    api_url = "https://mudeerapi.abasa.com/user/login"
    data = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(api_url, json=data)
        # response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Login failed. {str(e)}")
        return None

    if response.status_code == 200:
        response_data = response.json()
        Timer.bearer_token = response_data['token']
        Timer.User_id = response_data['_id']
        mark_attendance(
            user_id=response_data['_id'],
            name=response_data['first_name'],
            department=response_data['department'],
            status=" ",
            appversion="v2",
        )
        messagebox.showinfo("Success", "Login successful!")
        return response_data
    else:
        response_data = response.json()
        messagebox.showerror("Error", response_data["message"])
        return None

def mark_attendance(user_id, name, status, department, appversion):
    api_url = "https://mudeerapi.abasa.com/user/attendance"
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
            "Authorization": f"Bearer {Timer.bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers)
        # response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
        return

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['message'])
    else:
        print("Failed to mark attendance")
        print(response.status_code)

def event_activity(mouseclick, keystroke, hoursPassed, shiftstatus, activeTab, employeeStatus,user_id,bearer_token):
    try:
        api_url = "https://mudeerapi.abasa.com/user/eventactivity"
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
        response = requests.post(api_url, data=data, headers=headers)
        if response.status_code == 200:
            print(data)
            print("event_activity")
            update_isclicked("false")
            update_ispressed("false")
            update_employeeStatus(0)
        else:
            print(f"Failed to send event activity data: {response.status_code}")
    except Exception as e:
        print(f"Error in event_activity: {e}")
              
def post_clicks(imagepath, activeTab, shiftStatus,user_id):
    try:
        api_url = "https://mudeerapi.abasa.com/user/activewindow"
        data = {
            "user_id": user_id,
            "shiftStatus": shiftStatus,
            "activeTab": activeTab
        }
        headers = {
            "Authorization": f"Bearer {Timer.bearer_token}",
        }
        image_path = imagepath
        files = {'testImage': (f'{datetime.datetime.now()}image.png', image_path)}
        response = requests.post(api_url, data=data, headers=headers, files=files)
        if response.status_code == 200:
            print(data)
            print("post_activity")
            print("Success")
        else:
            print(f"Failed to send screenshot: {response.status_code}")
    except Exception as e:
        print(f"Error in post_clicks: {e}")
    
    
def checkout(user_id):
    api_url = "https://mudeerapi.abasa.com/user/attendance/checkout"
    data = {
        "user_id": user_id,
    }
    try:
        headers = {
            "Authorization": f"Bearer {Timer.bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers)
        # response.raise_for_status()
        print(api_url)
        print(data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
        return

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['message'])
    else:
        print("Failed to checkout")
        print(response.status_code)
        
def start_break(user_id):
    api_url = "https://mudeerapi.abasa.com/user/attendance/break/start"
    data = {
        "user_id": user_id,
    }
    try:
        headers = {
            "Authorization": f"Bearer {Timer.bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers)
        # response.raise_for_status()
        print(api_url)
        print(data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
        return

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['message'])
    else:
        print("Failed to checkout")
        print(response.status_code)
        
        
def stop_break(user_id):
    api_url = "https://mudeerapi.abasa.com/user/attendance/break/stop"
    data = {
        "user_id": user_id,
    }
    try:
        headers = {
            "Authorization": f"Bearer {Timer.bearer_token}",
        }
        response = requests.post(api_url, json=data, headers=headers)
        # response.raise_for_status()
        print(api_url)
        print(data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Please check your internet connection. {str(e)}")
        return

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['message'])
    else:
        print("Failed to checkout")
        print(response.status_code)