import time

from lib.keyboard_layout import StringModeHandler, KeyboardLayoutBE


class CommandProcessor:
    def __init__(self, filename, write_speed=0.03):
        self.filename = filename
        self.write_speed = write_speed
        self.replay_list = []
        self.string_mode_handler = StringModeHandler()
        self.process_commands()

    def process_commands(self):
        if not self.check_file(self.filename):
            return

        with open(self.filename, "r") as f:
            for line in f:
                self.process_line(line)

    def check_file(self, filename):
        try:
            with open(filename, "r") as f:
                if len(f.read()) == 0:
                    print("File empty")
                    return False
                else:
                    print("File not empty")
                    return True
        except IOError:
            print("Check_file: File doesn't exist")
            return False
        except Exception as e:
            print(f"Check_file: Unknown error {e}")
            return False

    def process_line(self, line):
        if line == "\n":
            print("Blank line")
        elif line.split()[0] == "STRING":
            self.string_mode(line)
        elif line.split()[0] == "DELAY":
            self.delay_mode(line)
        elif line.split()[0] == "WRITE":
            self.write_mode(line)
        elif line.split()[0] == "#":
            self.comment_mode(line)
        elif line.split()[0] == "REPLAY":
            self.replay_mode(line)
        elif line.split()[0] in KeyboardLayoutBE.belgian_layout(): # si c'est une commande dans le dictionnaire et qui n'est pas un caractère
            self.command_mode(line)
        self.replay_list.append(line)

    def string_mode(self, line):
        string = line[7:]
        print(f"String: {string}")
        self.string_mode_handler.string_mode(string=string, write_speed=self.write_speed)

    def delay_mode(self, line):
        delay_time = int(line.split()[1])
        time.sleep(delay_time / 1000.0)

    def write_mode(self, line):
        raise NotImplementedError

    def comment_mode(self, line):
        print(f"Comment: {line}")

    def replay_mode(self, line):
        raise NotImplementedError

    def command_mode(self, line):
        raise NotImplementedError


