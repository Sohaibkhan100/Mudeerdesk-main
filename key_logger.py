
import threading
from timer_screen import Timer
from pynput import keyboard
import time


class Logger:
    exit_event = threading.Event()  # Event to signal the thread to exit
    logging_thread = None  # Global variable to store the thread



def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
        Timer.ispressed = "true"
        Timer.employeeStatus=1
    except AttributeError:
        print(f"Special key pressed: {key}")
        Timer.ispressed = "true"
        Timer.employeeStatus=1

    if Logger.exit_event.is_set():
        # If the exit event is set, stop the keylogging loop
        return False 

def generate_log():
    print("Generating log...")
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        while not Logger.exit_event.is_set():
            if not keyboard_listener.running:  # Check if the listener is still running
                break  # Break out of the loop if the listener is no longer running
            time.sleep(0.1)  # Sleep for a short duration to avoid high CPU usage

    print("Log generation stopped.")


def start_logging_thread():
    try:
        Logger.logging_thread = threading.Thread(target=generate_log)
        Logger.logging_thread.start()
    except Exception as e:
        print(f"Exception in start_logging_thread: {e}")

def stop_logging_thread():
    print(Logger.exit_event)
    Logger.exit_event.set() # Set the event to signal the thread to exit
    print("hey")
    if Logger.logging_thread is not None:
        Logger.logging_thread.join()
        
