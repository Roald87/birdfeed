from picamera2 import Picamera2, Preview
import time
import datetime
from keypress import key_pressed

picam2 = Picamera2()
config = picam2.create_still_configuration(buffer_count=3)
picam2.configure(config)
picam2.start(show_preview=False)

print("Press 'p' to capture a photo. Press 'q' to quit.")

while True:
    if key_pressed("p"):
        start_time = time.time()
        print("p pressed")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        filename = f"{timestamp}.jpg"
        picam2.capture_file(filename)

        end_time = time.time()
        capture_time = end_time - start_time
        print(f"Image captured: {filename}, Time taken: {capture_time:.2f} seconds")

        # Add a small delay to avoid capturing multiple images with one keypress
        time.sleep(0.5)
    elif key_pressed("q"):
        print("Exiting...")
        break

# Stop the camera
picam2.stop()
