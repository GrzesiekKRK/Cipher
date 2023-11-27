import cipher
import json


class FileHandler:
    def __init__(self, filename: str, contents: [cipher.Text]):
        self.filename = filename
        self.contents = contents

    def write(self) -> None:
        data = {"data": self.contents}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def append(self) -> None:
        with open(self.filename, "w") as f:
            json.dump(self.contents, f, indent=4)

    @staticmethod
    def read_file(filename: str) -> dict:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
