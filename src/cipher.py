from abc import ABC, abstractmethod
import string
from buffer import Text


class Rot(ABC):
    """Logic of encryption and decryption"""
    @abstractmethod
    def encrypt(self, text: Text):
        ...

    @abstractmethod
    def decrypt(self, text: Text):
        ...


def get_rot(text: Text) -> None:
    code13 = Rot13()
    code47 = Rot47()
    if text.rot_type == 13:
        if text.status.lower() == "decrypted":
            code13.encrypt(text)
        else:
            code13.decrypt(text)
    elif text.rot_type == 47:
        if text.status.lower() == "decrypted":
            code47.encrypt(text)
        else:
            code47.decrypt(text)


class Rot13(Rot):
    def encrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[13:] + alphabet[:13]
        tabel = str.maketrans(alphabet, char_table)
        text.status = "Encrypted"
        text.contents = text.contents.lower().translate(tabel)
        print(f"Encryption completed\n {text}")

    def decrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[-13:] + alphabet[:-13]
        tabel = str.maketrans(alphabet, char_table)
        text.status = "Decrypted"
        text.contents = text.contents.lower().translate(tabel)
        print(f"Decryption completed\n {text}")


class Rot47(Rot):
    def encrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[21:] + alphabet[:21]
        tabel = str.maketrans(alphabet, char_table)
        text.status = "Encrypted"
        text.contents = text.contents.lower().translate(tabel)
        print(f"Encryption completed\n {text}")

    def decrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[-21:] + alphabet[:-21]
        tabel = str.maketrans(alphabet, char_table)
        text.status = "Decrypted"
        text.contents = text.contents.lower().translate(tabel)
        print(f"Decryption completed\n {text}")

# class RotOmega:
#
#     @staticmethod
#     def omega_encryption(text: Text) -> str:
#         mode = text.rot_type
#         if abs(mode) > 26:
#             mode = mode % 26
#         alphabet = string.ascii_lowercase
#         char_table = alphabet[mode:] + alphabet[:mode]
#         tabel = str.maketrans(alphabet, char_table)
#         return text.contents.lower().translate(tabel)
