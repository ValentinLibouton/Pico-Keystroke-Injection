class KeyboardLayoutBE:
    """Classe pour gérer la disposition du clavier belge."""

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.modifiers = {
            'Shift': 0xe1,
            'AltGr': 0xe6
        }

    def belgian_layout(self):
        """Retourne un dictionnaire de la disposition du clavier belge."""
        return {
            "CTRL_LEFT":    (0x01, 0x00),
            "SHIFT_LEFT":   (0x02, 0x00),
            "ALT_LEFT":     (0x04, 0x00),
            "WIN":          (0x08, 0x00),
            "CTRL_RIGHT":   (0x10, 0x00),
            "SHIFT_RIGHT":  (self.modifiers['Shift'], 0x00),
            "ALT_RIGHT":    (self.modifiers['AltGr'], 0x00),
            "ENTER":        (0x00, 0x28),
            "ESCAPE":       (0x00, 0x29),
            "BACK":         (0x00, 0x2A),
            "TAB":          (0x00, 0x2B),
            "SPACE":        (0x00, 0x2C),
            "CAPS_LOCK":    (0x00, 0x39),
            "F1":           (0x00, 0x3A),
            "F2":           (0x00, 0x3B),
            "F3":           (0x00, 0x3C),
            "F4":           (0x00, 0x3D),
            "F5":           (0x00, 0x3E),
            "F6":           (0x00, 0x3F),
            "F7":           (0x00, 0x40),
            "F8":           (0x00, 0x41),
            "F9":           (0x00, 0x42),
            "F10":          (0x00, 0x43),
            "F11":          (0x00, 0x44),
            "F12":          (0x00, 0x45),
            "PRINT_SCREEN": (0x00, 0x46),
            "SCROLL_LOCK":  (0x00, 0x47),
            "PAUSE":        (0x00, 0x48),
            "INSERT":       (0x00, 0x49),
            "HOME":         (0x00, 0x4A),
            "PAGE_UP":      (0x00, 0x4B),
            "DELETE":       (0x00, 0x4C),
            "END":          (0x00, 0x4D),
            "PAGE_DOWN":    (0x00, 0x4E),
            "RIGHT_ARROW":  (0x00, 0x4F),
            "LEFT_ARROW":   (0x00, 0x50),
            "DOWN_ARROW":   (0x00, 0x51),
            "UP_ARROW":     (0x00, 0x52),
            "NUM_LOCK":     (0x00, 0x53),
            "MENU":         (0x00, 0x65),
            'a':            (0x00, 0x14),  # a
            'b':            (0x00, 0x05),  # b
            'c':            (0x00, 0x06),  # c
            'd':            (0x00, 0x07),  # d
            'e':            (0x00, 0x08),  # e
            'f':            (0x00, 0x09),  # f
            'g':            (0x00, 0x0A),  # g
            'h':            (0x00, 0x0B),  # h
            'i':            (0x00, 0x0C),  # i
            'j':            (0x00, 0x0D),  # j
            'k':            (0x00, 0x0E),  # k
            'l':            (0x00, 0x0F),  # l
            'm':            (0x00, 0x33),  # m
            'n':            (0x00, 0x11),  # n
            'o':            (0x00, 0x12),  # o
            'p':            (0x00, 0x13),  # p
            'q':            (0x00, 0x04),  # q
            'r':            (0x00, 0x15),  # r
            's':            (0x00, 0x16),  # s
            't':            (0x00, 0x17),  # t
            'u':            (0x00, 0x18),  # u
            'v':            (0x00, 0x19),  # v
            'w':            (0x00, 0x1D),  # w
            'x':            (0x00, 0x1B),  # x
            'y':            (0x00, 0x1C),  # y
            'z':            (0x00, 0x1A),  # z
            ',':            (0x00, 0x10),  # ,
            '&':            (0x00, 0x1E),  # &
            'é':            (0x00, 0x1F),  # é
            '"':            (0x00, 0x20),  # "
            '\'':           (0x00, 0x21),  # '
            '(':            (0x00, 0x22),  # (
            '§':            (0x00, 0x23),  # §
            'è':            (0x00, 0x24),  # è
            '!':            (0x00, 0x25),  # !
            'ç':            (0x00, 0x26),  # ç
            'à':            (0x00, 0x27),  # à
            ')':            (0x00, 0x2D),  # )
            '-':            (0x00, 0x2E),  # -
            '^':            ((0x00, 0x2F), (0x00, 0x00), (0x00, 0x2F)),  # ^
            '$':            (0x00, 0x30),  # $
            'µ':            (0x00, 0x31),  # µ
            'ù':            (0x00, 0x34),  # ù
            '²':            (0x00, 0x35),  # ²
            ';':            (0x00, 0x36),  # ;
            ':':            (0x00, 0x37),  # :
            '=':            (0x00, 0x38),  # =
            '/':            (0x00, 0x54),  # /
            '*':            (0x00, 0x55),  # *
            '+':            (0x00, 0x57),  # +
            '<':            (0x00, 0x64),  # <
            'A':            (self.modifiers['Shift'], 0x14),  # Shift + a
            'B':            (self.modifiers['Shift'], 0x05),  # Shift + b
            'C':            (self.modifiers['Shift'], 0x06),  # Shift + c
            'D':            (self.modifiers['Shift'], 0x07),  # Shift + d
            'E':            (self.modifiers['Shift'], 0x08),  # Shift + e
            'F':            (self.modifiers['Shift'], 0x09),  # Shift + f
            'G':            (self.modifiers['Shift'], 0x0A),  # Shift + g
            'H':            (self.modifiers['Shift'], 0x0B),  # Shift + h
            'I':            (self.modifiers['Shift'], 0x0C),  # Shift + i
            'J':            (self.modifiers['Shift'], 0x0D),  # Shift + j
            'K':            (self.modifiers['Shift'], 0x0E),  # Shift + k
            'L':            (self.modifiers['Shift'], 0x0F),  # Shift + l
            'M':            (self.modifiers['Shift'], 0x33),  # Shift + m
            'N':            (self.modifiers['Shift'], 0x11),  # Shift + n
            'O':            (self.modifiers['Shift'], 0x12),  # Shift + o
            'P':            (self.modifiers['Shift'], 0x13),  # Shift + p
            'Q':            (self.modifiers['Shift'], 0x04),  # Shift + q
            'R':            (self.modifiers['Shift'], 0x15),  # Shift + r
            'S':            (self.modifiers['Shift'], 0x16),  # Shift + s
            'T':            (self.modifiers['Shift'], 0x17),  # Shift + t
            'U':            (self.modifiers['Shift'], 0x18),  # Shift + u
            'V':            (self.modifiers['Shift'], 0x19),  # Shift + v
            'W':            (self.modifiers['Shift'], 0x1D),  # Shift + w
            'X':            (self.modifiers['Shift'], 0x1B),  # Shift + x
            'Y':            (self.modifiers['Shift'], 0x1C),  # Shift + y
            'Z':            (self.modifiers['Shift'], 0x1A),  # Shift + z
            '?':            (self.modifiers['Shift'], 0x10),  # Shift + ,
            '1':            (self.modifiers['Shift'], 0x1E),  # Shift + &
            '2':            (self.modifiers['Shift'], 0x1F),  # Shift + é
            '3':            (self.modifiers['Shift'], 0x20),  # Shift + "
            '4':            (self.modifiers['Shift'], 0x21),  # Shift + '
            '5':            (self.modifiers['Shift'], 0x22),  # Shift + (
            '6':            (self.modifiers['Shift'], 0x23),  # Shift + §
            '7':            (self.modifiers['Shift'], 0x24),  # Shift + è
            '8':            (self.modifiers['Shift'], 0x25),  # Shift + !
            '9':            (self.modifiers['Shift'], 0x26),  # Shift + ç
            '0':            (self.modifiers['Shift'], 0x27),  # Shift + à
            '°':            (self.modifiers['Shift'], 0x2D),  # Shift + )
            '_':            (self.modifiers['Shift'], 0x2E),  # Shift + -
            '¨':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x00), (self.modifiers['Shift'], 0x2F)),  # Shift + ^, exception
            '£':            (self.modifiers['Shift'], 0x31),  # Shift + µ
            '%':            (self.modifiers['Shift'], 0x34),  # Shift + ù
            '³':            (self.modifiers['Shift'], 0x35),  # Shift + ²
            '.':            (self.modifiers['Shift'], 0x36),  # Shift + ;
            '>':            (self.modifiers['Shift'], 0x64),  # Shift + <
            '\\':           (self.modifiers['AltGr'], 0x64),  # AltGr + <
            '|':            (self.modifiers['AltGr'], 0x1E),  # AltGr + &
            '@':            (self.modifiers['AltGr'], 0x1F),  # AltGr + é
            '#':            (self.modifiers['AltGr'], 0x20),  # AltGr + "
            '¼':            (self.modifiers['AltGr'], 0x21),  # AltGr + '
            '½':            (self.modifiers['AltGr'], 0x22),  # AltGr + (
            '{':            (self.modifiers['AltGr'], 0x26),  # AltGr + ç
            '}':            (self.modifiers['AltGr'], 0x27),  # AltGr + à
            '[':            (self.modifiers['AltGr'], 0x2F),  # AltGr + ^
            ']':            (self.modifiers['AltGr'], 0x30),  # AltGr + $
            '€':            (self.modifiers['AltGr'], 0x08),  # AltGr + e
            '”':            (self.modifiers['AltGr'], 0x05),  # AltGr + b
            '“':            (self.modifiers['AltGr'], 0x19),  # AltGr + v
            '¢':            (self.modifiers['AltGr'], 0x06),  # AltGr + c
            '»':            (self.modifiers['AltGr'], 0x1B),  # AltGr + x
            '«':            (self.modifiers['AltGr'], 0x1D),  # AltGr + w
            '`':            ((self.modifiers['AltGr'], 0x31), (0x00, 0x00), (self.modifiers['AltGr'], 0x31)),  # AltGr + µ, exception
            '´':            ((self.modifiers['AltGr'], 0x34), (0x00, 0x00), (self.modifiers['AltGr'], 0x34)),  # AltGr + ù, exception
            '~':            ((self.modifiers['AltGr'], 0x38), (0x00, 0x00), (self.modifiers['AltGr'], 0x38)),  # AltGr + =, exception
            '¬':            (self.modifiers['AltGr'], 0x35),  # AltGr + ²
            '¸':            ((self.modifiers['AltGr'], 0x2E), (0x00, 0x00), (self.modifiers['AltGr'], 0x2E)),  # AltGr + -, exception
            '¶':            (self.modifiers['AltGr'], 0x15),  # AltGr + r
            'ŧ':            (self.modifiers['AltGr'], 0x17),  # AltGr + t
            '←':            (self.modifiers['AltGr'], 0x1C),  # AltGr + y
            '↓':            (self.modifiers['AltGr'], 0x18),  # AltGr + u
            '→':            (self.modifiers['AltGr'], 0x0C),  # AltGr + i
            'œ':            (self.modifiers['AltGr'], 0x12),  # AltGr + o
            'þ':            (self.modifiers['AltGr'], 0x13),  # AltGr + p
            'æ':            (self.modifiers['AltGr'], 0x04),  # AltGr + q
            'ß':            (self.modifiers['AltGr'], 0x16),  # AltGr + s
            'ð':            (self.modifiers['AltGr'], 0x07),  # AltGr + d
            'đ':            (self.modifiers['AltGr'], 0x09),  # AltGr + f
            'ŋ':            (self.modifiers['AltGr'], 0x0A),  # AltGr + g
            'ħ':            (self.modifiers['AltGr'], 0x0B),  # AltGr + h
            "ĸ":            (self.modifiers['AltGr'], 0x0E),  # AltGr + k
            'ł':            (self.modifiers['AltGr'], 0x0F),  # AltGr + l
            '─':            (self.modifiers['AltGr'], 0x36),
            '·':            (self.modifiers['AltGr'], 0x37),  # AltGr + !
            ' ':            (0x00, 0x2C),  # SPACE
            '    ':         (0x00, 0x2B),  # TAB
            'ä':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x14)),  # ä
            'ë':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x08)),  # ë
            'ẗ':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x17)),  # ẗ
            'ÿ':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x1C)),  # ÿ
            'ü':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x18)),  # ü
            'ï':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x0C)),  # ï
            'ö':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x12)),  # ö
            'ḧ':            ((self.modifiers['Shift'], 0x2F), (0x00, 0X0B)),  # ḧ
            'ẅ':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x1D)),  # ẅ
            'ẍ':            ((self.modifiers['Shift'], 0x2F), (0x00, 0x1B)),  # ẍ
            'Ä':            ((self.modifiers['Shift'], 0x2F), (self.modifiers['Shift'], 0x14)),  # Ä
            'Ë':            ((self.modifiers['Shift'], 0x2F), (self.modifiers['Shift'], 0x08)),  # Ë
            'Ÿ':            ((self.modifiers['Shift'], 0x2F), (self.modifiers['Shift'], 0x1C)),  # Ÿ
            'Ü':            ((self.modifiers['Shift'], 0x2F), (self.modifiers['Shift'], 0x18)),  # Ü
            'Ï':            ((self.modifiers['Shift'], 0x2F), (self.modifiers['Shift'], 0x0C)),  # Ï todo here
            'Ö':            ((self.modifiers['Shift'], 0x2F), (self.modifiers['Shift'], 0x12)),  # Ö
            'Â':            ((0x00, 0x47), (self.modifiers['Shift'], 0x14)),  # Â
            'Ê':            ((0x00, 0x47), (self.modifiers['Shift'], 0x08)),  # Ê
            'Û':            ((0x00, 0x47), (self.modifiers['Shift'], 0x18)),  # Û
            'Î':            ((0x00, 0x47), (self.modifiers['Shift'], 0x0C)),  # Î
            'Ô':            ((0x00, 0x47), (self.modifiers['Shift'], 0x12)),  # Ô
            'Ŝ':            ((0x00, 0x47), (self.modifiers['Shift'], 0x16)),  # Ŝ
            'Ĝ':            ((0x00, 0x47), (self.modifiers['Shift'], 0x0A)),  # Ĝ
            'Ĵ':            ((0x00, 0x47), (self.modifiers['Shift'], 0x0D)),  # Ĵ
            'ŵ':            ((0x00, 0x47), (self.modifiers['Shift'], 0x1D)),  # ŵ
            'ĉ':            ((0x00, 0x47), (self.modifiers['Shift'], 0x06)),  # ĉ
        }

    def type_character(self, character):
        """Tape le caractère donné en utilisant la disposition du clavier belge."""
        keycode = self.belgian_layout().get(character)
        if keycode:
            if isinstance(keycode[0], tuple):
                for sub_keycode in keycode:
                    self.keyboard.press(*sub_keycode)
            else:
                self.keyboard.press(*keycode)
            self.keyboard.release_all()
        else:
            print(f"Character {character} not found in keyboard layout.")



class StringModeHandler:
    """Classe pour gérer la saisie en mode chaîne."""

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.layout = KeyboardLayoutBE(keyboard)

    def string_mode(self, string):
        """Tape la chaîne de caractères donnée."""
        for character in string:
            self.layout.type_character(character)

