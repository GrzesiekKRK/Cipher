"""Take all inputs in project and shows menu options"""


def show_menu() -> None:
    print(
            f"1.Show current in buffer\n"
            f"2.Encryption / Decryption\n"
            f"3.Load from file \n"
            f"4.Save data to file\n"
            f"0.Exit"
        )


def user_menu() -> str:
    show_menu()
    choice = input("\nWhich one?: ")
    return choice


def code_decode() -> str:
    """Choose 'Text' object from buffer to encrypt or decrypt"""
    while True:
        user = input("Choose which one to encrypt/ decrypt: ")
        return user


def write_or_append() -> str:
    mode = input("Write  or append to file?: ").lower()
    return mode


def filename() -> str:
    name = input("Filename: ")
    return f"{name}.json"
