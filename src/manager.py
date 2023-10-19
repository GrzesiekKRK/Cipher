from menu import user_menu, code_decode, write_or_append, filename
from file_handler import FileHandler
import cipher
from buffer import Buffer, Text


class Manager:
    """Manage project"""

    def run_time(self) -> None:
        while True:
            choice = user_menu()
            self.perform_action(choice)

    def perform_action(self, choice):
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
                pass
            case "0":
                exit()

    @staticmethod
    def encrypt_decrypt():
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
    def file():
        try:
            name = filename()
            action = write_or_append()
            convert = Buffer.convert()
            if action == "write":
                creat_file = FileHandler(name, convert)
                creat_file.write()
            elif action == "append":
                old_data = FileHandler.read_file(name)
                for new in convert:
                    old_data["data"].append(new)
                creat_file = FileHandler(name, old_data)
                creat_file.write()
            else:
                print("Wrong input. Write or append")
        except FileNotFoundError:
            creat_file = FileHandler(name, convert)
            creat_file.write()

    @staticmethod
    def read_file():
        name = filename()
        try:
            one = FileHandler.read_file(name)
        except FileNotFoundError:
            print("File not found!!")
        else:
            for element in one["data"]:
                custom = Text(element["contents"], element["rot_type"], element["status"])
                Buffer.add(custom)
