import pyautogui
import keyboard
import time
import threading

# Set the click interval in seconds (adjustable)
click_interval = 0.5  # Time between clicks
clicking = False  # Global flag to track if the clicking is active

# Define the pattern of clicks as a list of (x, y) coordinates
click_pattern = [
    (500, 500),  # First click position (x, y)
    (600, 500),  # Second click position
    (700, 500),  # Third click position
    (600, 600),  # Fourth click position
    # You can add more coordinates as needed
]

# Function to handle clicking in a pattern
def start_clicking():
    global clicking
    while clicking:
        for position in click_pattern:
            if not clicking:
                break  # Stop the clicking if the flag is turned off
            pyautogui.click(position)  # Click at the specified position
            time.sleep(click_interval)  # Wait for the interval before next click

# Function to toggle the clicker
def toggle_clicker():
    global clicking
    if clicking:
        clicking = False
        print("Auto-clicker stopped.")
    else:
        clicking = True
        print("Auto-clicker started.")
        # Start the clicking in a separate thread to avoid blocking the keyboard input
        click_thread = threading.Thread(target=start_clicking)
        click_thread.start()

# Register hotkeys for starting/stopping
keyboard.add_hotkey('ctrl+alt+s', toggle_clicker)  # Press Ctrl+Alt+S to start/stop the clicker
keyboard.add_hotkey('ctrl+alt+q', lambda: exit())  # Press Ctrl+Alt+Q to quit the program

print("Pattern auto-clicker is ready. Press Ctrl+Alt+S to start/stop, Ctrl+Alt+Q to quit.")
keyboard.wait('ctrl+alt+q')  # Wait until the user presses the quit hotkey
