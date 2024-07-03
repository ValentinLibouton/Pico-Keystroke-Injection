import os
from lib.command import CommandProcessor
import board
import digitalio


# Configuration de la broche pour vérifier l'état du pin 14 (GP10)
pin = digitalio.DigitalInOut(board.GP10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

print("Initial pin value (should be high if not connected to GND):", pin.value)

inject_file = "inject.txt"

if not pin.value:
    if inject_file in os.listdir():
        CommandProcessor(filename=inject_file)
    else:
        print("Inject file does not exist")
else:
    print("Pin 14 not connected on GND")