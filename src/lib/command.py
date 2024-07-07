import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from lib.keyboard_layout import StringModeHandler, KeyboardLayoutBE, CommandModeHandler


class CommandProcessor:
    def __init__(self, filename, write_speed=0.03):
        self.filename = filename
        self.write_speed = write_speed
        self.history = []
        self.keyboard = Keyboard(usb_hid.devices)
        self.keyboard_layout = KeyboardLayoutBE(self.keyboard)
        self.string_mode_handler = StringModeHandler()
        self.command_mode_handler = CommandModeHandler()

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
        self.history.append(line)
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
        elif line.split()[0] in self.keyboard_layout.commands_layout():
            self.commands_mode(line)

    def string_mode(self, line):
        string = line[7:]
        print(f"String: {string}")
        self.string_mode_handler.string_mode(string=string, write_speed=self.write_speed)

    def delay_mode(self, line):
        """mili seconds"""
        delay_time = int(line.split()[1])
        time.sleep(delay_time / 1000.0)

    def write_mode(self, line):
        filename = line.split()[1]
        filename = "./inject/" + filename
        if not self.check_file(filename=filename):
            return

        with open(filename, "r") as f:
            for line in f:
                self.string_mode_handler.string_mode(string=line, write_speed=self.write_speed)
                self.command_mode_handler.commands_mode(commands=["ENTER"])


    def comment_mode(self, line):
        print(f"Comment: {line}")

    def replay_mode(self, line):
        _, times, num_lines = line.split()
        times = int(times)
        num_lines = int(num_lines)
        if num_lines > len(self.history)-1:
            print("Not enough history to replay")
            return

        commands_to_replay = self.history[-(num_lines+1):-1]
        print(f"Replaying {times} times the following commands: {commands_to_replay}")

        for _ in range(times):
            for command in commands_to_replay:
                self.process_line(command)

    def commands_mode(self, line):
        commands = line.split()
        self.command_mode_handler.commands_mode(commands=commands)


