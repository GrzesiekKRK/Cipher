from menu import user_action, code_decode, write_or_append, get_filename, hand_writen
from file_handler import FileHandler
import cipher
from buffer import Buffer, Text


class Manager:
    """Manage project"""

    def run_time(self) -> None:
        while True:
            choice = user_action()
            self.perform_action(choice)

    def perform_action(self, choice: str) -> None:
        match choice:
            case "1":
                Buffer.show_buffer()
            case "2":
                self.encrypt_decrypt()
            case "3":
                self.read_file()
            case "4":
                self.file()
            case "5":
                self.make_new_object()
            case "0":
                exit()

    @staticmethod
    def encrypt_decrypt() -> None:
        Buffer.show_buffer()
        user = code_decode()
        try:
            if int(user) <= len(Buffer.data):
                text = Buffer.data[int(user) - 1]
                cipher.get_rot(text)
            else:
                print("\nWrong object number\n")
        except ValueError:
            print("\nValue error\n")

    @staticmethod
    def file() -> None:
        # TODO import os os.isfile(path: str)
        name = get_filename()
        action = write_or_append()
        convert = Buffer.convert()
        try:
            if action == "write":
                creat_file = FileHandler(name, convert)
                creat_file.write()
            elif action == "append":
                old_data = FileHandler.read_file(name)
                for new in convert:
                    old_data["data"].append(new)
                creat_file = FileHandler(name, old_data)
                creat_file.append()
            else:
                print("Wrong input. Write or append")
        except FileNotFoundError:
            creat_file = FileHandler(name, convert)
            creat_file.write()

    @staticmethod
    def read_file() -> None:
        file_name = get_filename()
        try:
            data = FileHandler.read_file(file_name)
        except FileNotFoundError:
            print("File not found!!")
        else:
            Buffer.load_from_dict(data)

    @staticmethod
    def make_new_object():
        creator = hand_writen()
        custom = Text(contents=creator[0], rot_type=creator[1], status=creator[2])
        Buffer.add(custom)
