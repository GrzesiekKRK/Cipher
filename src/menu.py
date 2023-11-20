"""Take all inputs in project and shows menu options"""


def show_menu() -> None:
    print(
        f"1.Show current in buffer\n"
        f"2.Encryption / Decryption\n"
        f"3.Load from file \n"
        f"4.Save data to file\n"
        f"5.Write text and choose rot\n"
        f"0.Exit"
    )


def user_action() -> str:
    show_menu()
    choice = input("\nWhich one?: ")
    return choice


def code_decode() -> str:
    """Choose 'Text' object from buffer to encrypt or decrypt"""
    while True:
        user = input("Choose which one to encrypt/decrypt: ")
        return user


def write_or_append() -> str:
    mode = input("Write  or append to file?: ").lower()
    return mode


def get_filename() -> str:
    name = input("Filename (without extension): ")
    return f"{name}.json"


def hand_writen() -> list:
    while True:
        text = input("Text: ")
        rot = input("Spaces between letters(Rot): ")
        status = input("Status encrypt/decrypt: ")
        return [text, int(rot), status]
