import time
import os
from lib.command import CommandProcessor
import board
import digitalio


# Configuration de la broche pour vérifier l'état du pin 14 (GP10)
pin = digitalio.DigitalInOut(board.GP10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

number_of_runs = 1
i = 0
inject_file = "inject.txt"
while i < number_of_runs:
    time.sleep(2)
    if not pin.value:
        if inject_file in os.listdir("./inject"):
            i += 1
            CommandProcessor(filename="./inject/"+inject_file, write_speed=0.001)
        else:
            print("Inject file does not exist")
    else:
        print("Pin 14 not connected on GND")
