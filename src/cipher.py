from abc import ABC, abstractmethod
import string
from buffer import Text


class Rot(ABC):
    """Logic of encryption and decryption"""

    @abstractmethod
    def encrypt(self, text: Text):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text: Text):
        raise NotImplementedError

    @abstractmethod
    def transform(self, alphabet, char_table, text):
        raise NotImplementedError


def get_rot(text: Text) -> None:
    if text.rot_type == 13:
        code13 = Rot13()
        if text.status.lower() == "decrypted":
            code13.encrypt(text)
        else:
            code13.decrypt(text)
    elif text.rot_type == 47:
        code47 = Rot47()
        if text.status.lower() == "decrypted":
            code47.encrypt(text)
        else:
            code47.decrypt(text)
    else:
        custom = RotCustomized()
        if text.status.lower() == "decrypted":
            custom.encryption(text)
        else:
            custom.decrypted(text)


class Rot13(Rot):
    def transform(self, alphabet, char_table, text):
        tabel = str.maketrans(alphabet, char_table)
        text.contents = text.contents.lower().translate(tabel)

    def encrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[13:] + alphabet[:13]
        self.transform(alphabet, char_table, text)
        text.status = "Encrypted"
        print(f"Encryption completed\n {text}")

    def decrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[-13:] + alphabet[:-13]
        self.transform(alphabet, char_table, text)
        text.status = "Decrypted"
        print(f"Decryption completed\n {text}")


class Rot47(Rot):
    def transform(self, alphabet, char_table, text):
        tabel = str.maketrans(alphabet, char_table)
        text.contents = text.contents.lower().translate(tabel)

    def encrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[21:] + alphabet[:21]
        self.transform(alphabet, char_table, text)
        text.status = "Encrypted"
        print(f"Encryption completed\n {text}")

    def decrypt(self, text: Text) -> None:
        alphabet = string.ascii_lowercase
        char_table = alphabet[-21:] + alphabet[:-21]
        self.transform(alphabet, char_table, text)
        text.status = "Decrypted"
        print(f"Decryption completed\n {text}")


class RotCustomized:
    def transform(self, alphabet, char_table, text):
        tabel = str.maketrans(alphabet, char_table)
        text.contents = text.contents.lower().translate(tabel)

    def _get_mode(self, text):
        mode = text.rot_type
        if abs(mode) > 26:
            mode = mode % 26
        return mode

    def encryption(self, text: Text) -> None:
        mode = self._get_mode(text)
        alphabet = string.ascii_lowercase
        char_table = alphabet[mode:] + alphabet[:mode]
        self.transform(alphabet, char_table, text)
        text.status = "Encrypted"
        print(f"Encryption completed\n {text}")

    def decrypted(self, text: Text):
        mode = self._get_mode(text)
        alphabet = string.ascii_lowercase
        char_table = alphabet[-mode:] + alphabet[:-mode]
        self.transform(alphabet, char_table, text)
        text.status = "Decrypted"
        print(f"Decryption completed\n {text}")
