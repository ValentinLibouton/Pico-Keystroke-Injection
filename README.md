# Pico-Keystroke-Injection
Pico-Keystroke-Injection

## Requirements

    Python 3.x
    usb_hid library
    Adafruit HID library (for Keyboard functionality)
    A supported microcontroller (e.g., Raspberry Pi Pico) with CircuitPython

## Installation
1. Install CircuitPython on your microcontroller: [https://circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/)
2. Download adafruit_hid [https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid)
3. Copy `adafruit_hid` folder, `commands.py`, `keyboard_layout.py` in `lib` folder in Pico
4. Copy `code.py` in `CIRCUITPY` folder
5. Create inject folder in `CIRCUITPY` folder
6. Copy the `inject.txt` file and the files you want to write with WRITE command in `inject` folder

## Usage
1. Create a file named `inject.txt` in the `./inject` directory and strings you want to process

## Example
With a file named some_text.txt containing:
```
Dear Sir or Madam,

This is the text that will be written

Best regards,
```
In inject.txt, for example, write:
```shell
STRING Hello World!
ENTER
STRING After this key ENTER for a return to the line I greet you
ENTER
STRING Now i sleep during 1 seconds
ENTER
DELAY 1000
STRING and i continue
ENTER
REPLAY 2 5
WRITE some_text.txt
STRING End !
```