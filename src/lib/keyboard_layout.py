import usb_hid
from adafruit_hid.keyboard import Keyboard
import time
class KeyboardLayoutBE:
    """Classe pour gérer la disposition du clavier belge."""

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.modifiers = {
            'Shift': 0xe1,
            'AltGr': 0xe6,
            'Alt': 0xe2
        }
    def commands_layout(self):
        layout = {
            "CTRL_LEFT": (0xe0,), # ok
            "SHIFT_LEFT": (self.modifiers['Shift'],), # ok
            "ALT_LEFT": (self.modifiers['Alt'],), # ok
            "WIN": (0xe3,), # ok
            "CTRL_RIGHT": (0xe4,), # ok
            "SHIFT_RIGHT": (self.modifiers['Shift'],), # ok
            "ALT_RIGHT": (self.modifiers['AltGr'],), # ok
            "ENTER": (0x28,), # ok
            "ESCAPE": (0x29,), # ok
            "BACK": (0x2a,), # ok
            "TAB": (0x2b,), # ok
            "SPACE": (0x2c,), # ok
            "CAPS_LOCK": (0x39,), # ok
            "F1": (0x3a,), # ok
            "F2": (0x3b,), # ok
            "F3": (0x3c,), # ok
            "F4": (0x3d,), # ok
            "F5": (0x3e,), # ok
            "F6": (0x3f,),
            "F7": (0x40,),
            "F8": (0x41,),
            "F9": (0x42,),
            "F10": (0x43,), # ok
            "F11": (0x44,), # ok
            "F12": (0x45,),
            "PRINT_SCREEN": (0x46,), # ok
            "SCROLL_LOCK": (0x47,),
            "PAUSE": (0x48,),
            "INSERT": (0x49,), # ok
            "HOME": (0x4a,), # ok
            "PAGE_UP": (0x4b,), # ok
            "DELETE": (0x4c,), # ok
            "END": (0x4d,), # ok
            "PAGE_DOWN": (0x4e,), # ok
            "RIGHT_ARROW": (0x4f,), # ok
            "LEFT_ARROW": (0x50,), # ok
            "DOWN_ARROW": (0x51,), # ok
            "UP_ARROW": (0x52,), # ok
            "NUM_LOCK": (0x53,),
            "MENU": (0x65,),
        }

        aliases = {
            "CONTROL": "CTRL_LEFT",
            "CTRL": "CTRL_LEFT",
            "SHIFT": "SHIFT_LEFT",
            "ALT": "ALT_LEFT",
            "CMD": "WIN",
            "DEL": "DELETE",
            "ALTGR": "ALT_RIGHT",
            "ALT_GR": "ALT_RIGHT",
            "ESC": "ESCAPE"
        }

        for alias, original in aliases.items():
            layout[alias] = layout[original]

        return layout


    def char_layout(self):
        """Retourne un dictionnaire de la disposition du clavier belge."""
        return {
            "a":            (0x14,), # ok
            "b":            (0x05,), # ok
            "c":            (0x06,), # ok
            "d":            (0x07,), # ok
            "e":            (0x08,), # ok
            "f":            (0x09,), # ok
            "g":            (0x0a,), # ok
            "h":            (0x0b,), # ok
            "i":            (0x0c,), # ok
            "j":            (0x0d,), # ok
            "k":            (0x0e,), # ok
            "l":            (0x0f,), # ok
            "m":            (0x33,), # ok
            "n":            (0x11,), # ok
            "o":            (0x12,), # ok
            "p":            (0x13,), # ok
            "q":            (0x04,), # ok
            "r":            (0x15,), # ok
            "s":            (0x16,), # ok
            "t":            (0x17,), # ok
            "u":            (0x18,), # ok
            "v":            (0x19,), # ok
            "w":            (0x1d,), # ok
            "x":            (0x1b,), # ok
            "y":            (0x1c,), # ok
            "z":            (0x1a,), # ok
            ",":            (0x10,), # ok
            "&":            (0x1e,), # ok
            "é":            (0x1f,), # ok
            '"':            (0x20,), # ok
            "'":            (0x21,), # ok
            "(":            (0x22,), # ok
            "§":            (0x23,), # ok
            "è":            (0x24,), # ok
            "!":            (0x25,), # ok
            "ç":            (0x26,), # ok
            "à":            (0x27,), # ok
            ")":            (0x2d,), # ok
            "-":            (0x2e,), # ok
            "^":            ((0x2f,), (0x00,), (0x2f,)), # ok
            "$":            (0x30,), # ok
            "µ":            (0x31,), # ok
            "ù":            (0x34,), # ok
            "²":            (0x35,), # ok
            ";":            (0x36,), # ok
            ":":            (0x37,), # ok
            "=":            (0x38,), # ok
            "/":            (0x54,), # ok
            "*":            (0x55,), # ok
            "+":            (0x57,), # ok
            "<":            (0x64,), # ok
            "A":            (self.modifiers['Shift'], 0x14), # ok
            "B":            (self.modifiers['Shift'], 0x05), # ok
            "C":            (self.modifiers['Shift'], 0x06), # ok
            "D":            (self.modifiers['Shift'], 0x07), # ok
            "E":            (self.modifiers['Shift'], 0x08), # ok
            "F":            (self.modifiers['Shift'], 0x09), # ok
            "G":            (self.modifiers['Shift'], 0x0a), # ok
            "H":            (self.modifiers['Shift'], 0x0b), # ok
            "I":            (self.modifiers['Shift'], 0x0c), # ok
            "J":            (self.modifiers['Shift'], 0x0d), # ok
            "K":            (self.modifiers['Shift'], 0x0e), # ok
            "L":            (self.modifiers['Shift'], 0x0f), # ok
            "M":            (self.modifiers['Shift'], 0x33), # ok
            "N":            (self.modifiers['Shift'], 0x11), # ok
            "O":            (self.modifiers['Shift'], 0x12), # ok
            "P":            (self.modifiers['Shift'], 0x13), # ok
            "Q":            (self.modifiers['Shift'], 0x04), # ok
            "R":            (self.modifiers['Shift'], 0x15), # ok
            "S":            (self.modifiers['Shift'], 0x16), # ok
            "T":            (self.modifiers['Shift'], 0x17), # ok
            "U":            (self.modifiers['Shift'], 0x18), # ok
            "V":            (self.modifiers['Shift'], 0x19), # ok
            "W":            (self.modifiers['Shift'], 0x1d), # ok
            "X":            (self.modifiers['Shift'], 0x1b), # ok
            "Y":            (self.modifiers['Shift'], 0x1c), # ok
            "Z":            (self.modifiers['Shift'], 0x1a), # ok
            "?":            (self.modifiers['Shift'], 0x10), # ok
            "1":            (self.modifiers['Shift'], 0x1e), # ok
            "2":            (self.modifiers['Shift'], 0x1f), # ok
            "3":            (self.modifiers['Shift'], 0x20), # ok
            "4":            (self.modifiers['Shift'], 0x21), # ok
            "5":            (self.modifiers['Shift'], 0x22), # ok
            "6":            (self.modifiers['Shift'], 0x23), # ok
            "7":            (self.modifiers['Shift'], 0x24), # ok
            "8":            (self.modifiers['Shift'], 0x25), # ok
            "9":            (self.modifiers['Shift'], 0x26), # ok
            "0":            (self.modifiers['Shift'], 0x27), # ok
            "°":            (self.modifiers['Shift'], 0x2d), # ok
            "_":            (self.modifiers['Shift'], 0x2e), # ok
            "¨":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x00), (self.modifiers['Shift'], 0x2f)), # ok
            "£":            (self.modifiers['Shift'], 0x31), # ok
            "%":            (self.modifiers['Shift'], 0x34), # ok
            "³":            (self.modifiers['Shift'], 0x35), # ok
            ".":            (self.modifiers['Shift'], 0x36), # ok
            ">":            (self.modifiers['Shift'], 0x64), # ok
            "\\":           (self.modifiers['AltGr'], 0x64), # ok
            "|":            (self.modifiers['AltGr'], 0x1e), # ok
            "@":            (self.modifiers['AltGr'], 0x1f), # ok
            "#":            (self.modifiers['AltGr'], 0x20), # ok
            "¼":            (self.modifiers['AltGr'], 0x21), # ok
            "½":            (self.modifiers['AltGr'], 0x22), # ok
            "{":            (self.modifiers['AltGr'], 0x26), # ok
            "}":            (self.modifiers['AltGr'], 0x27), # ok
            "[":            (self.modifiers['AltGr'], 0x2f), # ok
            "]":            (self.modifiers['AltGr'], 0x30), # ok
            "€":            (self.modifiers['AltGr'], 0x08), # ok
            "”":            (self.modifiers['AltGr'], 0x05), # no...
            "“":            (self.modifiers['AltGr'], 0x19), # no...
            "¢":            (self.modifiers['AltGr'], 0x00), # no...
            "»":            (self.modifiers['AltGr'], 0x1b), # ok
            "«":            (self.modifiers['AltGr'], 0x1d), # ok
            "`":            ((self.modifiers['AltGr'], 0x31), (0x00, 0x00), (self.modifiers['AltGr'], 0x31)), # ok
            "´":            ((self.modifiers['AltGr'], 0x34), (0x00, 0x00), (self.modifiers['AltGr'], 0x34)), # ok
            "~":            ((self.modifiers['AltGr'], 0x38), (0x00, 0x00), (self.modifiers['AltGr'], 0x38)), # ok
            "¬":            (self.modifiers['AltGr'], 0x35), # ok
            "¸":            ((self.modifiers['AltGr'], 0x2e), (0x00, 0x00), (self.modifiers['AltGr'], 0x2e)), # ok
            "¶":            (self.modifiers['AltGr'], 0x15), # ok
            "ŧ":            (self.modifiers['AltGr'], 0x17), # ok
            "←":            (self.modifiers['AltGr'], 0x1c), # ok
            "↓":            (self.modifiers['AltGr'], 0x18), # ok
            "→":            (self.modifiers['AltGr'], 0x0c), # ok
            "œ":            (self.modifiers['AltGr'], 0x12), # ok
            "þ":            (self.modifiers['AltGr'], 0x13), # ok
            "æ":            (self.modifiers['AltGr'], 0x04), # ok
            "ß":            (self.modifiers['AltGr'], 0x16), # ok
            "ð":            (self.modifiers['AltGr'], 0x07), # ok
            "đ":            (self.modifiers['AltGr'], 0x09), # ok
            "ŋ":            (self.modifiers['AltGr'], 0x0a), # ok
            "ħ":            (self.modifiers['AltGr'], 0x0b), # ok
            "ĸ":            (self.modifiers['AltGr'], 0x0e), # ok
            "ł":            (self.modifiers['AltGr'], 0x0f), # ok
            "─":            (self.modifiers['AltGr'], 0x36), # no...
            "·":            (self.modifiers['AltGr'], 0x37), # no...
            " ":            (0x2c,), # ok
            "    ":         (0x2b,), # ok
            "ä":            ((self.modifiers['Shift'], 0x2f), (0x14,)), # ok
            "ë":            ((self.modifiers['Shift'], 0x2f), (0x08,)), # ok
            "ẗ":            ((self.modifiers['Shift'], 0x2f), (0x17,)), # ok
            "ÿ":            ((self.modifiers['Shift'], 0x2f), (0x1c,)), # ok
            "ü":            ((self.modifiers['Shift'], 0x2f), (0x18,)), # ok
            "ï":            ((self.modifiers['Shift'], 0x2f), (0x0c,)), # ok
            "ö":            ((self.modifiers['Shift'], 0x2f), (0x12,)), # ok
            "ḧ":            ((self.modifiers['Shift'], 0x2f), (0x0b,)), # ok
            "ẅ":            ((self.modifiers['Shift'], 0x2f), (0x1d,)), # ok
            "ẍ":            ((self.modifiers['Shift'], 0x2f), (0x1b,)), # ok
            "Ä":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x14)), # ok
            "Ë":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x08)), # ok
            "Ÿ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x1c)), # ok
            "Ü":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x18)), # ok
            "Ï":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x0c)), # ok
            "Ö":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x12)), # ok
            "Ḧ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x0b)), # ok
            "Ẅ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x1d)), # ok
            "Ẍ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x1b)), # ok
            "â":            ((0x2f,), (0x14,)),
            "ẑ":            ((0x2f,), (0x1a,)),
            "ê":            ((0x2f,), (0x08,)),
            "ŷ":            ((0x2f,), (0x1c,)),
            "û":            ((0x2f,), (0x18,)),
            "î":            ((0x2f,), (0x0c,)),
            "ô":            ((0x2f,), (0x12,)),
            "ŝ":            ((0x2f,), (0x16,)),
            "ĝ":            ((0x2f,), (0x0a,)),
            "ĥ":            ((0x2f,), (0x0b,)),
            "ĵ":            ((0x2f,), (0x0d,)),
            "ŵ":            ((0x2f,), (0x1d,)),
            "ĉ":            ((0x2f,), (0x06,)),
            "Â":            ((0x2f,), (self.modifiers['Shift'], 0x14)),
            "Ê":            ((0x2f,), (self.modifiers['Shift'], 0x08)),
            "Ŷ":            ((0x2f,), (self.modifiers['Shift'], 0x1c)),
            "Û":            ((0x2f,), (self.modifiers['Shift'], 0x18)),
            "Î":            ((0x2f,), (self.modifiers['Shift'], 0x0c)),
            "Ô":            ((0x2f,), (self.modifiers['Shift'], 0x12)),
            "Ŝ":            ((0x2f,), (self.modifiers['Shift'], 0x16)),
            "Ĝ":            ((0x2f,), (self.modifiers['Shift'], 0x0a)),
            "Ĥ":            ((0x2f,), (self.modifiers['Shift'], 0x0b)),
            "Ĵ":            ((0x2f,), (self.modifiers['Shift'], 0x0d)),
            "Ŵ":            ((0x2f,), (self.modifiers['Shift'], 0x1d)),
            "Ĉ":            ((0x2f,), (self.modifiers['Shift'], 0x06)),
        }

    def type_character(self, character):
        """Tape le caractère donné en utilisant la disposition du clavier belge."""
        keycode = self.char_layout().get(character)
        if keycode:
            if isinstance(keycode[0], tuple):
                for sub_keycode in keycode:
                    self.keyboard.press(*sub_keycode)
                    self.keyboard.release_all()
            else:
                self.keyboard.press(*keycode)
                self.keyboard.release_all()
        else:
            print(f"Character {character} not found in keyboard layout.")

    def type_commands(self, commands):
        print(str(commands))
        keycode_list = []
        for command in commands:
            keycode = self.commands_layout().get(command) or self.char_layout().get(command)
            if keycode:
                keycode_list.append(keycode)
            else:
                print(f"Command {command} not found in keyboard layout.")
                self.keyboard.release_all()
                return
        print(f"Keycode: {keycode_list}")
        for keycode in keycode_list:
            self.keyboard.press(*keycode)

        self.keyboard.release_all()







class StringModeHandler:
    """Classe pour gérer la saisie en mode chaîne."""

    def __init__(self):
        self.keyboard = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutBE(self.keyboard)
    
    def string_mode(self, string, write_speed):
        """Tape la chaîne de caractères donnée."""
        for character in string:
            self.layout.type_character(character)
            time.sleep(write_speed)

class CommandModeHandler:
    """Classe pour gérer la saisie en mode commandes."""

    def __init__(self):
        self.keyboard = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutBE(self.keyboard)

    def commands_mode(self, commands:list):
        self.layout.type_commands(commands=commands)
