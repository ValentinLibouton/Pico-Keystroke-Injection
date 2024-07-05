import time
import os
from lib.command import CommandProcessor
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout import KeyboardLayoutBE

# Configuration de la broche pour vérifier l'état du pin 14 (GP10)
pin = digitalio.DigitalInOut(board.GP10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutBE(keyboard)


inject_file = "inject.txt"
time.sleep(3)
if not pin.value:
    if inject_file in os.listdir():

        CommandProcessor(filename=inject_file, layout=layout, write_speed=0.001)
    else:
        print("Inject file does not exist")
else:
    print("Pin 14 not connected on GND")
