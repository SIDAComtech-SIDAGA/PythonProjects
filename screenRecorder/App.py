import cv2
import numpy as np
import pyautogui
import keyboard


# Get the screen size for recording
screen_size = pyautogui.size()

# Set frames per second and codec
fps = 20
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Define output file name
output_file = "Screen_Recording.mp4"

# Initialize the VideoWriter
out = cv2.VideoWriter(output_file, fourcc, fps, (screen_size.width, screen_size.height))

print("Recording... Press 'q' to stop.")

try:
    while True:
        # Capture a screenshot
        screen = pyautogui.screenshot()
        
        # Convert the screenshot to a NumPy array
        frame = np.array(screen)
        
        # Convert the color from RGB to BGR (OpenCV format)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Write the frame to the video file
        out.write(frame)
        
        # Check if 'q' is pressed to stop recording
        if keyboard.is_pressed('q'):
            print("Recording stopped.")
            break
except KeyboardInterrupt:
    # Handle a manual interruption (Ctrl+C) gracefully
    print("\nRecording interrupted.")

# Release the VideoWriter and save the file
out.release()
print(f"Video file was saved to {output_file}")
q