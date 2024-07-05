from src.lib.adafruit_hid.keyboard_layout_base import KeyboardLayoutBase


class KeyboardLayoutBE(KeyboardLayoutBase):
    """Map ASCII characters to appropriate keypresses on a standard US PC keyboard.

    Non-ASCII characters and most control characters will raise an exception.
    """

    # The ASCII_TO_KEYCODE bytes object is used as a table to maps ASCII 0-127
    # to the corresponding # keycode on a US 104-key keyboard.
    # The user should not normally need to use this table,
    # but it is not marked as private.
    #
    # Because the table only goes to 127, we use the top bit of each byte (ox80) to indicate
    # that the shift key should be pressed. So any values 0x{8,9,a,b}* are shifted characters.
    #
    # The Python compiler will concatenate all these bytes literals into a single bytes object.
    # Micropython/CircuitPython will store the resulting bytes constant in flash memory
    # if it's in a .mpy file, so it doesn't use up valuable RAM.
    #
    # \x00 entries have no keyboard key and so won't be sent.
    ASCII_TO_KEYCODE = (
        b"\x00"  # NUL Todo
        b"\x00"  # SOH Todo
        b"\x00"  # STX Todo
        b"\x00"  # ETX Todo
        b"\x00"  # EOT Todo
        b"\x00"  # ENQ Todo
        b"\x00"  # ACK Todo
        b"\x00"  # BEL \a Todo
        b"\x2a"  # BS BACKSPACE \b Todo
        b"\x2b"  # TAB \t Todo
        b"\x28"  # LF \n Todo
        b"\x00"  # VT \v Todo
        b"\x00"  # FF \f Todo
        b"\x00"  # CR \r Todo
        b"\x00"  # SO Todo
        b"\x00"  # SI Todo
        b"\x00"  # DLE Todo
        b"\x00"  # DC1 Todo
        b"\x00"  # DC2 Todo
        b"\x00"  # DC3 Todo
        b"\x00"  # DC4 Todo
        b"\x00"  # NAK Todo
        b"\x00"  # SYN Todo
        b"\x00"  # ETB Todo
        b"\x00"  # CAN Todo
        b"\x00"  # EM Todo
        b"\x00"  # SUB Todo
        b"\x29"  # ESC Todo
        b"\x00"  # FS Todo
        b"\x00"  # GS Todo
        b"\x00"  # RS Todo
        b"\x00"  # US Todo
        b"\x2c"  # SPACE Todo
        b"\x9e"  # ! Todo
        b"\xb4"  # " Todo
        b"\xa0"  # # Todo
        b"\xa1"  # $ Todo
        b"\xa2"  # % Todo
        b"\xa4"  # & Todo
        b"\x34"  # ' Todo
        b"\xa6"  # ( Todo
        b"\xa7"  # ) Todo
        b"\xb0"  # *
        b"\xb8"  # +
        b"\x10"  # ,
        b"\x2e"  # -
        b"\xb6"  # .
        b"\xb7"  # /
        b"\xa7"  # 0
        b"\x9e"  # 1
        b"\x9f"  # 2
        b"\xa0"  # 3
        b"\xa1"  # 4
        b"\xa2"  # 5
        b"\xa3"  # 6
        b"\xa4"  # 7
        b"\xa5"  # 8
        b"\xa6"  # 9
        b"\x37"  # :
        b"\x36"  # ;
        b"\x64"  # <
        b"\x38"  # =
        b"\xe4"  # >
        b"\x90"  # ?
        b"\xe0\x38|\x03"  # @ Todo I'm here
        b"\x94"  # A 
        b"\x85"  # B 
        b"\x86"  # C 
        b"\x87"  # D 
        b"\x88"  # E 
        b"\x89"  # F 
        b"\x8a"  # G 
        b"\x8b"  # H 
        b"\x8c"  # I 
        b"\x8d"  # J 
        b"\x8e"  # K 
        b"\x8f"  # L 
        b"\xb3"  # M 
        b"\x91"  # N 
        b"\x92"  # O 
        b"\x93"  # P 
        b"\x84"  # Q 
        b"\x95"  # R 
        b"\x96"  # S 
        b"\x97"  # T 
        b"\x98"  # U 
        b"\x99"  # V 
        b"\x9d"  # W 
        b"\x9b"  # X 
        b"\x9c"  # Y 
        b"\x9a"  # Z 
        b"\x2f"  # [ Todo
        b"\x31"  # \ Todo
        b"\x30"  # ] Todo
        b"\xa3"  # ^ Todo
        b"\xad"  # _ Todo
        b"\x35"  # ` Todo
        b"\x14"  # a
        b"\x05"  # b
        b"\x06"  # c
        b"\x07"  # d
        b"\x08"  # e
        b"\x09"  # f
        b"\x0a"  # g
        b"\x0b"  # h
        b"\x0c"  # i
        b"\x0d"  # j
        b"\x0e"  # k
        b"\x0f"  # l
        b"\x33"  # m
        b"\x11"  # n
        b"\x12"  # o
        b"\x13"  # p
        b"\x04"  # q
        b"\x15"  # r
        b"\x16"  # s
        b"\x17"  # t
        b"\x18"  # u
        b"\x19"  # v
        b"\x1d"  # w
        b"\x1b"  # x
        b"\x1c"  # y
        b"\x1a"  # z
        b"\xaf"  # { Todo
        b"\xb1"  # | Todo
        b"\xb0"  # } Todo
        b"\xb5"  # ~ Todo
        b"\x4c"  # DEL DELETE Todo
    )


KeyboardLayout = KeyboardLayoutBE
