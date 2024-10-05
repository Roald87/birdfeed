from picamera2 import Picamera2, Preview
import time
import datetime
from keypress import key_pressed

import RPi.GPIO as GPIO

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (2048, 1536)})
picam2.configure(config)
picam2.start(show_preview=False)

# The GPIO.BCM is how they are called on the sticker. D4 = 4 then.
# If you use GPIO.BOARD D4 = pin 7,
GPIO.setmode(GPIO.BCM)
pir_sensor_bcm_pin = 4
GPIO.setup(pir_sensor_bcm_pin, GPIO.IN)

print("Press 'q' to quit.")

while True:
    if GPIO.input(pir_sensor_bcm_pin):
        start_time = time.time()
        print("p pressed")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        filename = f"{timestamp}.jpg"
        picam2.capture_file(filename)

        end_time = time.time()
        capture_time = end_time - start_time
        print(f"Image captured: {filename}, Time taken: {capture_time:.2f} seconds")
        n = 5
        time.sleep(n)
        print(f"Sleeping for {n} s until watching for new movement.")
    elif key_pressed("q"):
        print("Exiting...")
        break

# Stop the camera
picam2.stop()
