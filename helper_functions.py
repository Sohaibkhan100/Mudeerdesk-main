import os
import platform
from timer_screen import Timer
from cryptography.fernet import Fernet
import pygetwindow as gw

system_platform = platform.system()


def update_isclicked(value):
    Timer.isclicked = value

def update_ispressed(value):
    Timer.ispressed = value

def update_employeeStatus(value):
    Timer.employeeStatus = value
    
    
def ActiveTabs():
    try:
        if system_platform == 'Darwin':
            active_window = gw.getActiveWindow()
            if active_window:
                Timer.CurrentTab = active_window
                # print(active_window)
            else:
                Timer.CurrentTab = None
        else:
            active_window = gw.getActiveWindow()
            if active_window:
                Timer.CurrentTab = active_window.title
            else:
                Timer.CurrentTab = "No Active Window"
    except Exception as e:
        print(f"Error in ActiveTabs: {e}")
        

# Proper Fernet key
fernet_key = b'kZNftXo3vNj2JHeJheJnPq7BpoO9xSxB_v5psl6vLDI='  # Replace with your generated key

# Encrypt data using the encryption key
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt data using the encryption key
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Set file permissions (600 for Unix-like systems)
def set_permissions(filepath):
    os.chmod(filepath, 0o600)  # Read and write permissions for the owner only