from picamera2 import Picamera2, Preview
import time
import datetime
from keypress import key_pressed

picam2 = Picamera2()
picam2.start()

print("Press 'p' to capture a photo. Press 'q' to quit.")

while True:
    if key_pressed("p"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        filename = f"{timestamp}.jpg"
        picam2.capture_file(filename)
        # Add a small delay to avoid capturing multiple images with one keypress
        time.sleep(0.5)
    elif key_pressed("q"):
        print("Exiting...")
        break

# Stop the camera
picam2.stop()
