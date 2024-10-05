import time
from datetime import datetime

import RPi.GPIO as GPIO

if __name__ == "__main__":
    # The GPIO.BCM is how they are called on the sticker. D4 = 4 then.
    # If you use GPIO.BOARD D4 = pin 7,
    GPIO.setmode(GPIO.BCM)

    pir_sensor_bcm_pin = 4
    GPIO.setup(pir_sensor_bcm_pin, GPIO.IN)

    while True:
        if GPIO.input(pir_sensor_bcm_pin):
            time_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"{time_str} detected something")
        else:
            print("Nothing")

        time.sleep(1)
