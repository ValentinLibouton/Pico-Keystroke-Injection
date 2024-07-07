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
            "F2": (0x3b,),
            "F3": (0x3c,),
            "F4": (0x3d,),
            "F5": (0x3e,),
            "F6": (0x3f,),
            "F7": (0x40,),
            "F8": (0x41,),
            "F9": (0x42,),
            "F10": (0x43,),
            "F11": (0x44,),
            "F12": (0x45,),
            "PRINT_SCREEN": (0x46,),
            "SCROLL_LOCK": (0x47,),
            "PAUSE": (0x48,),
            "INSERT": (0x49,),
            "HOME": (0x4a,),
            "PAGE_UP": (0x4b,),
            "DELETE": (0x4c,), # ok
            "END": (0x4d,),
            "PAGE_DOWN": (0x4e,),
            "RIGHT_ARROW": (0x4f,),
            "LEFT_ARROW": (0x50,),
            "DOWN_ARROW": (0x51,),
            "UP_ARROW": (0x52,),
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
            "a":            (0x14,),
            "b":            (0x05,),
            "c":            (0x06,),
            "d":            (0x07,),
            "e":            (0x08,),
            "f":            (0x09,),
            "g":            (0x0a,),
            "h":            (0x0b,),
            "i":            (0x0c,),
            "j":            (0x0d,),
            "k":            (0x0e,),
            "l":            (0x0f,),
            "m":            (0x33,),
            "n":            (0x11,),
            "o":            (0x12,),
            "p":            (0x13,),
            "q":            (0x04,),
            "r":            (0x15,),
            "s":            (0x16,),
            "t":            (0x17,),
            "u":            (0x18,),
            "v":            (0x19,),
            "w":            (0x1d,),
            "x":            (0x1b,),
            "y":            (0x1c,),
            "z":            (0x1a,),
            ",":            (0x10,),
            "&":            (0x1e,),
            "é":            (0x1f,),
            '"':            (0x20,),
            "'":            (0x21,),
            "(":            (0x22,),
            "§":            (0x23,),
            "è":            (0x24,),
            "!":            (0x25,),
            "ç":            (0x26,),
            "à":            (0x27,),
            ")":            (0x2d,),
            "-":            (0x2e,),
            "^":            ((0x2f,), (0x00,), (0x2f,)),
            "$":            (0x30,),
            "µ":            (0x31,),
            "ù":            (0x34,),
            "²":            (0x35,),
            ";":            (0x36,),
            ":":            (0x37,),
            "=":            (0x38,),
            "/":            (0x54,),
            "*":            (0x55,),
            "+":            (0x57,),
            "<":            (0x64,),
            "A":            (self.modifiers['Shift'], 0x14),
            "B":            (self.modifiers['Shift'], 0x05),
            "C":            (self.modifiers['Shift'], 0x06),
            "D":            (self.modifiers['Shift'], 0x07),
            "E":            (self.modifiers['Shift'], 0x08),
            "F":            (self.modifiers['Shift'], 0x09),
            "G":            (self.modifiers['Shift'], 0x0a),
            "H":            (self.modifiers['Shift'], 0x0b),
            "I":            (self.modifiers['Shift'], 0x0c),
            "J":            (self.modifiers['Shift'], 0x0d),
            "K":            (self.modifiers['Shift'], 0x0e),
            "L":            (self.modifiers['Shift'], 0x0f),
            "M":            (self.modifiers['Shift'], 0x33),
            "N":            (self.modifiers['Shift'], 0x11),
            "O":            (self.modifiers['Shift'], 0x12),
            "P":            (self.modifiers['Shift'], 0x13),
            "Q":            (self.modifiers['Shift'], 0x04),
            "R":            (self.modifiers['Shift'], 0x15),
            "S":            (self.modifiers['Shift'], 0x16),
            "T":            (self.modifiers['Shift'], 0x17),
            "U":            (self.modifiers['Shift'], 0x18),
            "V":            (self.modifiers['Shift'], 0x19),
            "W":            (self.modifiers['Shift'], 0x1d),
            "X":            (self.modifiers['Shift'], 0x1b),
            "Y":            (self.modifiers['Shift'], 0x1c),
            "Z":            (self.modifiers['Shift'], 0x1a),
            "?":            (self.modifiers['Shift'], 0x10),
            "1":            (self.modifiers['Shift'], 0x1e),
            "2":            (self.modifiers['Shift'], 0x1f),
            "3":            (self.modifiers['Shift'], 0x20),
            "4":            (self.modifiers['Shift'], 0x21),
            "5":            (self.modifiers['Shift'], 0x22),
            "6":            (self.modifiers['Shift'], 0x23),
            "7":            (self.modifiers['Shift'], 0x24),
            "8":            (self.modifiers['Shift'], 0x25),
            "9":            (self.modifiers['Shift'], 0x26),
            "0":            (self.modifiers['Shift'], 0x27),
            "°":            (self.modifiers['Shift'], 0x2d),
            "_":            (self.modifiers['Shift'], 0x2e),
            "¨":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x00), (self.modifiers['Shift'], 0x2f)),
            "£":            (self.modifiers['Shift'], 0x31),
            "%":            (self.modifiers['Shift'], 0x34),
            "³":            (self.modifiers['Shift'], 0x35),
            ".":            (self.modifiers['Shift'], 0x36),
            ">":            (self.modifiers['Shift'], 0x64),
            "\\":           (self.modifiers['AltGr'], 0x64),
            "|":            (self.modifiers['AltGr'], 0x1e),
            "@":            (self.modifiers['AltGr'], 0x1f),
            "#":            (self.modifiers['AltGr'], 0x20),
            "¼":            (self.modifiers['AltGr'], 0x21),
            "½":            (self.modifiers['AltGr'], 0x22),
            "{":            (self.modifiers['AltGr'], 0x26),
            "}":            (self.modifiers['AltGr'], 0x27),
            "[":            (self.modifiers['AltGr'], 0x2f),
            "]":            (self.modifiers['AltGr'], 0x30),
            "€":            (self.modifiers['AltGr'], 0x08),
            "”":            (self.modifiers['AltGr'], 0x05),
            "“":            (self.modifiers['AltGr'], 0x19),
            "¢":            (self.modifiers['AltGr'], 0x00),
            "»":            (self.modifiers['AltGr'], 0x1b),
            "«":            (self.modifiers['AltGr'], 0x1d),
            "`":            ((self.modifiers['AltGr'], 0x31), (0x00, 0x00), (self.modifiers['AltGr'], 0x31)),
            "´":            ((self.modifiers['AltGr'], 0x34), (0x00, 0x00), (self.modifiers['AltGr'], 0x34)),
            "~":            ((self.modifiers['AltGr'], 0x38), (0x00, 0x00), (self.modifiers['AltGr'], 0x38)),
            "¬":            (self.modifiers['AltGr'], 0x35),
            "¸":            ((self.modifiers['AltGr'], 0x2e), (0x00, 0x00), (self.modifiers['AltGr'], 0x2e)),
            "¶":            (self.modifiers['AltGr'], 0x15),
            "ŧ":            (self.modifiers['AltGr'], 0x17),
            "←":            (self.modifiers['AltGr'], 0x1c),
            "↓":            (self.modifiers['AltGr'], 0x18),
            "→":            (self.modifiers['AltGr'], 0x0c),
            "œ":            (self.modifiers['AltGr'], 0x12),
            "þ":            (self.modifiers['AltGr'], 0x13),
            "æ":            (self.modifiers['AltGr'], 0x04),
            "ß":            (self.modifiers['AltGr'], 0x16),
            "ð":            (self.modifiers['AltGr'], 0x07),
            "đ":            (self.modifiers['AltGr'], 0x09),
            "ŋ":            (self.modifiers['AltGr'], 0x0a),
            "ħ":            (self.modifiers['AltGr'], 0x0b),
            "ĸ":            (self.modifiers['AltGr'], 0x0e),
            "ł":            (self.modifiers['AltGr'], 0x0f),
            "─":            (self.modifiers['AltGr'], 0x36),
            "·":            (self.modifiers['AltGr'], 0x37),
            " ":            (0x00, 0x2c),
            "    ":         (0x00, 0x2b),
            "ä":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x14)),
            "ë":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x08)),
            "ẗ":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x17)),
            "ÿ":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x1c)),
            "ü":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x18)),
            "ï":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x0c)),
            "ö":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x12)),
            "ḧ":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x0b)),
            "ẅ":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x1d)),
            "ẍ":            ((self.modifiers['Shift'], 0x2f), (0x00, 0x1b)),
            "Ä":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x14)),
            "Ë":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x08)),
            "Ÿ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x1c)),
            "Ü":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x18)),
            "Ï":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x0c)),
            "Ö":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x12)),
            "Ḧ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x0b)),
            "Ẅ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x1d)),
            "Ẍ":            ((self.modifiers['Shift'], 0x2f), (self.modifiers['Shift'], 0x1b)),
            "â":            ((0x00, 0x2f), (0x00, 0x14)),
            "ẑ":            ((0x00, 0x2f), (0x00, 0x1a)),
            "ê":            ((0x00, 0x2f), (0x00, 0x08)),
            "ŷ":            ((0x00, 0x2f), (0x00, 0x1c)),
            "û":            ((0x00, 0x2f), (0x00, 0x18)),
            "î":            ((0x00, 0x2f), (0x00, 0x0c)),
            "ô":            ((0x00, 0x2f), (0x00, 0x12)),
            "ŝ":            ((0x00, 0x2f), (0x00, 0x16)),
            "ĝ":            ((0x00, 0x2f), (0x00, 0x0a)),
            "ĥ":            ((0x00, 0x2f), (0x00, 0x0b)),
            "ĵ":            ((0x00, 0x2f), (0x00, 0x0d)),
            "ŵ":            ((0x00, 0x2f), (0x00, 0x1d)),
            "ĉ":            ((0x00, 0x2f), (0x00, 0x06)),
            "Â":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x14)),
            "Ê":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x08)),
            "Ŷ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x1c)),
            "Û":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x18)),
            "Î":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x0c)),
            "Ô":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x12)),
            "Ŝ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x16)),
            "Ĝ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x0a)),
            "Ĥ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x0b)),
            "Ĵ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x0d)),
            "Ŵ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x1d)),
            "Ĉ":            ((0x00, 0x2f), (self.modifiers['Shift'], 0x06)),
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
