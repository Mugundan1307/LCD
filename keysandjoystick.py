import RPi.GPIO as GPIO
import time

pins = {
    21: "KEY1",
    20: "KEY2",
    16: "KEY3",
    6:  "JOY_UP",
    19: "JOY_DOWN",
    5:  "JOY_LEFT",
    26: "JOY_RIGHT",
    13: "JOY_PRESS",
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for p in pins:
    GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last = {p: GPIO.input(p) for p in pins}

print("Press joystick / keys, Ctrl+C to exit")
try:
    while True:
        for p, name in pins.items():
            v = GPIO.input(p)
            if v != last[p]:
                if v == 0:
                    print(f"{name} PRESSED")
                else:
                    print(f"{name} RELEASED")
                last[p] = v
        time.sleep(0.02)
except KeyboardInterrupt:
    GPIO.cleanup()
